<template>
  <div class="size-container">
    <div class="welcome-container">
      <div class="header">
        <q-btn flat dense round icon="arrow_back" @click="goBack" />
        <div class="title">{{ $t('logCycle.sex.title') }}</div>
      </div>
      <div class="linie"></div>
      <div class="description">
        {{ $t('logCycle.sex.description') }}
      </div>
      <div class="form-group">
        <q-select
          filled
          v-model="selectedOption"
          :options="translatedOptions"
          input-class="text-right"
          class="q-mb-sm"
          emit-value
          map-options
        >
          <template v-slot:prepend></template>
        </q-select>
      </div>
      <div class="button-container">
        <StandardButton :label="$t('buttons.save')" @click="saveCycleData" />
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed } from 'vue';
import { useRouter } from 'vue-router';
import { useI18n } from 'vue-i18n';
import { api } from 'src/boot/axios';
import StandardButton from 'components/StandardButton.vue';
import { useAuthStore } from 'src/stores/auth';

export default {
  components: {
    StandardButton
  },
  setup() {
    const { t } = useI18n();
    const router = useRouter();
    const authStore = useAuthStore();

    const selectedOption = ref(null);

    const options = [
      { key: 'keinSex', value: 0 },
      { key: 'geschuetzterSex', value: 1 },
      { key: 'ungeschuetzterSex', value: 2 },
      { key: 'lustAufSex', value: 3 },
      { key: 'masturbation', value: 4 }
    ];

    const translatedOptions = computed(() => {
      return options.map(option => ({
        label: t(`logCycle.sex.options.${option.key}`),
        value: option.value
      }));
    });

    const goBack = () => {
      window.history.back();
    };

    const saveCycleData = async () => {
      if (selectedOption.value === null) {
        alert("Bitte wählen Sie eine Option aus!");
        return;
      }

      const requestBody = {
        date: new Date().toISOString().split('T')[0], 
        type: 5,
        value: selectedOption.value
      };

      try {
        await authStore.refreshAccessToken(); 

        await api.post('/cycles/log/', requestBody, {
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${authStore.accessToken}`
          }
        });

        alert("Daten erfolgreich gespeichert!");
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

    return {
      selectedOption,
      translatedOptions,
      goBack,
      saveCycleData
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
    margin-bottom: 10px;
  }
  .form-group {
    width: 100%;
  }
  
  .form-group p {
    margin: 0; 
    font-size: 16px;
    margin-left: 7px;
    margin-right: 7px;
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
  