<template>
  <div class="size-container">
  <div class="welcome-container">
    <div class="header">
      <q-btn flat dense round icon="arrow_back" @click="goBack" />
      <div class="title">{{ $t('logCycle.home.title') }}</div>
      <q-btn flat dense round icon="edit" @click="navigateToEdit" />
    </div>
    <div class="linie"></div>
    <div class="icon-grid">
      <div class="icon-item" v-for="(item, index) in selectedIconItems" :key="index">
        <img :src="item.icon" class="icon" @click="handleIconClick(item.key)" />
        <div class="icon-label">{{ $t(`logCycle.home.labels.${item.key}`) }}</div>
      </div>
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
    handleIconClick(key) {
      const routes = {
        menstruation: 'LogCycleMens',
        temperature: 'LogCycleTemp',
        cervixMucus: 'LogCycleCerfix',
        cervixPosition: 'LogCycleGebaermutter',
        sex: 'LogCycleSex',
        medicine: 'LogCycleMedicine',
        ovulationTest: 'LogCycleOvulationTest',
        pregnancyTest: 'LogCyclePregnancyTest'
      };
      if (routes[key]) {
        this.$router.push({ name: routes[key] });
      }
    },
    updateIconItems() {
      const defaultIconItems = [
        { key: 'menstruation', icon: '/log_ZyklusEntry/icon_mens.svg', selected: true },
        { key: 'temperature', icon: '/log_ZyklusEntry/icon_temperature.svg', selected: true },
        { key: 'cervixMucus', icon: '/log_ZyklusEntry/icon_cerfix.svg', selected: true },
        { key: 'cervixPosition', icon: '/log_ZyklusEntry/icon_gebaermutter.svg', selected: true },
        { key: 'sex', icon: '/log_ZyklusEntry/icon_heart.svg', selected: true },
        { key: 'medicine', icon: '/log_ZyklusEntry/icon_medicine.svg', selected: true },
        { key: 'ovulationTest', icon: '/log_ZyklusEntry/icon_ovuTest.svg', selected: true },
        { key: 'pregnancyTest', icon: '/log_ZyklusEntry/icon_pregTest.svg', selected: true }
      ];
      const storedItems = JSON.parse(localStorage.getItem('iconItems'));
      if (storedItems) {
        this.iconItems = storedItems.map(item => ({
          ...item,
          key: item.key || defaultIconItems.find(i => i.label === item.label)?.key,
          label: this.$t(`logCycle.home.labels.${item.key}`)
        }));
      } else {
        this.iconItems = defaultIconItems;
        localStorage.setItem('iconItems', JSON.stringify(this.iconItems));
      }
    }
  },
  created() {
    window.addEventListener('storage', this.updateIconItems);
    this.updateIconItems();
  },
  beforeUnmount() {
    window.removeEventListener('storage', this.updateIconItems);
  },
  watch: {
    '$i18n.locale': {
      handler() {
        this.updateIconItems();
      },
      immediate: true
    }
  }
};
</script>

<style scoped>


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
  margin-top: 20px;
}

.title {
  font: 600 20px 'Inter', sans-serif;
  color: #000;
  text-align: center;
}

.icon-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
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
