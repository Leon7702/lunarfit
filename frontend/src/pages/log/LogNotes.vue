<template>
  <div class="size-container">
    <div class="welcome-container">
      <div class="header">
        <q-btn flat dense round icon="arrow_back" @click="goBack" />
        <div class="title">{{ $t('logNotes.title') }}</div>
      </div>
      <div class="linie"></div>
      <div class="description">
        {{ $t('logNotes.description') }}
      </div>
      <div class="textarea">
        <InputTextArea v-model="notes" />
      </div>
      <div class="button-container">
        <StandardButton @click="saveChanges" :label="$t('buttons.save')" />
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';
import { api } from 'src/boot/axios';
import InputTextArea from 'components/InputTextArea.vue';
import StandardButton from 'components/StandardButton.vue';
import { useRouter } from 'vue-router';
import { useAuthStore } from 'src/stores/auth'; 

export default {
  components: {
    InputTextArea,
    StandardButton
  },
  setup() {
    const notes = ref('');
    const router = useRouter();
    const authStore = useAuthStore();

    const goBack = () => {
      window.history.back();
    };

    const saveChanges = async () => {
  console.log('Aktueller Wert von notes:', notes.value);

  if (!notes.value.trim()) {
    console.log("Notiz darf nicht leer sein!");
    alert("Notiz darf nicht leer sein!");
    return;
  }

  const requestBody = {
    date: new Date().toISOString().split('T')[0], // YYYY-MM-DD format
    content: notes.value
  };

  try {
    await authStore.refreshAccessToken(); // Refresh the token before making the request

    const response = await api.post('/notes/', requestBody, {
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${authStore.accessToken}`
      }
    });
    console.log('Notiz erfolgreich gespeichert', response.data);
    alert("Notiz erfolgreich gespeichert!");
    router.push('/log'); 
  } catch (error) {
    console.error('Fehler beim Speichern der Notiz', error);
    alert("Fehler beim Speichern der Notiz!");
  }
};


    return {
      notes,
      goBack,
      saveChanges
    };
  }
};
</script>

<style scoped>
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
  margin-top: 20px;
}

.title {
  font: 600 20px 'Inter', sans-serif;
  color: #000;
  text-align: center;
  flex-grow: 1;
  padding-right: 30px;
}

.description {
  text-align: left;
  width: 100%;
  margin-top: 30px;
  font-size: 16px;
  font-weight: 500;
  margin-bottom: 15px;
}

.textarea {
  width: 100%;
}

.button-container {
  position: fixed;
  bottom: 80px;
  width: 100%;
  display: flex;
  justify-content: center;
  left: 0;
}
</style>
