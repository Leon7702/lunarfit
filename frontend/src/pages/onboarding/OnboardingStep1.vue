<template>
  <div class="size-container">
  <div class="welcome-container">
    <div class="content">
      <BackButtonText />
      <img src="/src/assets/Step1.svg" alt="Person form" class="person-image" />
      <h2 class="form-step">
        <span class="form-step-highlight">{{ $t('onboarding.onboardingStep1.step')}}</span> {{ $t('onboarding.onboardingStep1.title') }}
      </h2>
      <FormFieldText id="firstName" :label="$t('onboarding.onboardingStep1.fields.firstName')" iconName="" inputType="text" />
      <FormFieldText id="lastName" :label="$t('onboarding.onboardingStep1.fields.lastName')" iconName="" inputType="text" pattern="" />
      <FormFieldText id="birthdate" :label="$t('onboarding.onboardingStep1.fields.birthdate')" iconName="" inputType="date" />
      <FormFieldText id="height" :label="$t('onboarding.onboardingStep1.fields.height')" iconName="" inputType="number" />
      <FormFieldText id="weight" :label="$t('onboarding.onboardingStep1.fields.weight')" iconName="" inputType="number" />
      <div class="button-container">
        <StandardButton :label="$t('buttons.next')" @click="navigateToNextStep" />
      </div>
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

.button-container {
  position: fixed;
  bottom: 30px; 
  width: 100%;
  display: flex;
  justify-content: center;
  left: 0;
}

</style>
