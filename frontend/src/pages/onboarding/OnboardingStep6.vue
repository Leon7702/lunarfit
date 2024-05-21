<template>
    <div class="welcome-container">
      <div class="content">
        <BackButtonText />
        <img src="/src/assets/Step6.svg" alt="Person form" class="person-image" />
        <h2 class="form-step">
          <span class="form-step-highlight">Schritt 6:</span> Sportverhalten
        </h2>
        <div class="form-group">
          <p>Wie lange dauert eine durchschnittliche Trainingseinheit?</p>
          <DropDownSingleSelect :options="contraceptionOptions"/>
        </div>
        <div class="form-group">
            <p>Auf einer Skala von 1 - 6: Wie intensiv ist deine durchschnittliche Trainingseinheit?</p>
           <SliderWithLabel/>
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
  import DropDownSingleSelect from 'components/DropDownSingleSelect.vue';
  import SliderWithLabel from 'src/components/SliderWithLabel.vue';
  
  export default {
    components: {
      StandardButton,
      BackButtonText,
      DropDownSingleSelect,
      SliderWithLabel
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
    height: 100vh; /* Ensure the container takes up the full height of the viewport */
  }
  
  .content {
    max-width: 324px;
    flex: 1; /* Allow content to take up remaining space */
    overflow-y: auto; /* Ensure content is scrollable if it overflows */
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
    margin-bottom: 10px; /* Space between form groups */
  }
  
  .form-group p {
    margin: 0; /* Remove margin below paragraph */
    font-size: 16px;
    margin-left: 7px;
    margin-right: 7px;
  }
  
  .button-container {
    position: fixed;
    bottom: 30px; /* Adjust this value to set the distance from the bottom */
    width: 100%;
    display: flex;
    justify-content: center;
    left: 0;
  }
  </style>
