import { defineStore } from 'pinia';

export const useLogTrainingStore = defineStore('logTraining', {
  state: () => ({
    trainingStatus: null,
    selectedActivity: null,
    duration: null,
    intensity: null,
  }),
  actions: {
    setTrainingStatus(status) {
      this.trainingStatus = status;
    },
    setSelectedActivity(activity) {
      this.selectedActivity = activity;
    },
    setDuration(duration) {
      this.duration = duration;
    },
    setIntensity(intensity) {
      this.intensity = intensity;
    },
    async saveTrainingData() {
      try {
        await api.post('/training/workouts/', {
          start: new Date().toISOString(),
          duration: this.duration,
          intensity: this.intensity,
          sport: this.selectedActivity,
        });
        // Reset store state after successful save
        this.trainingStatus = null;
        this.selectedActivity = null;
        this.duration = null;
        this.intensity = null;
      } catch (error) {
        console.error('Failed to save workout:', error);
      }
    },
  },
});
