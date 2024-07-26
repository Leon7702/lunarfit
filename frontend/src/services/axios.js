import axios from 'axios';
import { useAuthStore } from '../stores/auth';
import router from '../router';

const api = axios.create({
  baseURL: 'http://localhost:8000',
});

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

export default api;
