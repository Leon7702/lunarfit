<template>
  <div class="size-container">
    <div class="welcome-container">
      <div class="content">
        <BackButtonText />
        <img src="~assets/Step3.svg" alt="Person form" class="person-image" />
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
            clearable
            filled
            v-model="profile.contraceptive"
            :options="contraceptionOptions"
            input-class="text-left"
            class="q-mb-sm"
            emit-value
            map-options
          >
            <template v-slot:prepend></template>
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
import { ref, watch, onMounted } from 'vue';
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

    const saveProfile = async () => {
      try {
        await api.patch(`/users/profile/${authStore.userId}/`, profile.value);
        // alert('Profile updated successfully');
      } catch (error) {
        console.error('Failed to update profile:', error);
        alert('Failed to update profile');
      }
    };

    const fetchContraception = async () => {
      try {
        const response = await api.get(`/users/profile/${authStore.userId}/`);
        profile.value = response.data;
      } catch (error) {
        console.error('Failed to fetch contraception:', error);
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

    watch(() => authStore.userId, (newUserId) => {
      if (newUserId) {
        fetchContraception();
      }
    });

    onMounted(() => {
      fetchContraception();
    });

    return {
      profile,
      hormonalContraception,
      saveProfile,
      navigateToNextStep,
      fetchContraception
    };
  },
  computed: {
    contraceptionOptions() {
      return [
        { label: this.$t('profile.contraceptionOptions[0]'), value: 0 },
        { label: this.$t('profile.contraceptionOptions[1]'), value: 1 },
        { label: this.$t('profile.contraceptionOptions[2]'), value: 2 },
        { label: this.$t('profile.contraceptionOptions[3]'), value: 3 },
        { label: this.$t('profile.contraceptionOptions[4]'), value: 4 },
        // { label: this.$t('profile.contraceptionOptions[5]'), value: 5 }
      ];
    },
  },
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
