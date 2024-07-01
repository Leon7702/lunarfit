<template>
  <div class="welcome-container">
    <div class="content">
      <BackButtonText />
      <img src="/src/assets/Step3.svg" alt="Person form" class="person-image" />
      <h2 class="form-step">
        <span class="form-step-highlight">{{ $t('onboarding.onboardingStep3.step') }}</span> {{ $t('onboarding.onboardingStep3.title') }}
      </h2>
      <div class="form-group">
        <p>{{ $t('onboarding.onboardingStep3.fields.hormonalContraception') }}</p>
        <RadioToggle v-model="hormonalContraception" />
      </div>
      <div class="form-group" v-if="hormonalContraception === 'ja'">
        <p>{{ $t('onboarding.onboardingStep3.fields.contraceptionMethod') }}</p>
        <DropDownSingleSelect :options="contraceptionOptions"/>
      </div>
    </div>
    <div class="button-container">
      <StandardButton label="Weiter" @click="navigateToNextStep" />
    </div>
  </div>
</template>

<script>
import StandardButton from 'components/StandardButton.vue';
import BackButtonText from 'components/BackButtonText.vue';
import RadioToggle from 'components/RadioToggle.vue';
import DropDownSingleSelect from 'components/DropDownSingleSelect.vue';

export default {
  components: {
    StandardButton,
    BackButtonText,
    RadioToggle,
    DropDownSingleSelect
  },
  data() {
    return {
      hormonalContraception: null,
      contraceptionOptions: [
        {
          value: 'pille',
          label: this.$t('onboarding.onboardingStep3.fields.contraceptionOptions.pille')
        },
        {
          value: 'hormonspirale',
          label: this.$t('onboarding.onboardingStep3.fields.contraceptionOptions.hormonspirale')
        },
        {
          value: 'hormonimplantat',
          label: this.$t('onboarding.onboardingStep3.fields.contraceptionOptions.hormonimplantat')
        },
        {
          value: 'dreimonatsspritze',
          label: this.$t('onboarding.onboardingStep3.fields.contraceptionOptions.dreimonatsspritze')
        },
        {
          value: 'vaginalring',
          label: this.$t('onboarding.onboardingStep3.fields.contraceptionOptions.vaginalring')
        },
        {
          value: 'sonstiges',
          label: this.$t('onboarding.onboardingStep3.fields.contraceptionOptions.sonstiges')
        }
      ]
    };
  },
  methods: {
    goBack() {
      window.history.back();
    },
    navigateToNextStep() {
      this.$router.push({ name: 'OnboardingStep5' });
    }
  }
};
</script>

  
  <style scoped>
  .welcome-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 20px;
    position: relative;
    height: 100vh; 
  }
  
  .content {
    width: 90%;
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
  
  .button-container {
    position: fixed;
    bottom: 30px;
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
