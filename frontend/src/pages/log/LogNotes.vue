<template>
    <div class="welcome-container">
      <div class="header">
        <q-btn flat dense round icon="arrow_back" @click="goBack" />
        <div class="title">Notizen</div>
      </div>
      <div class="linie"></div>
      <div class="description">
        Füge eine Notiz hinzu:
      </div>
      <div class="textarea">
        <InputTextArea v-model="notes" />
      </div>
      <div class="button-container">
        <StandardButton @click="saveChanges" label="Speichern" />
      </div>
    </div>
  </template>
  
  <script>
  import InputTextArea from 'components/InputTextArea.vue';
  import StandardButton from 'components/StandardButton.vue';
  
  export default {
    components: {
      InputTextArea,
      StandardButton
    },
    data() {
      return {
        notes: ''
      };
    },
    methods: {
      goBack() {
        window.history.back();
      }
    }
  };
  </script>
  
  <style scoped>
  .welcome-container {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
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
    text-align: left;
    width: 100%;
    margin-top: 30px;
    font-size: 16px;
    font-weight: 500;
    margin-bottom: 15px;
  }
   .textarea {
    width:100%;
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
  