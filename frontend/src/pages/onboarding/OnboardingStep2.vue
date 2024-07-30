<template>
  <div class="size-container">
    <div class="welcome-container">
      <div class="content">
        <BackButtonText />
        <img src="~assets/Step2.svg" alt="Person form" class="person-image" />
        <h2 class="form-step">
          <span class="form-step-highlight">{{ $t('onboarding.onboardingStep2.step') }}</span>
          {{ $t('onboarding.onboardingStep2.title') }}
        </h2>
        <div class="form-group">
          <p>{{ $t('onboarding.onboardingStep2.fields.lastMenstruation') }}</p>
          <q-input filled v-model="last_menstruation" type="date" input-class="text-right input-text" class="q-mb-sm" />
        </div>
        <div class="form-group">
          <p>{{ $t('onboarding.onboardingStep2.fields.menstruationDuration') }}</p>
          <q-input filled v-model="menstruation_duration" type="number" input-class="text-right input-text" class="q-mb-sm" />
        </div>
        <div class="form-group">
          <p>{{ $t('onboarding.onboardingStep2.fields.cycleLength') }}</p>
          <q-input filled v-model="cycle_duration" type="number" input-class="text-right input-text" class="q-mb-sm" />
        </div>
        <div class="button-container">
          <StandardButton :label="$t('buttons.next')" @click="navigateToNextStep" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { api } from 'src/boot/axios';
import StandardButton from 'components/StandardButton.vue';
import BackButtonText from 'components/BackButtonText.vue';
import { useOnboardingStore } from 'src/stores/onboarding';

export default {
  components: {
    StandardButton,
    BackButtonText
  },
  setup() {
    const onboardingStore = useOnboardingStore();
    const router = useRouter();

    const last_menstruation = ref('');
    const menstruation_duration = ref(null);
    const cycle_duration = ref(null);

    const logLastMenstruation = async () => {
      try {
        await api.post('/cycles/log/', {
          date: last_menstruation.value,
          value: "1", 
          type: 1 
        });
      } catch (error) {
        console.error('Error logging last menstruation:', error);
        alert('Fehler beim Speichern der letzten Menstruation.');
      }
    };

    const navigateToNextStep = async () => {
      if (!last_menstruation.value.trim() || menstruation_duration.value === null || cycle_duration.value === null) {
        alert("Bitte füllen Sie alle Felder aus!");
        return;
      }

      try {
        await logLastMenstruation();

        onboardingStore.setMenstruationData({
          cycle_duration: cycle_duration.value,
          menstruation_duration: menstruation_duration.value,
          last_menstruation: last_menstruation.value
        });

        router.push({ name: 'OnboardingStep4' });
      } catch (error) {
        console.error('Failed to navigate to next step:', error);
        alert('Failed to navigate to next step');
      }
    };

    return {
      last_menstruation,
      menstruation_duration,
      cycle_duration,
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

.text-color {
  color: #50C1BA;
  font-size: 14px;
}

.input-text {
  text-align: right;
  font-size: 16px;
}

.button-container {
  position: fixed;
  bottom: 30px;
  width: 100%;
  display: flex;
  justify-content: center;
  left: 0;
}

.q-input .q-field__native {
  text-align: right;
}
</style>
