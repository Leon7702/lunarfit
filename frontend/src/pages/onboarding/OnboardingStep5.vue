<template>
  <div class="size-container">
  <div class="welcome-container">
    <div class="content">
      <BackButtonText />
      <img src="/src/assets/Step4.svg" alt="Person form" class="person-image" />
      <h2 class="form-step">
        <span class="form-step-highlight">{{ $t('onboarding.onboardingStep4.step') }}</span> {{ $t('onboarding.onboardingStep4.title') }}
      </h2>
      <div class="form-group">
        <p>{{ $t('onboarding.onboardingStep4.fields.trainingSessions') }}</p>
        <FormFieldText id="count" label="" iconName="" inputType="number" />
      </div>
      <div class="form-group">
        <p>{{ $t('onboarding.onboardingStep4.fields.trainingDuration') }}</p>
        <FormFieldText id="duration" label="" iconName="" inputType="number" />
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
import FormFieldText from 'components/FormFieldText.vue';

export default {
  components: {
    StandardButton,
    BackButtonText,
    FormFieldText
  },
  methods: {
    goBack() {
      window.history.back();
    },
    navigateToNextStep() {
      this.$router.push({ name: 'OnboardingStep6' });
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
    margin-bottom: 10px; 
  }

  .form-group p {
    margin: 0;
    font-size: 16px;
    margin-left: 7px;
    margin-right: 7px;
  }

  .form-group-one p {
    margin: 0;
    font-size: 16px;
    margin-left: 7px;
    margin-right: 7px;
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
