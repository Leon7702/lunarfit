import { defineStore } from 'pinia';
import axios from 'axios';

function parseJwt(token) {
  const base64Url = token.split('.')[1];
  const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
  const jsonPayload = decodeURIComponent(atob(base64).split('').map(function(c) {
    return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
  }).join(''));

  return JSON.parse(jsonPayload);
}

export const useAuthStore = defineStore('auth', {
  state: () => ({
    accessToken: localStorage.getItem('accessToken') || '',
    refreshToken: localStorage.getItem('refreshToken') || '',
    userId: localStorage.getItem('userId') || null,
  }),
  actions: {
    async login(credentials) {
      try {
        const response = await axios.post('http://localhost:8000/api/users/token/', credentials);
        this.setAccessToken(response.data.access);
        this.setRefreshToken(response.data.refresh);

        const decodedToken = parseJwt(response.data.access);
        const userId = decodedToken.user_id; // Angenommen, die Benutzer-ID ist im Token enthalten
        this.setUserId(userId);
      } catch (error) {
        console.error('Failed to login:', error);
        throw error;
      }
    },

    async refreshAccessToken() {
      try {
        const response = await axios.post('http://localhost:8000/api/users/token/refresh/', {
          refresh: this.refreshToken,
        });
        this.setRefreshToken(response.data.refresh);
        this.setAccessToken(response.data.access);

        const decodedToken = parseJwt(response.data.access);
        const userId = decodedToken.user_id; // Angenommen, die Benutzer-ID ist im Token enthalten
        this.setUserId(userId);
        return response.data.access;
      } catch (error) {
        console.error('Failed to refresh access token:', error);
        throw error;
      }
    },
    setAccessToken(token) {
      this.accessToken = token;
      localStorage.setItem('accessToken', token);
    },
    setRefreshToken(token) {
      this.refreshToken = token;
      localStorage.setItem('refreshToken', token);
    },
    setUserId(userId) {
      this.userId = userId;
      localStorage.setItem('userId', userId);
    },
    clearTokens() {
      this.accessToken = '';
      this.refreshToken = '';
      this.userId = null;
      localStorage.removeItem('accessToken');
      localStorage.removeItem('refreshToken');
      localStorage.removeItem('userId');
    },
    logout() {
      this.clearTokens();
    },
  },
  getters: {
    isAuthenticated: (state) => !!state.accessToken,
  },
});
