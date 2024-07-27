import { defineStore } from 'pinia';
import axios from 'axios';

export const useOnboardingStore = defineStore('onboarding', {
  state: () => ({
    userId: null,
    workout_frequency: null,
    workout_duration: null,
    workout_intensity: 1, // Initialwert auf Minimum gesetzt
    cycle_duration: null,
    menstruation_duration: null,
    last_menstruation: null,
    authToken: null // Add authToken to the state
  }),
  actions: {
    setUserId(userId) {
      this.userId = userId;
    },
    setWorkoutData({ frequency, duration }) {
      this.workout_frequency = frequency;
      this.workout_duration = duration;
    },
    setWorkoutIntensity(intensity) {
      this.workout_intensity = intensity;
    },
    setMenstruationData({ cycle_duration, menstruation_duration, last_menstruation }) {
      this.cycle_duration = cycle_duration;
      this.menstruation_duration = menstruation_duration;
      this.last_menstruation = last_menstruation;
    },
    setAuthToken(token) {
      this.authToken = token;
    },
    async refreshAccessToken() {
      try {
        const response = await axios.post('http://localhost:8000/api/auth/refresh/', {
          // Add necessary data for token refresh if required
        });
        this.setAuthToken(response.data.token);
      } catch (error) {
        console.error('Failed to refresh access token:', error);
      }
    }
  }
});
