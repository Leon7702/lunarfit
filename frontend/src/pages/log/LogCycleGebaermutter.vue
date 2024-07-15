<template>
  <div class="size-container">
  <div class="welcome-container">
    <div class="header">
      <q-btn flat dense round icon="arrow_back" @click="goBack" />
      <div class="title">{{ $t('logCycle.cervixPosition.title') }}</div>
    </div>
    <div class="linie"></div>
    <p class="description">
      {{ $t('logCycle.cervixPosition.description') }}
    </p>
    <div class="icon-grid">
      <div
        class="icon-item"
        v-for="(item, index) in iconItems"
        :key="index"
        @click="selectItem(index)"
        :class="{ selected: selectedIndex === index }"
      >
        <div class="icon-wrapper">
          <img :src="item.icon" class="icon" />
          <div class="icon-circle" :class="{ active: selectedIndex === index }"></div>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
export default {
  data() {
    return {
      iconItems: [],
      selectedIndex: null // Hinzufügen der selectedIndex-Eigenschaft
    };
  },
  computed: {
    localizedIcons() {
      return {
        closed: this.$t('logCycle.cervixPosition.icons.closed'),
        partiallyOpen: this.$t('logCycle.cervixPosition.icons.partiallyOpen'),
        fullyOpen: this.$t('logCycle.cervixPosition.icons.fullyOpen')
      };
    }
  },
  watch: {
    '$i18n.locale': 'updateIconItems'
  },
  methods: {
    goBack() {
      window.history.back();
    },
    selectItem(index) {
      this.selectedIndex = index; // Setzen des ausgewählten Index
    },
    updateIconItems() {
      this.iconItems = [
        { icon: this.localizedIcons.closed },
        { icon: this.localizedIcons.partiallyOpen },
        { icon: this.localizedIcons.fullyOpen }
      ];
    }
  },
  created() {
    this.updateIconItems();
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
}

.icon-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(100px, 1fr));
  width: 100%;
  max-width: 600px;
  justify-content: center;
}

.icon-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 12px;
  cursor: pointer; 
}

.icon-wrapper {
  position: relative;
  width: 180px; /* 60px * 3 */
  height: 180px; /* 60px * 3 */
}

.icon {
  width: 100%;
  height: 100%;
}

.icon-circle {
  position: absolute;
  bottom: 15px;
  left: 50%;
  transform: translateX(-50%);
  width: 25px;
  height: 25px;
  border-radius: 50%;
  background-color: lightgray;
  transition: background-color 0.3s;
}

.icon-circle.active {
  background-color: var(--q-primary);
}

</style>
