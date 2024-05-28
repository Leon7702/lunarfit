<template>
    <div class="welcome-container">
      <div class="header">
        <q-btn flat dense round icon="arrow_back" @click="goBack" />
        <div class="title">Menstruation</div>
      </div>
      <div class="linie"></div>
      <div class="button-container">
        <StandardButton :label="buttonLabel" @click="toggleMenstruationStatus" />
      </div>
      <div class="welcome-text">
        <p class="description">{{ descriptionText }}</p>
      </div>
    </div>
  </template>
  
  <script>
  import StandardButton from 'components/StandardButton.vue';
  
  export default {
    components: {
      StandardButton
    },
    data() {
      return {
        buttonLabel: "+  Menstruation",
        descriptionText: "Tippe hier, wenn deine Menstruation heute begonnen hat."
      };
    },
    methods: {
      goBack() {
        window.history.back();
      },
      toggleMenstruationStatus() {
        if (this.buttonLabel === "+  Menstruation") {
          this.buttonLabel = "Menstruation aktiv";
          this.descriptionText = "Tippe hier, wenn deine Menstruation vorbei ist.";
        } else {
          this.buttonLabel = "+  Menstruation";
          this.descriptionText = "Tippe hier, wenn deine Menstruation heute begonnen hat.";
        }
      }
    }
  };
  </script>
  
  <style scoped>
  .welcome-container {
    display: flex;
    flex-direction: column;
    align-items: flex-start; /* Ausrichtung links */
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
    margin-top: 60px;
  }
  
  .title {
    font: 600 20px 'Inter', sans-serif;
    color: #000;
    text-align: center;
    flex-grow: 1;
    padding-right: 30px;
  }
  
  .description {
    font: 12px/22px 'Inter', sans-serif;
    margin-top: 5px;
  }
  
  .button-container {
    margin-top: 20px;
    margin-left: 0; 
    width: 100%;
  }
  </style>
  