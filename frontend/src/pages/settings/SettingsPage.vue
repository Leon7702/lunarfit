<template>
  <div class="welcome-container">
    <div class="header">
      <q-btn flat dense round icon="arrow_back" @click="goBack" />
      <div class="title">Einstellungen</div>
    </div>
    <div class="linie"></div>

    <div class="q-md" style="max-width: 100%">
      <q-list>
      <q-item-label header class="q-pt-xl q-pb-xs">PROFIL</q-item-label>
      <q-item clickable v-ripple class="q-mb-xs grey-background" @click="navigateToProfile">
        <q-item-section side>
            <img src="../../assets/ProfileIcon.svg">
        </q-item-section>
        <q-item-section>
          <q-item-label>Persönliche Informationen</q-item-label>
        </q-item-section>
        <q-item-section side>
            <img src="../../assets/arrow-right.svg">
        </q-item-section>
      </q-item>

      <q-item clickable v-ripple class="grey-background" @click="navigateToAccount">
        <q-item-section side>
            <img src="../../assets/SettingsIcon.svg">
        </q-item-section>
        <q-item-section>
          <q-item-label>Account Einstellungen</q-item-label>
        </q-item-section>
        <q-item-section side>
            <img src="../../assets/arrow-right.svg">
        </q-item-section>
      </q-item>
    </q-list>

    <q-list>
      <q-item-label header class="q-pt-lg q-pb-xs">MITTEILUNGEN</q-item-label>

      <q-item tag="label" v-ripple class="grey-background2">
        <q-item-section side>
            <img src="../../assets/NotificationIcon.svg">
        </q-item-section>
        <q-item-section>
          <q-item-label>Mitteilungen</q-item-label>
        </q-item-section>
        <q-item-section side>
          <q-toggle color="teal" v-model="notif1" />
        </q-item-section>
      </q-item>
    </q-list>

      <q-list>
      <q-item-label header class="q-pt-lg q-pb-xs">EINSTELLUNGEN</q-item-label>
      <q-item clickable v-ripple class="q-mb-xs grey-background" @click="navigateToLanguage">
        <q-item-section side>
            <img src="../../assets/GlobeIcon.svg">
        </q-item-section>
        <q-item-section>
          <q-item-label>Sprache</q-item-label>
        </q-item-section>
        <q-item-section side>
            <img src="../../assets/arrow-right.svg">
        </q-item-section>
      </q-item>

      <q-item clickable v-ripple class="grey-background">
        <q-item-section side>
            <img src="../../assets/LogoutIcon.svg">
        </q-item-section>
        <q-item-section>
          <q-item-label>Logout</q-item-label>
        </q-item-section>
        <q-item-section side>
            <img src="../../assets/arrow-right.svg">
        </q-item-section>
      </q-item>
    </q-list>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';
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
