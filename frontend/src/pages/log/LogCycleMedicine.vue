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
      <DropDownSingleSelect :options="medicineOptions" v-model="selectedMedicine" placeholder="Auswählen" />
    </div>
    <div class="small-description">
      {{ $t('logCycle.medicine.smallDescription') }}
    </div>
  </div>
  </div>
</template>

<script>
import DropDownSingleSelect from 'components/DropDownSingleSelect.vue';

export default {
  components: {
    DropDownSingleSelect
  },
  data() {
    return {
      selectedMedicine: null,
      medicineOptions: [
        { label: this.$t('logCycle.medicine.options.notfallkontrazeptiva'), value: 'Notfallkontrazeptiva' },
        { label: this.$t('logCycle.medicine.options.hormonersatz'), value: 'Hormonersatz' },
        { label: this.$t('logCycle.medicine.options.opioideSchmerzmittel'), value: 'Opiode Schmerzmittel' },
        { label: this.$t('logCycle.medicine.options.diclofenacIbuprofen'), value: 'Diclofenac/Ibuprofen' }
      ]
    };
  },
  methods: {
    goBack() {
      window.history.back();
    }
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
  </style>
  