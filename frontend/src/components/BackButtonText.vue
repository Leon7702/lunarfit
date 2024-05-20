<template>
    <div @click="navigateBack">
      <img src="/src/assets/BackButton_with_text.svg" alt="Zurück" />
    </div>
  </template>
  
  <script>
  export default {
    methods: {
      navigateBack() {
        this.$router.go(-1); // Navigiert zur vorherigen Seite
      }
    }
  };
  </script>
  