<template>
    <div class="welcome-container">
      <!-- Inhalt des ersten Bildschirms hier... -->
      <img src="/src/assets/Image_OnboardingEnd.svg" alt="Welcome Image" class="image" />
      <div class="welcome-text">
        <h1 class="title">Geschafft!</h1>
        <p class="description">
          Vielen Dank für das Ausfüllen der Fragen. Auf Basis deiner Antworten werden dir bereits anfängliche Empfehlungen abgegeben.
          <br />
          <br />
          Denk daran: Je genauer du deinen Zyklus und dein Sportverhalten trackst, desto genauer werden deine Empfehlungen.
        </p>
      </div>
      <!-- Verwendung der StandardButton-Komponente für den "Weiter"-Button -->
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
        // Weiterleitung zur Vue-Komponente des zweiten Bildschirms
        this.$router.push({ name: 'OnboardingStart' }); // Passe den Routenname entsprechend an
      }
    }
  };
  </script>
  
  <style scoped>
  .welcome-container {
    display: flex;
    flex-direction: column;
    align-items: center; /* Zentriert den Inhalt horizontal */
    padding-left: 20px;
    padding-right: 20px;
    height: 100vh; /* Vollbildhöhe */
    overflow: auto;
    margin: auto;
  }
  
  .image {
    aspect-ratio: 1.64;
    object-fit: auto;
    object-position: center;
    margin-top: 60px;
    width: 100%;
  }
  
  .welcome-text {
    text-align: left; /* Text links ausrichten */
  }
  
  .title {
    font: 600 24px/129% 'Inter', sans-serif; /* Füge Inter als Schriftart hinzu */
    margin-top: 5vh;
  }
  
  .description {
    font: 16px/22px 'Inter', sans-serif; /* Füge Inter als Schriftart hinzu */
    margin-top: 3vh;
  }
  
  .button-container {
    position: fixed;
    bottom: 30px; /* Abstand vom unteren Rand des Bildschirms */
    width: 100%;
    display: flex;
    justify-content: center;
    left: 0;
  }
  
  @media only screen and (min-width: 600px) {
    .welcome-container {
      max-width: 500px;
      margin: auto;
    }
  }
  </style>
  