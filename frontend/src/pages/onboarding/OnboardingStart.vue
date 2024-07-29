<template>
  <div class="size-container">
    <div class="welcome-container">
      <img src="~assets/Image_OnboardingStart.svg" alt="Welcome Image" class="image" />
      <div class="welcome-text">
        <h1 class="title">{{ $t('onboarding.start.title')}}</h1>
        <p class="description">{{ $t('onboarding.start.description')}}</p>
      </div>
      <div class="button-container">
        <StandardButton :label="$t('buttons.next')" @click="navigateToOnboardingStep1" />
      </div>
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
        this.$router.push({ name: 'OnboardingStep1' });
      }
    }
  };
  </script>

  <style scoped>
  .welcome-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    overflow: auto;
    margin: auto;
  }

  .image {
    object-fit: auto;
    object-position: center;
    margin-top: 20px;
    width: 70%;
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
    bottom: 30px;
    width: 100%;
    display: flex;
    justify-content: center;
    left: 0;
  }

  </style>
