<template>
    <div class="welcome-container">
      <div class="content">
        <BackButtonText />
        <img src="/src/assets/Step5.svg" alt="Person form" class="person-image" />
        <h2 class="form-step">
          <span class="form-step-highlight">Schritt 5:</span> Sportverhalten
        </h2>
        <div class="description">
          Wie intensiv waren deine Trainingseinheiten im Durchschnitt im letzten Monat?
        </div>
        <div class="slider">
          <SliderWithLabelVertical10 topText="Maximal anstrengend" bottomText="Gar nicht anstrengend" />
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
  import SliderWithLabelVertical10 from 'src/components/SliderWithLabelVertical10.vue';
  
  export default {
    components: {
      StandardButton,
      BackButtonText,
      SliderWithLabelVertical10
    },
    data() {
      return {
        contraceptionOptions: ['60 Minuten oder weniger', '60 bis 120 Minuten', '120 Minuten oder mehr']
      }
    },
    methods: {
      goBack() {
        window.history.back();
      },
      navigateToNextStep() {
        this.$router.push({ name: 'OnboardingEnd' });
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
    width: 90%;
    flex: 1;
    overflow-y: auto;
  }
  
  .person-image {
    margin-bottom: 20px;
    margin-top: 10px;
    width: 100%;
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
    margin-bottom: 20px; 
  }
  
  .form-group p {
    margin: 0; 
    font-size: 16px;
    margin-left: 7px;
    margin-right: 7px;
  }

  .description {

    font-size: 16px;
    margin-left: 7px;
    margin-right: 7px;
    margin-bottom: 10px;
  }
  .slider {
    margin-top: 40px;
    margin-right: 12%;
  }
  
  .button-container {
    position: fixed;
    bottom: 30px; 
    width: 100%;
    display: flex;
    justify-content: center;
    left: 0;
  }

  @media only screen and (min-width: 500px) {
    .welcome-container {
      max-width: 500px;
      margin: auto;
      margin-top: 5%;
    }
  }
  </style>
