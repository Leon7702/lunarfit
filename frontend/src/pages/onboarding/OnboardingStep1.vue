<template>
  <div class="size-container">
    <div class="welcome-container">
      <div class="content">
        <BackButtonText />
        <img src="~assets/Step1.svg" alt="Person form" class="person-image" />
        <h2 class="form-step">
          <span class="form-step-highlight">{{ $t('onboarding.onboardingStep1.step') }}</span>
          {{ $t('onboarding.onboardingStep1.title') }}
        </h2>
        <q-list class="form-list">
          <q-input
            ref="firstNameRef"
            filled
            v-model="profile.first_name"
            type="text"
            input-class="text-right"
            class="q-mb-sm"
            :rules="nameRules"
          >
            <template v-slot:prepend>
              <div class="text-color">{{ $t('profile.firstName') }}</div>
            </template>
          </q-input>
          <q-input
            ref="lastNameRef"
            filled
            v-model="profile.last_name"
            type="text"
            input-class="text-right"
            class="q-mb-sm"
            :rules="nameRules"
          >
            <template v-slot:prepend>
              <div class="text-color">{{ $t('profile.lastName') }}</div>
            </template>
          </q-input>
          <q-input
            ref="birthdateRef"
            filled
            v-model="profile.birthdate"
            type="date"
            input-class="text-right"
            class="q-mb-sm"
            :rules="birthdateRules"
          >
            <template v-slot:prepend>
              <div class="text-color">{{ $t('profile.birthdate') }}</div>
            </template>
          </q-input>
          <q-input
            ref="heightRef"
            filled
            v-model="profile.body_height"
            type="number"
            input-class="text-right"
            class="q-mb-sm"
            :rules="heightRules"
          >
            <template v-slot:prepend>
              <div class="text-color">{{ $t('profile.height') }}</div>
            </template>
          </q-input>
          <q-input
            ref="weightRef"
            filled
            v-model="profile.body_weight"
            type="number"
            input-class="text-right"
            class="q-mb-sm"
            :rules="weightRules"
          >
            <template v-slot:prepend>
              <div class="text-color">{{ $t('profile.weight') }}</div>
            </template>
          </q-input>
        </q-list>
        <div class="button-container">
          <StandardButton :label="$t('buttons.next')" @click="navigateToNextStep" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { api } from 'src/boot/axios';
import { useI18n } from 'vue-i18n';
import { useAuthStore } from 'src/stores/auth';
import StandardButton from 'components/StandardButton.vue';
import BackButtonText from 'components/BackButtonText.vue';

export default {
  components: {
    StandardButton,
    BackButtonText
  },
  setup() {
    const authStore = useAuthStore();
    const router = useRouter();
    const { t } = useI18n();

    const profile = ref({
      first_name: '',
      last_name: '',
      birthdate: '',
      body_height: null,
      body_weight: null,
    });

    const firstNameRef = ref(null);
    const lastNameRef = ref(null);
    const birthdateRef = ref(null);
    const heightRef = ref(null);
    const weightRef = ref(null);

    const nameRules = [
      val => !!val || t('validation.required'),
      val => /^[\p{L}\p{M}]+(?:[-\s][\p{L}\p{M}]+)*$/u.test(val) || t('validation.onlyLetters')
    ];

    const birthdateRules = [
      // val => !!val || t('validation.requiredBirthdate'),
      val => new Date(val) <= new Date() || t('validation.birthdateFuture'),
      val => new Date(val).getFullYear() > new Date().getFullYear() - 120 || t('validation.birthdateUnrealistic')
    ];

    const heightRules = [
      val => !!val || t('validation.requiredHeight'),
      val => val > 0 || t('validation.positiveHeight'),
      val => val >= 100 && val <= 250|| t('validation.realisticHeight')
    ];

    const weightRules = [
      val => !!val || t('validation.requiredWeight'),
      val => val > 0 || t('validation.positiveWeight'),
      val => val >= 20 && val <= 200 || t('validation.realisticWeight')
    ];

    const fetchProfile = async () => {
      try {
        const response = await api.get(`/users/profile/${authStore.userId}/`);
        profile.value = response.data;
      } catch (error) {
        console.error('Failed to fetch profile:', error);
      }
    };

    const saveProfile = async () => {
      try {
        await api.patch(`/users/profile/${authStore.userId}/`, profile.value);
        // alert(t('profile.updateSuccess'));
      } catch (error) {
        console.error('Failed to update profile:', error);
        alert(t('profile.updateFailure'));
      }
    };

    const navigateToNextStep = async () => {
      firstNameRef.value.validate();
      lastNameRef.value.validate();
      birthdateRef.value.validate();
      heightRef.value.validate();
      weightRef.value.validate();

      if (
        firstNameRef.value.hasError ||
        lastNameRef.value.hasError ||
        birthdateRef.value.hasError ||
        heightRef.value.hasError ||
        weightRef.value.hasError
      ) {
        alert(t('validation.fixErrors'));
        return;
      }

      try {
        await saveProfile();
        router.push({ name: 'OnboardingStep2' });
      } catch (error) {
        console.error('Failed to navigate to next step:', error);
        alert(t('navigation.failure'));
      }
    };

    onMounted(() => {
      fetchProfile();
    });

    return {
      profile,
      navigateToNextStep,
      firstNameRef,
      lastNameRef,
      birthdateRef,
      heightRef,
      weightRef,
      nameRules,
      birthdateRules,
      heightRules,
      weightRules
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

.button-container {
  position: fixed;
  bottom: 30px;
  width: 100%;
  display: flex;
  justify-content: center;
  left: 0;
}

.form-list .q-input {
  display: flex;
  flex-direction: column;
}

.text-color {
  font-size: 12px;
  color: #50C1BA;
  margin-bottom: 4px;
}

.label-text {
  color: #50C1BA;
}
</style>
