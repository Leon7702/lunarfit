import axios from 'axios';
import { useAuthStore } from '../stores/auth';
import router from '../router';

const api = axios.create({
  baseURL: 'http://localhost:8000/api',
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
    if (error.response.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;
      const authStore = useAuthStore();
      try {
        const newAccessToken = await authStore.refreshAccessToken();
        api.defaults.headers.common['Authorization'] = 'Bearer ' + newAccessToken;
        return api(originalRequest);
      } catch (e) {
        authStore.logout();
        router.push('/login');
        return Promise.reject(e);
      }
    }
    return Promise.reject(error);
  }
);

export default api;
