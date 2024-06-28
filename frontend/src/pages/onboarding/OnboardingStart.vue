<template>
    <div class="welcome-container">
      <img src="/src/assets/Image_OnboardingStart.svg" alt="Welcome Image" class="image" />
      <div class="welcome-text">
        <h1 class="title">Willkommen bei LunarFit.</h1>
        <p class="description">
          Um dich und deinen Zyklus besser kennenzulernen, beantworte bitte die
          folgenden Fragen über deinen Körper, deinen Zyklus und dein Sportverhalten.
          <br />
          <br />
          Deine Daten werden streng vertraulich behandelt und sicher aufbewahrt.
        </p>
      </div>
      <div class="button-container">
        <StandardButton label="Weiter" @click="navigateToOnboardingStep1" />
      </div>
    </div>
  </template>
  
  <script>
  import StandardButton from 'components/StandardButton.vue';
  
  export default {
    components: {
      StandardButton
    },
    methods: {
      navigateToOnboardingStep1() {
        this.$router.push({ name: 'OnboardingStep1' }); 
      }
    }
  };
  </script>
  
  <style scoped>
  .welcome-container {
    display: flex;
    flex-direction: column;
    align-items: center; 
    width: 90%;
    height: 100vh; 
    overflow: auto;
    margin: auto;
  }
  
  .image {
    object-fit: auto;
    object-position: center;
    margin-top: 20px;
    width: 70%;
  }
  
  .welcome-text {
    text-align: left; 
  }
  
  .title {
    font: 600 24px/129% 'Inter', sans-serif; 
    margin-top: 5vh;
  }
  
  .description {
    font: 16px/22px 'Inter', sans-serif; 
    margin-top: 3vh;
  }
  
  .button-container {
    position: fixed;
    bottom: 30px;
    width: 100%;
    display: flex;
    justify-content: center;
    left: 0;
  }
  
  @media only screen and (min-width: 200px) {
    .welcome-container {
      max-width: 350px;
      margin: auto;
      margin-top: 5%;
    }
  }
  </style>
