<template>
  <div class="size-container">
  <div class="welcome-container">
    <div class="header">
      <q-btn flat dense round icon="arrow_back" @click="goBack" />
      <div class="title">{{ $t('logCycle.homeList.editListTitle') }}</div>
    </div>
    <div class="linie"></div>
    <div v-for="(item, index) in iconItems" :key="index" class="icon-item" @click="toggleSelect(index)">
      <div class="left-circle">
        <q-icon :name="item.selected ? 'lens' : 'radio_button_unchecked'" color="primary" size="25px" />
      </div>
      <div class="icon-label">{{ $t(`logCycle.homeList.labels.${item.key}`) }}</div>
    </div>
    <div class="button-container">
      <StandardButton @click="saveChanges" :label="$t('buttons.save')" />
    </div>
  </div>
  </div>
</template>

<script>
import StandardButton from 'components/StandardButton.vue';

export default {
  name: 'LogCycleHomeList',
  components: {
    StandardButton
  },
  data() {
    return {
      iconItems: []
    };
  },
  methods: {
    goBack() {
      this.$router.push({ name: 'LogCycleHome' });
    },
    toggleSelect(index) {
      this.iconItems[index].selected = !this.iconItems[index].selected;
    },
    saveChanges() {
      localStorage.setItem('iconItems', JSON.stringify(this.iconItems));
      window.dispatchEvent(new Event('storage'));
      this.$router.push({ name: 'LogCycleHome' });
    }
  },
  created() {
    const defaultIconItems = [
      { key: 'menstruation', selected: true },
      { key: 'temperature', selected: true },
      { key: 'cervixMucus', selected: true },
      { key: 'cervixPosition', selected: true },
      { key: 'sex', selected: true },
      { key: 'medicine', selected: true },
      { key: 'ovulationTest', selected: true },
      { key: 'pregnancyTest', selected: true }
    ];
    const storedItems = JSON.parse(localStorage.getItem('iconItems'));
    if (storedItems) {
      this.iconItems = storedItems.map(item => ({
        ...item,
        key: item.key || defaultIconItems.find(i => i.label === item.label)?.key,
        label: this.$t(`logCycle.homeList.labels.${item.key}`)
      }));
    } else {
      this.iconItems = defaultIconItems;
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
  margin-top: 20px;
}

.title {
  font: 600 20px 'Inter', sans-serif;
  color: #000;
  text-align: center;
  flex-grow: 1;
  padding-right: 30px;
}

.icon-item {
  display: flex;
  align-items: center;
  width: 100%;
  padding: 15px;
  border-bottom: 0.5px solid #e0e0e0;
  cursor: pointer;
}

.left-circle {
  margin-right: 15px;
}

.icon-label {
  flex-grow: 1;
  font-size: 16px;
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
