<template>
  <div class="welcome-container">
    <div class="header">
      <q-btn flat dense round icon="arrow_back" @click="goBack" />
      <div class="title">{{ $t('logCycle.mens.title') }}</div>
    </div>
    <div class="linie"></div>
    <div class="button-container">
      <StandardButton :label="buttonLabel" @click="toggleMenstruationStatus" />
    </div>
    <div class="welcome-text">
      <p class="description">{{ descriptionText }}</p>
    </div>
  </div>
</template>

<script>
import StandardButton from 'components/StandardButton.vue';

export default {
  components: {
    StandardButton
  },
  data() {
    return {
      buttonLabel: this.$t('logCycle.mens.buttonLabel'),
      descriptionText: this.$t('logCycle.mens.descriptionText')
    };
  },
  methods: {
    goBack() {
      window.history.back();
    },
    toggleMenstruationStatus() {
      if (this.buttonLabel === this.$t('logCycle.mens.buttonLabel')) {
        this.buttonLabel = this.$t('logCycle.mens.buttonLabelActive');
        this.descriptionText = this.$t('logCycle.mens.descriptionTextActive');
      } else {
        this.buttonLabel = this.$t('logCycle.mens.buttonLabel');
        this.descriptionText = this.$t('logCycle.mens.descriptionText');
      }
    }
  },
  watch: {
    '$i18n.locale': {
      handler() {
        this.buttonLabel = this.$t('logCycle.mens.buttonLabel');
        this.descriptionText = this.$t('logCycle.mens.descriptionText');
      },
      immediate: true
    }
  }
};
</script>

  <style scoped>
  .welcome-container {
    display: flex;
    flex-direction: column;
    align-items: flex-start; 
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
    font: 12px/22px 'Inter', sans-serif;
    margin-top: 5px;
  }
  
  .button-container {
    margin-top: 20px;
    margin-left: 0; 
    width: 100%;
  }

  @media only screen and (min-width: 200px) {
    .welcome-container {
      max-width: 350px;
      margin: auto;
    }
  }
  </style>
  