<template>
  <div class="welcome-container">
    <div class="header">
      <q-btn flat dense round icon="arrow_back" @click="goBack" />
      <div class="title">Profil</div>
    </div>
    <div class="linie"></div>
  </div>
</template>

<script>

  export default {
    components: {

    },
    data() {
      return {

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
    padding-left: 20px;
    padding-right: 20px;
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

  </style>
