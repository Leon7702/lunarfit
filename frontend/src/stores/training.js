import { defineStore } from 'pinia';
import { api } from 'src/boot/axios';

export const useTrainingStore = defineStore('training', {
  state: () => ({
    start: '',
    duration: 0,
    intensity: 0,
    sport: 0,
    date: '',
    mood: 0,
    complaints: 0,
    recovery: 0,
  }),
  actions: {
    setStart(start) {
      this.start = start;
    },
    setDuration(duration) {
      this.duration = duration;
    },
    setIntensity(intensity) {
      this.intensity = intensity;
    },
    setSport(sport) {
      this.sport = sport;
    },
    setDate(date) {
      this.date = date;
    },
    setMood(mood) {
      this.mood = mood;
    },
    setComplaints(complaints) {
      this.complaints = complaints;
    },
    setRecovery(recovery) {
      this.recovery = recovery;
    },
    async saveWorkout() {
      try {
        await api.post('/training/workouts/', {
          start: this.start,
          duration: this.duration,
          intensity: this.intensity,
          sport: this.sport,
        });
      } catch (error) {
        console.error('Error saving workout data:', error);
        throw error;
      }
    },
    async saveTRS() {
      try {
        if (!this.date || this.mood === null || this.complaints === null || this.recovery === null) {
          throw new Error('Missing required fields');
        }

        await api.post('/training/trs/', {
          date: this.date,
          mood: this.mood,
          complaints: this.complaints,
          recovery: this.recovery,
        });
      } catch (error) {
        console.error('Error saving TRS data:', error);
        throw error;
      }
    },
  },
});
