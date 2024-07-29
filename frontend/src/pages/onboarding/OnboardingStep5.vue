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
            filled
            v-model="workout_frequency"
            type="number"
            input-class="text-right input-text"
            class="q-mb-sm"
          />
        </div>
        <div class="form-group">
          <p>{{ $t('onboarding.onboardingStep4.fields.trainingDuration') }}</p>
          <q-input
            filled
            v-model="workout_duration"
            type="number"
            input-class="text-right input-text"
            class="q-mb-sm"
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
import { useOnboardingStore } from 'src/stores/onboarding';
import StandardButton from 'components/StandardButton.vue';
import BackButtonText from 'components/BackButtonText.vue';

export default {
  components: {
    StandardButton,
    BackButtonText
  },
  setup() {
    const onboardingStore = useOnboardingStore();
    const router = useRouter();

    const workout_frequency = ref(null);
    const workout_duration = ref(null);

    const navigateToNextStep = () => {
      if (workout_frequency.value === null || workout_duration.value === null) {
        alert("Bitte füllen Sie alle Felder aus!");
        return;
      }

      onboardingStore.setWorkoutData({
        frequency: workout_frequency.value,
        duration: workout_duration.value
      });

      router.push({ name: 'OnboardingStep6' });
    };

    return {
      workout_frequency,
      workout_duration,
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
</style>
