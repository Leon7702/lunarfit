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
import { ref, onMounted } from 'vue';
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
    const currentNoteId = ref(null);
    const router = useRouter();
    const authStore = useAuthStore();

    const goBack = () => {
      window.history.back();
    };

    const fetchCurrentNote = async () => {
      const today = new Date().toISOString().split('T')[0]; 

      try {
        await authStore.refreshAccessToken();

        const response = await api.get('/notes/', {
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${authStore.accessToken}`
          },
          params: {
            date: today
          }
        });

        if (response.data.results.length > 0) {
          const note = response.data.results[0];
          notes.value = note.content;
          currentNoteId.value = note.id;
        } else {
          notes.value = '';
          currentNoteId.value = null;
        }
      } catch (error) {
        console.error('Fehler beim Abrufen der Notiz', error);
        alert("Fehler beim Abrufen der Notiz!");
      }
    };

    const saveChanges = async () => {
      const requestBody = {
        date: new Date().toISOString().split('T')[0], 
        content: notes.value
      };

      try {
        await authStore.refreshAccessToken();

        if (notes.value === '' && currentNoteId.value) {
          await api.delete(`/notes/${currentNoteId.value}/`, {
            headers: {
              'Content-Type': 'application/json',
              'Authorization': `Bearer ${authStore.accessToken}`
            }
          });
          currentNoteId.value = null; 
        } else if (currentNoteId.value) {
          await api.patch(`/notes/${currentNoteId.value}/`, requestBody, {
            headers: {
              'Content-Type': 'application/json',
              'Authorization': `Bearer ${authStore.accessToken}`
            }
          });
        } else {
          const response = await api.post('/notes/', requestBody, {
            headers: {
              'Content-Type': 'application/json',
              'Authorization': `Bearer ${authStore.accessToken}`
            }
          });
          currentNoteId.value = response.data.id; 
        }
      } catch (error) {
        console.error('Fehler beim Speichern der Notiz', error);
        alert("Fehler beim Speichern der Notiz!");
      }
    };

    onMounted(() => {
      fetchCurrentNote();
    });

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
