<template>
    <div class="welcome-container">
      <div class="content">
        <BackButtonText />
        <img src="/src/assets/Step3.svg" alt="Person form" class="person-image" />
        <h2 class="form-step">
          <span class="form-step-highlight">Schritt 3:</span> Zyklus
        </h2>
        <div class="form-group">
          <p>Ist dein Zyklus regelmäßig?</p>
          <RadioToggle/>
        </div>
        <div class="form-group">
          <p>Hast du während 5 Tagen vor oder während deiner Menstruation Symptome?</p>
          <RadioToggle/>
        </div>
      </div>
      <div class="button-container">
        <StandardButton label="Weiter" @click="navigateToNextStep" />
      </div>
    </div>
  </template>
  
  <script>
  import StandardButton from 'components/StandardButton.vue';
  import BackButtonText from 'components/BackButtonText.vue';
  import RadioToggle from 'components/RadioToggle.vue'
  
  export default {
    components: {
      StandardButton,
      BackButtonText,
      RadioToggle
    },
    methods: {
      goBack() {
        window.history.back();
      },
      navigateToNextStep() {
        this.$router.push({ name: 'OnboardingStep4' });
      }
    }
  };
  </script>
  
  <style scoped>
  .welcome-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 60px;
    position: relative;
    height: 100vh;
  }
  
  .content {
    max-width: 324px;
    flex: 1; 
    overflow-y: auto;
  }
  
  .person-image {
    margin-bottom: 20px;
    margin-top: 10px;
  }
  
  .form-step {
    color: #50c1ba;
    font: 700 20px/31px Inter, sans-serif;
    margin-left: 7px;
  }
  
  .form-step-highlight {
    color: rgba(80, 193, 186, 1);
  }
  
  .form-group {
    margin-bottom: 10px; 
  }
  
  .form-group p {
    margin: 0; 
    font-size: 16px;
    margin-left: 7px;
    margin-right: 7px;
  }
  
  .button-container {
    position: fixed;
    bottom: 30px; 
    width: 100%;
    display: flex;
    justify-content: center;
    left: 0;
  }
  </style>
