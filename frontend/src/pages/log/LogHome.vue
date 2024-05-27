<template>
    <div class="welcome-container">
      <!-- Inhalt des ersten Bildschirms hier... -->
      <div class="welcome-text">
        <h1 class="title">Log-Eintrag</h1>
      </div>
      <DateTodayPicker class="date" />
      <img src="/src/assets/log_zyklus.svg" alt="Zyklus Button" class="image" label="Weiter" @click="navigateToNextStep" />
      <img src="/src/assets/log_training.svg" alt="Training Button" class="image" />
    </div>
  </template>
  
  <script>
  import DateTodayPicker from 'components/DateTodayPicker.vue'

export default {
  components: {
    DateTodayPicker
  },
  methods: {
    goBack() {
      window.history.back();
    },
    navigateToNextStep() {
      this.$router.push({ name: 'LogCycleHome' });
    }
  }
};
 
  </script>
  
  <style scoped>
  .welcome-container {
    display: flex;
    flex-direction: column;
    align-items: center; /* Zentriert den Inhalt horizontal */
    padding-left: 20px;
    padding-right: 20px;
    height: 100vh; /* Vollbildhöhe */
    overflow: auto;
    margin: auto;
  }
  
  .image {
    aspect-ratio: 1.94;
    object-fit: auto;
    object-position: center;
    width: 100%;
  }
  
  .welcome-text {
    margin-top: 60px;
  }
  
  .title {
    font: 600 24px 'Inter', sans-serif; 
  }

  .date {
    margin-bottom: 20px;
  }
  
  @media only screen and (min-width: 600px) {
    .welcome-container {
      max-width: 500px;
      margin: auto;
    }
  }
  </style>
