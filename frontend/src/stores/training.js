import { defineStore } from 'pinia';
import { api } from 'src/boot/axios';

export const useTrainingStore = defineStore('training', {
  state: () => ({
    userId: null,
    trainingData: {
      sport: null,
      duration: null,
      intensity: null
    },
    authToken: null
  }),
  actions: {
    setUserId(userId) {
      this.userId = userId;
    },
    setTrainingData({ sport, duration }) {
      this.trainingData.sport = sport;
      this.trainingData.duration = duration;
    },
    setTrainingIntensity(intensity) {
      this.trainingData.intensity = intensity;
    },
    setAuthToken(token) {
      this.authToken = token;
    },
    async saveTrainingData() {
      try {
        await api.post('/training/workouts/', {
          start: new Date().toISOString(),
          duration: this.trainingData.duration,
          intensity: this.trainingData.intensity,
          sport: this.trainingData.sport
        }, {
          headers: {
            Authorization: `Bearer ${this.authToken}`
          }
        });
        alert('Training data saved successfully');
      } catch (error) {
        console.error('Failed to save training data:', error);
        alert('Failed to save training data');
      }
    },
    async refreshAccessToken() {
      try {
        const response = await api.post('/auth/refresh/', {
          // Add necessary data for token refresh if required
        });
        this.setAuthToken(response.data.token);
      } catch (error) {
        console.error('Failed to refresh access token:', error);
      }
    }
  }
});
