<template>
  <div class="welcome-container">
    <div class="header">
      <q-btn flat dense round icon="arrow_back" @click="goBack" />
      <div class="title">{{ $t('logCycle.pregnancyTest.title') }}</div>
    </div>
    <div class="linie"></div>
    <p class="description">
      {{ $t('logCycle.pregnancyTest.description') }}
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
        <div class="icon-label">{{ item.label }}</div>
      </div>
    </div>
  </div>
</template>
  <script>
  export default {
    data() {
      return {
        iconItems: [
          { icon: '/src/assets/log_Zyklus/test_positiv.svg' },
          { icon: '/src/assets/log_Zyklus/test_negativ.svg' },
          { icon: '/src/assets/log_Zyklus/test_ungueltig.svg' }
        ],
        selectedIndex: null
      };
    },
    methods: {
      goBack() {
        window.history.back();
      },
      selectItem(index) {
        this.selectedIndex = index;
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
    width: 140px;
    height: 240px;
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

  @media only screen and (min-width: 200px) {
    .welcome-container {
      max-width: 350px;
      margin: auto;
    }
  }
  </style>
  