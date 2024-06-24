<template>
  <div class="welcome-container">
    <div class="header">
      <q-btn flat dense round icon="arrow_back" @click="goBack" />
      <div class="title">{{ $t('settings.title') }}</div>
    </div>
    <div class="linie"></div>

    <div class="q-md" style="max-width: 100%">
      <q-list>
        <q-item-label header class="q-pt-xl q-pb-xs">{{ $t('settings.profileCaps') }}</q-item-label>
        <q-item clickable v-ripple class="q-mb-xs grey-background" @click="navigateToProfile">
          <q-item-section side>
            <img src="/src/assets/ProfileIcon.svg">
          </q-item-section>
          <q-item-section>
            <q-item-label>{{ $t('settings.personal-info') }}</q-item-label>
          </q-item-section>
          <q-item-section side>
            <img src="/src/assets/arrow-right.svg">
          </q-item-section>
        </q-item>

        <q-item clickable v-ripple class="grey-background" @click="navigateToAccount">
          <q-item-section side>
            <img src="/src/assets/SettingsIcon.svg">
          </q-item-section>
          <q-item-section>
            <q-item-label>{{ $t('settings.account-settings') }}</q-item-label>
          </q-item-section>
          <q-item-section side>
            <img src="/src/assets/arrow-right.svg">
          </q-item-section>
        </q-item>
      </q-list>

      <q-list>
        <q-item-label header class="q-pt-lg q-pb-xs">{{ $t('settings.notificationsCaps') }}</q-item-label>

        <q-item tag="label" v-ripple class="grey-background2">
          <q-item-section side>
            <img src="/src/assets/NotificationIcon.svg">
          </q-item-section>
          <q-item-section>
            <q-item-label>{{ $t('settings.notifications') }}</q-item-label>
          </q-item-section>
          <q-item-section side>
            <q-toggle color="teal" v-model="notif1" />
          </q-item-section>
        </q-item>
      </q-list>

      <q-list>
        <q-item-label header class="q-pt-lg q-pb-xs">{{ $t('settings.settingsCaps') }}</q-item-label>
        <q-item clickable v-ripple class="q-mb-xs grey-background" @click="navigateToLanguage">
          <q-item-section side>
            <img src="/src/assets/GlobeIcon.svg">
          </q-item-section>
          <q-item-section>
            <q-item-label>{{ $t('settings.language') }}</q-item-label>
          </q-item-section>
          <q-item-section side>
            <img src="/src/assets/arrow-right.svg">
          </q-item-section>
        </q-item>

        <q-item clickable v-ripple class="grey-background" @click="logout">
          <q-item-section side>
            <img src="/src/assets/LogoutIcon.svg">
          </q-item-section>
          <q-item-section>
            <q-item-label>{{ $t('settings.logout') }}</q-item-label>
          </q-item-section>
          <q-item-section side>
            <img src="/src/assets/arrow-right.svg">
          </q-item-section>
        </q-item>
      </q-list>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';
import { useAuthStore } from 'src/stores/auth.js';
export default {

  components: {

  },
  data() {
    return {
      check1: ref(true),
      notif1: ref(true),
    }
  },
  methods: {
    goBack() {
      window.history.back();
    },
    navigateToProfile() {
      this.$router.push({ name: 'Profile' });
    },
    navigateToAccount() {
      this.$router.push({ name: 'Account' });
    },
    navigateToLanguage() {
      this.$router.push({ name: 'Language' });
    },
    logout() {
      const authStore = useAuthStore();
      authStore.logout();
      this.$router.push('/login');
    }
  }
};
</script>

<style scoped>
.welcome-container {
  display: flex;
  flex-direction: column;
  /* height: 100vh; */
  margin: auto;
}

.linie {
  height: 1px;
  background-color: rgba(0, 0, 0, 0.1);
  width: 120%;
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

.grey-background {
  background-color: #F8F8F8;
  padding: 12px;
}

.grey-background2 {
  background-color: #F8F8F8;
}
</style>
