<template>
    <div class="welcome-container">
      <div class="header">
        <q-btn flat dense round icon="arrow_back" @click="goBack" />
        <div class="title">Zyklus Log-Eintrag</div>
        <q-btn flat dense round icon="edit" />
      </div>
      <div class="linie"></div>
      <div class="icon-grid">
        <div class="icon-item" v-for="(item, index) in iconItems" :key="index">
          <img :src="item.icon" class="icon" @click="handleIconClick(item.label)" />
          <div class="icon-label">{{ formatLabel(item.label) }}</div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        iconItems: [
          { label: 'Menstruation', icon: '/src/assets/log_Zyklus/icon_mens.svg' },
          { label: 'Temperatur', icon: '/src/assets/log_Zyklus/icon_temperature.svg' },
          { label: 'Zervixschleim', icon: '/src/assets/log_Zyklus/icon_cerfix.svg' },
          { label: 'Gebärmutterhals', icon: '/src/assets/log_Zyklus/icon_gebaermutter.svg' },
          { label: 'Geschlechtsverkehr', icon: '/src/assets/log_Zyklus/icon_heart.svg' },
          { label: 'Verhütungsmittel', icon: '/src/assets/log_Zyklus/icon_spirale.svg' },
          { label: 'Medikamente', icon: '/src/assets/log_Zyklus/icon_medicine.svg' },
          { label: 'Ovulationstest', icon: '/src/assets/log_Zyklus/icon_ovuTest.svg' },
          { label: 'Schwangerschaftstest', icon: '/src/assets/log_Zyklus/icon_pregTest.svg' }
        ]
      };
    },
    methods: {
      goBack() {
        window.history.back();
      },
      handleIconClick(label) {
        if (label === 'Menstruation') {
          this.$router.push({ name: 'LogCycleMens' });
        } else if (label === 'Temperatur') {
          this.$router.push({ name: 'LogCycleTemp' });
        } else if (label === 'Zervixschleim') {
          this.$router.push({ name: 'LogCycleCerfix' });
        } else if (label === 'Gebärmutterhals') {
          this.$router.push({ name: 'LogCycleGebaermutter' });
        } else if (label === 'Geschlechtsverkehr') {
          this.$router.push({ name: 'LogCycleSex' });
        } else if (label === 'Verhütungsmittel') {
          this.$router.push({ name: 'LogCycleContraceptive' });
        } else if (label === 'Medikamente') {
          this.$router.push({ name: 'LogCycleMedicine' });
        } else if (label === 'Ovulationstest') {
          this.$router.push({ name: 'LogCycleOvulationTest' });
        } else if (label === 'Schwangerschaftstest') {
          this.$router.push({ name: 'LogCyclePregnancyTest' });
        } 

      },
      formatLabel(label) {
        if (label === 'Gebärmutterhals' || label === 'Geschlechtsverkehr') {
          return label.slice(0, 11) + '-' + label.slice(11);
        } else if (label === 'Verhütungsmittel') {
          return label.slice(0, 10) + '-' + label.slice(10);
        } else if (label === 'Schwangerschaftstest') {
          return label.slice(0, 9) + '-' + label.slice(9);
        } else {
          return label;
        }
      }
    }
  };
  </script>
  
  <style scoped>
  .welcome-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 90%;
    height: 100vh;
    overflow: auto;
    margin: auto;
  }
  
  .linie {
    display: flex;
    flex-direction: column;
    align-items: center;
    overflow: auto;
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
  }
  
  .icon-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(100px, 1fr));
    gap: 10px;
    width: 100%;
    max-width: 600px;
    margin-top: 25px;
    justify-content: center;
  }
  
  .icon-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-bottom: 20px;
  }
  
  .icon {
    width: 60px;
    height: 60px;
    cursor: pointer; 
  }
  
  .icon-label {
    margin-top: 10px;
    text-align: center;
    font-size: 14px;
    padding: 0 5px;
  }
  </style>
  