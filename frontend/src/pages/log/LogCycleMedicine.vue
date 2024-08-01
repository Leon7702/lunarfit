<template>
  <div class="size-container">
    <div class="welcome-container">
      <div class="header">
        <q-btn flat dense round icon="arrow_back" @click="goBack" />
        <div class="title">{{ $t('logCycle.medicine.title') }}</div>
      </div>
      <div class="linie"></div>
      <div class="description">
        {{ $t('logCycle.medicine.description') }}
      </div>
      <div class="form-group">
        <q-select
          filled
          v-model="selectedMedicine"
          :options="translatedMedicineOptions"
          input-class="text-right"
          class="q-mb-sm"
          emit-value
          map-options
        >
          <template v-slot:prepend></template>
        </q-select>
      </div>
      <div class="small-description">
        {{ $t('logCycle.medicine.smallDescription') }}
      </div>
      <div class="button-container">
        <StandardButton :label="$t('buttons.save')" @click="saveMedication" />
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

    const selectedMedicine = ref(null);

    const medicineOptions = [
      { key: 'notfallkontrazeptiva', value: 3 },
      { key: 'diclofenac', value: 1 },
      { key: 'ibuprofen', value: 2 }
    ];

    const translatedMedicineOptions = computed(() => {
      return medicineOptions.map(option => ({
        label: t(`logCycle.medicine.options.${option.key}`),
        value: option.value
      }));
    });

    const goBack = () => {
      window.history.back();
    };

    const saveMedication = async () => {
      if (selectedMedicine.value === null) {
        return;
      }

      const requestBody = {
        start_date: new Date().toISOString().split('T')[0],
        end_date: new Date().toISOString().split('T')[0], 
        medication_id: selectedMedicine.value
      };

      try {
        await authStore.refreshAccessToken(); 

        await api.post('/cycles/medication/', requestBody, {
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${authStore.accessToken}`
          }
        });

        router.push('/log-cycle');
      
      } catch (error) {
        console.error('Fehler beim Speichern des Medikaments', error);
        alert("Fehler beim Speichern des Medikaments!");
      }
    };

    return {
      selectedMedicine,
      translatedMedicineOptions,
      goBack,
      saveMedication
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
  </style>
  