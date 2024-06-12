import { defineStore } from 'pinia';
import axios from 'axios';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    accessToken: localStorage.getItem('accessToken') || '',
    refreshToken: localStorage.getItem('refreshToken') || '',
  }),
  actions: {
    async login(credentials) {
      const response = await axios.post('http://localhost:8000/api/users/token/', credentials);
      this.setAccessToken(response.data.access);
      this.setRefreshToken(response.data.refresh);
    },
    async refreshAccessToken() {
      const response = await axios.post('http://localhost:8000/api/users/token/refresh/', {
        refresh: this.refreshToken,
      });
      this.setAccessToken(response.data.access);
      return response.data.access;
    },
    setAccessToken(token) {
      this.accessToken = token;
      localStorage.setItem('accessToken', token);
    },
    setRefreshToken(token) {
      this.refreshToken = token;
      localStorage.setItem('refreshToken', token);
    },
    clearTokens() {
      this.accessToken = '';
      this.refreshToken = '';
      localStorage.removeItem('accessToken');
      localStorage.removeItem('refreshToken');
    },
    logout() {
      this.clearTokens();
    },
  },
  getters: {
    isAuthenticated: (state) => !!state.accessToken,
  },
});
