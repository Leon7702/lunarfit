import { boot } from 'quasar/wrappers'
import axios from 'axios'
import { useAuthStore } from '../stores/auth';
import router from '../router';

// Be careful when using SSR for cross-request state pollution
// due to creating a Singleton instance here;
// If any client changes this (global) instance, it might be a
// good idea to move this instance creation inside of the
// "export default () => {}" function below (which runs individually
// for each client)

const api = axios.create({ baseURL: process.env.API})

export default boot(({ app }) => {

  // Request interceptor to add Authorization header
  api.interceptors.request.use((config) => {
    const authStore = useAuthStore();
    const token = authStore.accessToken;
    if (token) {
      config.headers['Authorization'] = `Bearer ${token}`;
    }
    return config;
  }, (error) => {
    return Promise.reject(error);
  });

  // Response interceptor for handling errors
  api.interceptors.response.use(
    (response) => response,
    async (error) => {
      const originalRequest = error.config;
      const authStore = useAuthStore();

      if (error.response) {
        switch (error.response.status) {
          case 401:
            if (!originalRequest._retry) {
              originalRequest._retry = true;
              try {
                const newAccessToken = await authStore.refreshAccessToken();
                api.defaults.headers.common['Authorization'] = 'Bearer ' + newAccessToken;
                originalRequest.headers['Authorization'] = 'Bearer ' + newAccessToken;
                return api(originalRequest);
              } catch (e) {
                authStore.logout();
                router.push('/login');
                return Promise.reject(e);
              }
            }
            break;

          case 403:
            console.error('Access forbidden: logging out...');
            authStore.logout();
            router.push('/login');
            break;

          case 500:
            console.error('Server error: please try again later.');
            // router.push('/server-error');
            break;

          default:
            break;
        }
      }

      return Promise.reject(error);
    }
  );

  // for use inside Vue files (Options API) through this.$axios and this.$api

  app.config.globalProperties.$axios = axios
  // ^ ^ ^ this will allow you to use this.$axios (for Vue Options API form)
  //       so you won't necessarily have to import axios in each vue file

  app.config.globalProperties.$api = api
  // ^ ^ ^ this will allow you to use this.$api (for Vue Options API form)
  //       so you can easily perform requests against your app's API
})

export { api }
