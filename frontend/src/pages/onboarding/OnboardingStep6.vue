<template>
  <div class="size-container">
  <div class="welcome-container">
    <div class="content">
      <BackButtonText />
      <img src="/src/assets/Step5.svg" alt="Person form" class="person-image" />
      <h2 class="form-step">
        <span class="form-step-highlight">{{ $t('onboarding.onboardingStep5.step') }}</span> {{ $t('onboarding.onboardingStep5.title') }}
      </h2>
      <div class="description">
        {{ $t('onboarding.onboardingStep5.description') }}
      </div>
      <div class="slider">
        <SliderWithLabelVertical10 :topText="$t('onboarding.onboardingStep5.slider.topText')" :bottomText="$t('onboarding.onboardingStep5.slider.bottomText')" />
      </div>
    </div>
    <div class="button-container">
      <StandardButton :label="$t('buttons.next')" @click="navigateToNextStep" />
    </div>
  </div>
  </div>
</template>

<script>
import StandardButton from 'components/StandardButton.vue';
import BackButtonText from 'components/BackButtonText.vue';
import SliderWithLabelVertical10 from 'src/components/SliderWithLabelVertical10.vue';

export default {
  components: {
    StandardButton,
    BackButtonText,
    SliderWithLabelVertical10
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

.content {
  flex: 1;
  overflow-y: auto;
}

.person-image {
  margin-bottom: 20px;
  margin-top: 10px;
  width: 100%;
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
  margin-bottom: 20px; 
}

.form-group p {
  margin: 0; 
  font-size: 16px;
  margin-left: 7px;
  margin-right: 7px;
}

.description {
  font-size: 16px;
  margin-left: 7px;
  margin-right: 7px;
  margin-bottom: 10px;
}

.slider {
  margin-top: 40px;
  margin-right: 12%;
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
