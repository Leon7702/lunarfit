<template>
  <div class="size-container">
  <div class="welcome-container">
    <div class="header">
      <q-btn flat dense round icon="arrow_back" @click="goBack" />
      <div class="title">{{ $t('profile.title') }}</div>
    </div>
    <div class="linie"></div>

    <q-list>
      <!-- TODO: change prefix (v-slot: prepend?) -->
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
      <q-select filled v-model="profile.contraceptive" :options="contraceptionOptions" input-class="text-right"
        class="q-mb-sm">
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
import { ref, onMounted } from 'vue';
import axios from 'axios';
import StandardButton from 'components/StandardButton.vue';

export default {
  // i18n handling
  name: 'ProfilePage',
  components: {
    StandardButton
  },
  setup() {
    //TODO: get data from backend --> replace these with dynamic data fetching logic
    const profile = ref({
      first_name: '',
      last_name: '',
      birthdate: '',
      body_height: null,
      body_weight: null,
      contraceptive: null
    });

    const fetchProfile = async () => {
      try {
        const response = await axios.get('http://localhost:3000/users/');
        profile.value = response.data;
      } catch (error) {
        console.error('Failed to fetch profile:', error);
      }
    };

    const saveProfile = async () => {
      try {
        await axios.patch('http://localhost:3000/users/', profile.value);
        alert('Profile updated successfully');
      } catch (error) {
        console.error('Failed to update profile:', error);
      }
    };

    onMounted(() => {
      fetchProfile();
    });

    return {
      profile,
      fetchProfile,
      saveProfile
    };
  },
  // refactored:
  computed: {
    contraceptionOptions() {
      return Array.from({ length: 6 }, (_, i) =>
        this.$t(`profile.contraceptionOptions[${i}]`)
      );
    },
  },
  methods: {
    goBack() {
      window.history.back();
    }
  }
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
  margin-top: 60px;
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

