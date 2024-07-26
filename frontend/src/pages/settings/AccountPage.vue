<template>
  <div class="size-container">
    <div class="welcome-container">
      <div class="header">
        <q-btn flat dense round icon="arrow_back" to="/settings" />
        <div class="title">{{ $t('account.title') }}</div>
      </div>
      <div class="linie"></div>

      <q-list>
        <q-item-label header class="q-pt-xl q-pb-xs text-color">{{ $t('account.email') }}</q-item-label>
        <q-item class="q-mb-xs grey-background">
          <q-item-section>
            <q-item-label>{{ email }}</q-item-label>
          </q-item-section>
        </q-item>
        <q-item-label header class="q-pt-md q-pb-xs text-color">{{ $t('account.password') }}</q-item-label>
        <q-item clickable v-ripple class="q-mb-xs grey-background">
          <q-item-section>
            <q-item-label>{{ $t('account.change-password') }}</q-item-label>
          </q-item-section>
          <q-item-section side>
            <img src="../../assets/arrow-right.svg" />
          </q-item-section>
        </q-item>
      </q-list>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import api from 'src/services/axios';
import { useAuthStore } from 'src/stores/auth';

export default {
  name: 'AccountPage',
  setup() {
    const email = ref('');
    const authStore = useAuthStore();

    const getEmail = async () => {
      try {
        const response = await api.get(`/api/users/${authStore.userId}/`);
        email.value = response.data.email;
      } catch (error) {
        console.error('Failed to fetch email:', error);
      }
    };

    onMounted(() => {
      getEmail();
    });

    return {
      email,
      getEmail
    };
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

.grey-background {
  background-color: #F8F8F8;
  padding: 12px;
}

.text-color {
  color: #50C1BA;
}
</style>
