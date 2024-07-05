<template>
  <div class="welcome-container">
    <img src="/src/assets/Image_OnboardingEnd.svg" alt="Welcome Image" class="image" />
    <div class="welcome-text">
      <h1 class="title">{{ $t('onboarding.onboardingEnd.title') }}</h1>
      <p class="description">
        {{ $t('onboarding.onboardingEnd.description') }}
      </p>
    </div>
    <div class="button-container">
      <StandardButton :label="$t('buttons.next')" @click="navigateToDashboard" />
    </div>
  </div>
</template>
  
  <script>
  import StandardButton from 'components/StandardButton.vue';
  
  export default {
  name: 'OnboardingEnd',
  components: {
    StandardButton
  },
  methods: {
    navigateToDashboard() {
      this.$router.push({ path: '/home' });
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
  
  .image {
    aspect-ratio: 1.64;
    object-fit: auto;
    object-position: center;
    margin-top: 20px;
    width: 100%;
  }
  
  .welcome-text {
    text-align: left; 
  }
  
  .title {
    font: 600 24px/129% 'Inter', sans-serif; 
    margin-top: 5vh;
  }
  
  .description {
    font: 16px/22px 'Inter', sans-serif; 
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
  
  @media only screen and (min-width: 200px) {
    .welcome-container {
      max-width: 350px;
      margin: auto;
      margin-top: 5%;
    }
  }
  </style>
  