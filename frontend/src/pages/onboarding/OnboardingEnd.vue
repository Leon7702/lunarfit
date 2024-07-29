<template>
  <div class="size-container">
    <div class="welcome-container">
      <img src="~assets/Image_OnboardingEnd.svg" alt="Welcome Image" class="image" />
      <div class="welcome-text">
        <h1 class="title">{{ $t('onboarding.onboardingEnd.title') }}</h1>
        <p class="description">
          {{ $t('onboarding.onboardingEnd.description') }}
        </p>
      </div>
      <div class="button-container">
        <StandardButton :label="$t('buttons.next')" @click="completeOnboarding" />
      </div>
    </div>
  </div>
</template>

<script>
import StandardButton from 'components/StandardButton.vue';
import { useRouter } from 'vue-router';
import { api } from 'src/boot/axios';
import { useAuthStore } from 'src/stores/auth';
import { useOnboardingStore } from 'src/stores/onboarding';

export default {
  components: {
    StandardButton
  },
  setup() {
    const router = useRouter();
    const authStore = useAuthStore();
    const onboardingStore = useOnboardingStore();

    const completeOnboarding = async () => {
      const requestBody = {
        user: authStore.userId,
        workout_frequency: onboardingStore.workout_frequency,
        workout_duration: onboardingStore.workout_duration,
        workout_intensity: onboardingStore.workout_intensity,
        cycle_duration: onboardingStore.cycle_duration,
        menstruation_duration: onboardingStore.menstruation_duration
      };

      try {
        await authStore.refreshAccessToken();
        const response = await api.post('/users/onboarding/', requestBody, {
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${authStore.accessToken}`
          }
        });

        console.log('Onboarding successfully completed', response.data);
        alert('Onboarding erfolgreich abgeschlossen');
        router.push('/home');
      } catch (error) {
        console.error('Failed to complete onboarding:', error);
        alert('Fehler beim Abschließen des Onboardings');
      }
    };

    return {
      completeOnboarding
    };
  }
};
</script>


  <style scoped>

  .image {
    aspect-ratio: 1.64;
    object-fit: auto;
    object-position: center;
    margin-top: 20px;
    width: 100%;
  }

  .welcome-text {
    text-align: left;
  }

  .title {
    font: 600 24px/129% 'Inter', sans-serif;
    margin-top: 5vh;
  }

  .description {
    font: 16px/22px 'Inter', sans-serif;
    margin-top: 3vh;
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
