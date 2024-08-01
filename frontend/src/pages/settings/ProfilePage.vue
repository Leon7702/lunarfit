<template>
  <div class="size-container">
    <div class="welcome-container">
      <div class="header">
        <q-btn flat dense round icon="arrow_back" to="/settings" />
        <div class="title">{{ $t('profile.title') }}</div>
      </div>
      <div class="linie"></div>

      <q-list>
        <q-input
          ref="firstNameRef"
          filled
          v-model="profile.first_name"
          type="text"
          input-class="text-right"
          class="q-pt-lg q-mb-sm"
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
        <q-select
          ref="contraceptiveRef"
          clearable
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
      </q-list>
      <div class="button-container">
        <StandardButton :label="$t('save')" @click="saveProfile"/>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, watch, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { useI18n } from 'vue-i18n';
import { api } from 'src/boot/axios';
import { useAuthStore } from 'src/stores/auth';
import StandardButton from 'components/StandardButton.vue';

export default {
  name: 'ProfilePage',
  components: {
    StandardButton
  },
  setup() {
    const { t } = useI18n();
    const authStore = useAuthStore();
    const router = useRouter();

    const profile = ref({
      user: null,
      first_name: '',
      last_name: '',
      birthdate: null,
      body_height: null,
      body_weight: null,
      contraceptive: null
    });

    const firstNameRef = ref(null);
    const lastNameRef = ref(null);
    const birthdateRef = ref(null);
    const heightRef = ref(null);
    const weightRef = ref(null);
    const contraceptiveRef = ref(null);

    const nameRules = [
      val => !!val || t('validation.required'),
      val => /^[\p{L}\p{M}]+(?:[-\s][\p{L}\p{M}]+)*$/u.test(val) || t('validation.onlyLetters')
    ];

    const birthdateRules = [
      val => !!val || t('validation.requiredBirthdate'),
      val => new Date(val) <= new Date() || t('validation.birthdateFuture'),
      val => new Date(val).getFullYear() > new Date().getFullYear() - 120 || t('validation.birthdateUnrealistic')
    ];

    const heightRules = [
      val => !!val || t('validation.requiredHeight'),
      val => val > 0 || t('validation.positiveHeight'),
      val => val >= 100 && val <= 250 || t('validation.realisticHeight')
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
      firstNameRef.value.validate();
      lastNameRef.value.validate();
      birthdateRef.value.validate();
      heightRef.value.validate();
      weightRef.value.validate();
      contraceptiveRef.value.validate();

      if (
        firstNameRef.value.hasError ||
        lastNameRef.value.hasError ||
        birthdateRef.value.hasError ||
        heightRef.value.hasError ||
        weightRef.value.hasError ||
        contraceptiveRef.value.hasError
      ) {
        alert(t('validation.fixErrors'));
        return;
      }

      try {
        await api.patch(`/users/profile/${authStore.userId}/`, profile.value);
        alert(t('profile.updateSuccess'));
        router.push({ name: 'Settings' });
      } catch (error) {
        console.error('Failed to update profile:', error);
        alert(t('profile.updateFailure'));
      }
    };

    watch(() => authStore.userId, (newUserId) => {
      if (newUserId) {
        fetchProfile();
      }
    });

    onMounted(() => {
      fetchProfile();
    });

    return {
      t,
      profile,
      firstNameRef,
      lastNameRef,
      birthdateRef,
      heightRef,
      weightRef,
      contraceptiveRef,
      nameRules,
      birthdateRules,
      heightRules,
      weightRules,
      saveProfile
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
.welcome-container {
  display: flex;
  flex-direction: column;
  margin: auto;
}

.linie {
  height: 1px;
  background-color: rgba(0, 0, 0, 0.1);
  margin-top: 10px;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  padding: 10px 0;
}

.title {
  font: 600 20px 'Inter', sans-serif;
  color: #000;
  text-align: center;
  flex-grow: 1;
  padding-right: 30px;
}

.text-color {
  color: #50C1BA;
  font-size: 14px;
}

.button-container {
  display: flex;
  justify-content: center;
}
</style>
