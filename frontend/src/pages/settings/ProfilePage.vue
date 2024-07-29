<template>
  <div class="size-container">
    <div class="welcome-container">
      <div class="header">
        <q-btn flat dense round icon="arrow_back" to="/settings" />
        <div class="title">{{ $t('profile.title') }}</div>
      </div>
      <div class="linie"></div>

      <q-list>
        <q-input filled v-model="profile.first_name" type="text" input-class="text-right" class="q-pt-xl q-mb-sm">
          <template v-slot:prepend>
            <div class="text-color">{{ $t('profile.firstName') }}</div>
          </template>
        </q-input>
        <q-input filled v-model="profile.last_name" type="text" input-class="text-right" class="q-mb-sm">
          <template v-slot:prepend>
            <div class="text-color">{{ $t('profile.lastName') }}</div>
          </template>
        </q-input>
        <q-input filled v-model="profile.birthdate" type="date" input-class="text-right" class="q-mb-sm">
          <template v-slot:prepend>
            <div class="text-color">{{ $t('profile.birthdate') }}</div>
          </template>
        </q-input>
        <q-input filled v-model="profile.body_height" type="number" input-class="text-right" class="q-mb-sm">
          <template v-slot:prepend>
            <div class="text-color">{{ $t('profile.height') }}</div>
          </template>
        </q-input>
        <q-input filled v-model="profile.body_weight" type="number" input-class="text-right" class="q-mb-sm">
          <template v-slot:prepend>
            <div class="text-color">{{ $t('profile.weight') }}</div>
          </template>
        </q-input>
        <q-select clearable filled v-model="profile.contraceptive" :options="contraceptionOptions"
          input-class="text-right" class="q-mb-sm" emit-value map-options>
          <template v-slot:prepend>
            <div class="text-color">{{ $t('profile.contraception') }}</div>
          </template>
        </q-select>
      </q-list>
      <div class="button-container">
        <StandardButton :label="$t('save')" @click="saveProfile" />
      </div>
    </div>
  </div>
</template>

<script>
import { ref, watch, onMounted } from 'vue';
import { api } from 'src/boot/axios';
import { useAuthStore } from 'src/stores/auth';
import StandardButton from 'components/StandardButton.vue';

export default {
  name: 'ProfilePage',
  components: {
    StandardButton
  },
  setup() {
    const authStore = useAuthStore();

    const profile = ref({
      user: null,
      // onboarding_finished: false,
      first_name: '',
      last_name: '',
      birthdate: null,
      body_height: null,
      body_weight: null,
      // language: 'de',
      contraceptive: null
    });

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
        alert('Profile updated successfully');
      } catch (error) {
        console.error('Failed to update profile:', error);
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
      profile,
      fetchProfile,
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
  padding: 20px;
}
</style>
