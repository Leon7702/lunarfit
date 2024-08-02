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
          <q-input
            ref="lastMenstruationRef"
            filled
            v-model="last_menstruation"
            type="date"
            input-class="text-left input-text"
            class="q-mb-sm"
            :rules="lastMenstruationRules"
          />
        </div>
        <div class="form-group">
          <div class="info-button">
            <p>{{ $t('onboarding.onboardingStep2.fields.menstruationDuration') }}</p>
            <q-btn class="q-pa-sm" fab flat round icon="info" color="grey-5" @click="openMenstruationLegendDialog" />
            <q-dialog v-model="menstruationLegend">
              <q-card>
                <q-card-section>
                  {{ $t('onboarding.onboardingStep2.menstruationLegendText') }}
                </q-card-section>
                <q-card-actions align="right">
                  <q-btn flat label="OK" v-close-popup />
                </q-card-actions>
              </q-card>
            </q-dialog>
          </div>
          <q-input
            ref="menstruationDurationRef"
            filled
            v-model="menstruation_duration"
            type="number"
            input-class="text-left input-text"
            class="q-mb-sm"
            :rules="menstruationDurationRules"
          />
        </div>
        <div class="form-group">
          <div class="info-button">
            <p>{{ $t('onboarding.onboardingStep2.fields.cycleLength') }}</p>
            <q-btn class="q-pa-sm" fab flat round icon="info" color="grey-5" @click="openCycleLegendDialog" />
            <q-dialog v-model="cycleLegend">
              <q-card>
                <q-card-section>
                  {{ $t('onboarding.onboardingStep2.cycleLegendText') }}
                </q-card-section>
                <q-card-actions align="right">
                  <q-btn flat label="OK" v-close-popup />
                </q-card-actions>
              </q-card>
            </q-dialog>
          </div>
          <q-input
            ref="cycleDurationRef"
            filled
            v-model="cycle_duration"
            type="number"
            input-class="text-left input-text"
            class="q-mb-sm"
            :rules="cycleDurationRules"
          />
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
import { useI18n } from 'vue-i18n';
import StandardButton from 'components/StandardButton.vue';
import BackButtonText from 'components/BackButtonText.vue';
import { useOnboardingStore } from 'src/stores/onboarding';

export default {
  components: {
    StandardButton,
    BackButtonText
  },
  setup() {
    const { t } = useI18n();
    const onboardingStore = useOnboardingStore();
    const router = useRouter();

    const last_menstruation = ref('');
    const menstruation_duration = ref(null);
    const cycle_duration = ref(null);

    const lastMenstruationRef = ref(null);
    const menstruationDurationRef = ref(null);
    const cycleDurationRef = ref(null);

    const menstruationLegend = ref(false);
    const cycleLegend = ref(false);

    const lastMenstruationRules = [
      val => !!val || t('validation.required'),
      val => new Date(val) <= new Date() || t('validation.lastMenstruationFuture'),
      val => new Date(val) >= new Date(new Date().setMonth(new Date().getMonth() - 3)) || t('validation.lastMenstruationTooOld')
    ];

    const menstruationDurationRules = [
      val => !!val || t('validation.required'),
      val => val > 0 || t('validation.positiveValue'),
      val => val >= 0 && val <= 20 || t('validation.realisticMensDuration'),
      val => Number.isInteger(Number(val)) || t('validation.realisticDay'),
    ];

    const cycleDurationRules = [
      val => !!val || t('validation.required'),
      val => val > 0 || t('validation.positiveValue'),
      val => val >= 20 && val <= 40 || t('validation.realisticCycleDuration'),
      val => Number.isInteger(Number(val)) || t('validation.realisticDay'),
    ];

    const logLastMenstruation = async () => {
      try {
        await api.post('/cycles/log/', {
          date: last_menstruation.value,
          value: "1",
          type: 1
        });
      } catch (error) {
        console.error('Error logging last menstruation:', error);
        alert(t('logging.lastMenstruationError'));
      }
    };

    const navigateToNextStep = async () => {
      lastMenstruationRef.value.validate();
      menstruationDurationRef.value.validate();
      cycleDurationRef.value.validate();

      if (
        lastMenstruationRef.value.hasError ||
        menstruationDurationRef.value.hasError ||
        cycleDurationRef.value.hasError
      ) {
        alert(t('validation.fixErrors'));
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
        alert(t('navigation.failure'));
      }
    };

    const openMenstruationLegendDialog = () => {
      menstruationLegend.value = true;
    };

    const openCycleLegendDialog = () => {
      cycleLegend.value = true;
    };

    return {
      last_menstruation,
      menstruation_duration,
      cycle_duration,
      lastMenstruationRef,
      menstruationDurationRef,
      cycleDurationRef,
      lastMenstruationRules,
      menstruationDurationRules,
      cycleDurationRules,
      navigateToNextStep,
      menstruationLegend,
      cycleLegend,
      openMenstruationLegendDialog,
      openCycleLegendDialog
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

.text-color {
  color: #50C1BA;
  font-size: 14px;
}

.input-text {
  text-align: right;
  font-size: 16px;
}

.info-button {
  display: flex;
  /* justify-content: space-between; */
  align-items: center;
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
