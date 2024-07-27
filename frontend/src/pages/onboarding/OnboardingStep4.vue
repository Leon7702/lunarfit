<template>
  <div class="size-container">
    <div class="welcome-container">
      <div class="content">
        <BackButtonText />
        <img src="/src/assets/Step3.svg" alt="Person form" class="person-image" />
        <h2 class="form-step">
          <span class="form-step-highlight">{{ $t('onboarding.onboardingStep3.step') }}</span>
          {{ $t('onboarding.onboardingStep3.title') }}
        </h2>
        <div class="form-group">
          <p>{{ $t('onboarding.onboardingStep3.fields.hormonalContraception') }}</p>
          <RadioToggle v-model="hormonalContraception" />
        </div>
        <div class="form-group" v-if="hormonalContraception === 'ja'">
          <p>{{ $t('onboarding.onboardingStep3.fields.contraceptionMethod') }}</p>
          <q-select
            filled
            v-model="profile.contraceptive"
            :options="contraceptionOptions"
            input-class="text-right"
            class="q-mb-sm"
            emit-value
            map-options
          >
            <template v-slot:prepend>
              <div class="text-color">{{ $t('profile.contraception') }}</div>
            </template>
          </q-select>
        </div>
      </div>
      <div class="button-container">
        <StandardButton :label="$t('buttons.next')" @click="navigateToNextStep" />
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { api } from 'src/boot/axios';
import StandardButton from 'components/StandardButton.vue';
import BackButtonText from 'components/BackButtonText.vue';
import RadioToggle from 'components/RadioToggle.vue';
import { useAuthStore } from 'src/stores/auth';

export default {
  components: {
    StandardButton,
    BackButtonText,
    RadioToggle,
  },
  setup() {
    const router = useRouter();
    const authStore = useAuthStore();

    const profile = ref({
      contraceptive: null
    });

    const hormonalContraception = ref(null);

    const contraceptionOptions = [
      { label: 'Pille', value: 0 },
      { label: 'Hormonspirale', value: 1 },
      { label: 'Hormonimplantat', value: 2 },
      { label: 'Dreimonatsspritze', value: 3 },
      { label: 'Vaginalring', value: 4 },
      { label: 'Sonstiges', value: 5 }
    ];

    const saveProfile = async () => {
      try {
        await api.patch(`/users/profile/${authStore.userId}/`, profile.value);
        alert('Profile updated successfully');
      } catch (error) {
        console.error('Failed to update profile:', error);
        alert('Failed to update profile');
      }
    };

    const navigateToNextStep = async () => {
      try {
        await saveProfile();
        router.push({ name: 'OnboardingStep5' });
      } catch (error) {
        console.error('Failed to navigate to next step:', error);
        alert('Failed to navigate to next step');
      }
    };

    onMounted(() => {
      // Optionally, you can fetch existing profile data here if needed.
    });

    return {
      profile,
      hormonalContraception,
      contraceptionOptions,
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
