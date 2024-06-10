<template>
  <div class="welcome-container">
    <div class="header">
      <q-btn flat dense round icon="arrow_back" @click="goBack" />
      <div class="title">Zyklus Log-Eintrag</div>
      <q-btn flat dense round icon="edit" @click="navigateToEdit" />
    </div>
    <div class="linie"></div>
    <div class="icon-grid">
      <div class="icon-item" v-for="(item, index) in selectedIconItems" :key="index">
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
      iconItems: []
    };
  },
  computed: {
    selectedIconItems() {
      return this.iconItems.filter(item => item.selected);
    }
  },
  methods: {
    goBack() {
      this.$router.push({ name: 'LogHome' });
    },
    navigateToEdit() {
      this.$router.push({ name: 'LogCycleHomeList' });
    },
    handleIconClick(label) {
      const routes = {
        'Menstruation': 'LogCycleMens',
        'Temperatur': 'LogCycleTemp',
        'Zervixschleim': 'LogCycleCerfix',
        'Gebärmutterhals': 'LogCycleGebaermutter',
        'Geschlechtsverkehr': 'LogCycleSex',
        'Verhütungsmittel': 'LogCycleContraceptive',
        'Medikamente': 'LogCycleMedicine',
        'Ovulationstest': 'LogCycleOvulationTest',
        'Schwangerschaftstest': 'LogCyclePregnancyTest'
      };
      if (routes[label]) {
        this.$router.push({ name: routes[label] });
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
  },
  created() {
    const storedItems = localStorage.getItem('iconItems');
    if (storedItems) {
      this.iconItems = JSON.parse(storedItems);
    } else {
      this.iconItems = [
        { label: 'Menstruation', icon: '/src/assets/log_Zyklus/icon_mens.svg', selected: true },
        { label: 'Temperatur', icon: '/src/assets/log_Zyklus/icon_temperature.svg', selected: true },
        { label: 'Zervixschleim', icon: '/src/assets/log_Zyklus/icon_cerfix.svg', selected: true },
        { label: 'Gebärmutterhals', icon: '/src/assets/log_Zyklus/icon_gebaermutter.svg', selected: true },
        { label: 'Geschlechtsverkehr', icon: '/src/assets/log_Zyklus/icon_heart.svg', selected: true },
        { label: 'Verhütungsmittel', icon: '/src/assets/log_Zyklus/icon_spirale.svg', selected: true },
        { label: 'Medikamente', icon: '/src/assets/log_Zyklus/icon_medicine.svg', selected: true },
        { label: 'Ovulationstest', icon: '/src/assets/log_Zyklus/icon_ovuTest.svg', selected: true },
        { label: 'Schwangerschaftstest', icon: '/src/assets/log_Zyklus/icon_pregTest.svg', selected: true }
      ];
      localStorage.setItem('iconItems', JSON.stringify(this.iconItems));
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
