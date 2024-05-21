<template>
  <div class="welcome-container">
    <div class="content">
      <BackButtonText />
      <img src="/src/assets/Step1.svg" alt="Person form" class="person-image" />
      <h2 class="form-step">
        <span class="form-step-highlight">Schritt 1:</span> Person
      </h2>
      <FormFieldText id="firstName" label="Vorname" iconName="" inputType="text" />
      <FormFieldText id="lastName" label="Nachname" iconName="" inputType="text" />
      <FormFieldText id="birthdate" label="Geburtsdatum" iconName="" inputType="date" />
      <FormFieldText id="height" label="Größe in cm" iconName="" inputType="number" />
      <FormFieldText id="weight" label="Gewicht in kg" iconName="" inputType="number" />
      <div class="button-container">
        <StandardButton label="Weiter" @click="navigateToNextStep" />
      </div>
    </div>
  </div>
</template>

<script>
import StandardButton from 'components/StandardButton.vue';
import FormFieldText from 'components/FormFieldText.vue';
import BackButtonText from 'components/BackButtonText.vue';

export default {
  components: {
    StandardButton,
    FormFieldText,
    BackButtonText
  },
  methods: {
    goBack() {
      window.history.back();
    },
    navigateToNextStep() {
      this.$router.push({ name: 'OnboardingStep2' });
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

.button-container {
  position: fixed;
  bottom: 30px; /* Adjust this value to set the distance from the bottom */
  width: 100%;
  display: flex;
  justify-content: center;
  left: 0;
}
</style>
