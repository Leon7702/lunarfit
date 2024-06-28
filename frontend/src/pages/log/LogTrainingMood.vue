<template>
    <div class="welcome-container">
      <div class="header">
        <q-btn flat dense round icon="arrow_back" @click="goBack" />
        <div class="title">Stimmung</div>
      </div>
      <div class="linie"></div>
      <div class="description">
        Wie bewertest du deine <br>heutige Stimmung?
      </div>
      <div class="slider">
        <SliderWithLabelVertical topText="Glücklich" bottomText="Traurig" />
      </div>
      <div class="button-container">
        <StandardButton label="Weiter" @click="navigateToNextStep" />
      </div>
    </div>
  </template>
  
  <script>
  import SliderWithLabelVertical from 'components/SliderWithLabelVertical.vue';
  import StandardButton from 'components/StandardButton.vue'
  
  export default {
    components: {
      SliderWithLabelVertical,
      StandardButton
    },
    methods: {
      goBack() {
        window.history.back();
      },
    navigateToNextStep() {
      this.$router.push({ name: 'LogTrainingRecovery' });
    }
    }
  };
  </script>
  
  <style scoped>
  .welcome-container {
    display: flex;
    flex-direction: column;
    align-items: center; /* Ausrichtung links */
    width: 90%;
    height: 100vh;
    overflow: auto;
    margin: auto;
  }
  
  .linie {
    height: 1px;
    background-color: rgba(0, 0, 0, 0.1);
    width: 120%;
    margin-top: 10px;
  }
  
  .header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    padding: 10px 0;
    margin-top: 20px;
  }
  
  .title {
    font: 600 20px 'Inter', sans-serif;
    color: #000;
    text-align: center;
    flex-grow: 1;
    padding-right: 30px;
  }

  .description {
    text-align: center;
    width: 100%;
    margin-top: 30px;
    font-size: 16px;
    font-weight: 500;
    margin-bottom: 10px;
  }
  .slider {
    margin-top: 40px;
    padding-right: 6%;
  }

  .button-container {
    position: fixed;
    bottom: 80px;  
    width: 100%;
    display: flex;
    justify-content: center;
    left: 0;
  }

  @media only screen and (min-width: 200px) {
    .welcome-container {
      max-width: 350px;
      margin: auto;
    }
  }
  </style>
  