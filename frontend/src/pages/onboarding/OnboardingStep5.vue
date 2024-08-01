<template>
  <div class="size-container">
    <div class="welcome-container">
      <div class="content">
        <BackButtonText />
        <img src="~assets/Step4.svg" alt="Person form" class="person-image" />
        <h2 class="form-step">
          <span class="form-step-highlight">{{ $t('onboarding.onboardingStep4.step') }}</span>
          {{ $t('onboarding.onboardingStep4.title') }}
        </h2>
        <div class="form-group">
          <p>{{ $t('onboarding.onboardingStep4.fields.trainingSessions') }}</p>
          <q-input
            ref="workoutFrequencyRef"
            filled
            v-model="workout_frequency"
            type="number"
            input-class="text-left input-text"
            class="q-mb-sm"
            :rules="workoutFrequencyRules"
          />
        </div>
        <div class="form-group">
          <p>{{ $t('onboarding.onboardingStep4.fields.trainingDuration') }}</p>
          <q-input
            ref="workoutDurationRef"
            filled
            v-model="workout_duration"
            type="number"
            input-class="text-left input-text"
            class="q-mb-sm"
            :rules="workoutDurationRules"
          />
        </div>
      </div>
      <div class="button-container">
        <StandardButton :label="$t('buttons.next')" @click="navigateToNextStep" />
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useI18n } from 'vue-i18n';
import { useOnboardingStore } from 'src/stores/onboarding';
import StandardButton from 'components/StandardButton.vue';
import BackButtonText from 'components/BackButtonText.vue';

export default {
  components: {
    StandardButton,
    BackButtonText
  },
  setup() {
    const { t } = useI18n();
    const onboardingStore = useOnboardingStore();
    const router = useRouter();

    const workout_frequency = ref(null);
    const workout_duration = ref(null);

    const workoutFrequencyRef = ref(null);
    const workoutDurationRef = ref(null);

    const workoutFrequencyRules = [
      val => !!val || t('validation.required'),
      val => val >= 0 && val <= 50 || t('validation.realisticFrequency'),
      val => Number.isInteger(Number(val)) || t('validation.realisticDay'),
    ];

    const workoutDurationRules = [
      val => !!val || t('validation.required'),
      val => val >= 0 || t('validation.positiveValue'),
      val => val <= 1440 || t('validation.realisticDuration'), // 1440 minutes = 24 hours
      val => Number.isInteger(Number(val)) || t('validation.realisticDay')
    ];

    const validateInput = () => {
      workoutFrequencyRef.value.validate();
      workoutDurationRef.value.validate();

      if (workoutFrequencyRef.value.hasError || workoutDurationRef.value.hasError) {
        alert(t('validation.fixErrors'));
        return false;
      }
      return true;
    };

    const navigateToNextStep = () => {
      if (!validateInput()) {
        return;
      }

      onboardingStore.setWorkoutData({
        frequency: workout_frequency.value,
        duration: workout_duration.value
      });

      router.push({ name: 'OnboardingStep6' });
    };

    return {
      t,
      workout_frequency,
      workout_duration,
      workoutFrequencyRef,
      workoutDurationRef,
      workoutFrequencyRules,
      workoutDurationRules,
      navigateToNextStep
    };
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

.button-container {
  position: fixed;
  bottom: 30px;
  width: 100%;
  display: flex;
  justify-content: center;
  left: 0;
}
</style>
