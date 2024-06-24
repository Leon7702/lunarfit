<template>
    <div class="welcome-container">
      <div class="header">
        <q-btn flat dense round icon="arrow_back" @click="goBack" />
        <div class="title">Geschlechtsverkehr</div>
      </div>
      <div class="linie"></div>
      <div class="description">
        Bitte zutreffendes auswählen:
      </div>
      <div class="form-group">
        <DropDownSingleSelect :options="contraceptionOptions"/>
      </div>
    </div>
  </template>
  
  <script>
  
  import DropDownSingleSelect from 'components/DropDownSingleSelect.vue';
  
  export default {
    components: {
      DropDownSingleSelect
    },
    data() {
      return {
        hormonalContraception: null,
        contraceptionOptions: ['Kein Sex', 'Geschützter Sex', 'Ungeschützter Sex', 'Lust auf Sex', 'Masturbation']
      }
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
    align-items: center;
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
    text-align: left;
    width: 100%;
    margin-top: 30px;
    font-size: 16px;
    font-weight: 500;
    margin-bottom: 10px;
  }
  .form-group {
    width: 100%;
  }
  
  .form-group p {
    margin: 0; 
    font-size: 16px;
    margin-left: 7px;
    margin-right: 7px;
  }
  
  @media only screen and (min-width: 200px) {
    .welcome-container {
      max-width: 350px;
      margin: auto;
    }
  }
  
  </style>
  