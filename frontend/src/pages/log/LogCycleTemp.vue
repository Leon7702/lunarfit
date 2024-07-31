<template>
  <div class="size-container">
    <div class="welcome-container">
      <div class="header">
        <q-btn flat dense round icon="arrow_back" @click="goBack" />
        <div class="title">{{ $t('logCycle.temperature.title') }}</div>
      </div>
      <div class="linie"></div>
      <div class="description">
        {{ $t('logCycle.temperature.description') }}
      </div>
      <div class="form-group">
        <q-input
          filled
          v-model="temperature"
          type="number"
          input-class="text-left input-text"
          class="q-mb-sm"
          clearable
          @clear="deleteCurrentEntry"
        />
      </div>
      <div class="description-two">
        {{ $t('logCycle.temperature.descriptionTwo') }}
      </div>
      <div class="form-group">
        <CheckboxInput v-model="storfaktoren" />
      </div>
      <div class="small-description">
        {{ $t('logCycle.temperature.smallDescription') }}
      </div>
      <div class="button-container">
        <StandardButton :label="$t('buttons.save')" @click="saveCycleData" />
      </div>
    </div>
  </div>
</template>

<script>
import CheckboxInput from 'components/CheckboxInput.vue';
import StandardButton from 'components/StandardButton.vue';
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { useI18n } from 'vue-i18n';
import { api } from 'src/boot/axios';
import { useAuthStore } from 'src/stores/auth';

export default {
  components: {
    CheckboxInput,
    StandardButton
  },
  setup() {
    const { t } = useI18n();
    const router = useRouter();
    const authStore = useAuthStore();

    const temperature = ref(null);
    const storfaktoren = ref(false);
    const currentEntryId = ref(null);

    const goBack = () => {
      window.history.back();
    };

    const fetchCurrentEntry = async () => {
      const today = new Date().toISOString().split('T')[0];
      try {
        await authStore.refreshAccessToken();
        const response = await api.get('/cycles/log/', {
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${authStore.accessToken}`
          },
          params: {
            type: 2,
            date: today
          }
        });

        if (response.data.results.length > 0) {
          const entry = response.data.results[0];
          currentEntryId.value = entry.id;

          const entryResponse = await api.get(`/cycles/log/${currentEntryId.value}/`, {
            headers: {
              'Content-Type': 'application/json',
              'Authorization': `Bearer ${authStore.accessToken}`
            }
          });

          temperature.value = parseFloat(entryResponse.data.value);
        } else {
          currentEntryId.value = null;
          temperature.value = null;
        }
      } catch (error) {
        console.error('Fehler beim Abrufen der Zyklusdaten', error);
      }
    };

    const deleteCurrentEntry = async () => {
      if (currentEntryId.value === null) {
        return;
      }

      try {
        await authStore.refreshAccessToken();
        await api.delete(`/cycles/log/${currentEntryId.value}/`, {
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${authStore.accessToken}`
          }
        });

        currentEntryId.value = null;
        temperature.value = null;
      } catch (error) {
        console.error('Fehler beim Löschen des Zyklusdatensatzes', error);
        alert('Fehler beim Löschen des Zyklusdatensatzes.');
      }
    };

    const saveCycleData = async () => {
      if (temperature.value === null) {
        return;
      }

      const requestBody = {
        date: new Date().toISOString().split('T')[0],
        type: 2,
        value: temperature.value
      };

      try {
        await authStore.refreshAccessToken();

        if (currentEntryId.value) {
          await api.patch(`/cycles/log/${currentEntryId.value}/`, requestBody, {
            headers: {
              'Content-Type': 'application/json',
              'Authorization': `Bearer ${authStore.accessToken}`
            }
          });
        } else {
          const response = await api.post('/cycles/log/', requestBody, {
            headers: {
              'Content-Type': 'application/json',
              'Authorization': `Bearer ${authStore.accessToken}`
            }
          });
          currentEntryId.value = response.data.id;
        }

       
      } catch (error) {
        console.error('Fehler beim Speichern der Zyklusdaten', error);

        if (error.response) {
          if (error.response.status === 400) {
            alert('Fehlerhafte Anfrage. Bitte überprüfen Sie Ihre Eingaben.');
          } else if (error.response.status === 401) {
            alert('Nicht autorisiert. Bitte melden Sie sich erneut an.');
          } else {
            alert('Fehler beim Speichern der Zyklusdaten.');
          }
        } else if (error.request) {
          alert('Keine Antwort vom Server. Bitte überprüfen Sie Ihre Internetverbindung.');
        } else {
          alert('Ein unbekannter Fehler ist aufgetreten.');
        }
      }
    };

    onMounted(() => {
      fetchCurrentEntry();
    });

    return {
      temperature,
      storfaktoren,
      goBack,
      saveCycleData,
      deleteCurrentEntry
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
  margin-top: 30px;
  text-align: left;
  width: 100%;
  font-size: 16px;
  font-weight: 500;
  margin-bottom: 10px;
}

.description-two {
  text-align: left;
  width: 100%;
  margin-top: 5px;
  font-size: 16px;
  font-weight: 500;
  margin-bottom: 10px;
}

.form-group {
  width: 100%;
}

.small-description {
  font: 12px/16px 'Inter', sans-serif;
  margin-top: 15px;
}
.button-container {
  position: fixed;
  bottom: 80px;  
  width: 100%;
  display: flex;
  justify-content: center;
  left: 0;
}

.q-mb-sm {
  margin-bottom: 30px;
}
</style>
