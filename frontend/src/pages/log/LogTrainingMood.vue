<template>
  <div class="size-container">
  <div class="welcome-container">
    <div class="header">
      <q-btn flat dense round icon="arrow_back" @click="goBack" />
      <div class="title">{{ $t('logTrainingMood.title') }}</div>
    </div>
    <div class="linie"></div>
    <div class="description">
      <span v-html="$t('logTrainingMood.description')"></span>
    </div>
    <div class="slider">
      <SliderWithLabelVertical :topText="$t('logTrainingMood.slider.topText')" :bottomText="$t('logTrainingMood.slider.bottomText')" />
    </div>
    <div class="button-container">
      <StandardButton :label="$t('buttons.next')" @click="navigateToNextStep" />
    </div>
  </div>
  </div>
</template>
  
  <script>
  import SliderWithLabelVertical from 'components/SliderWithLabelVertical.vue';
  import StandardButton from 'components/StandardButton.vue'
  
  export default {
    components: {
      SliderWithLabelVertical,
      StandardButton
    },
    methods: {
      goBack() {
        window.history.back();
      },
    navigateToNextStep() {
      this.$router.push({ name: 'LogTrainingRecovery' });
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
    text-align: center;
    width: 100%;
    margin-top: 30px;
    font-size: 16px;
    font-weight: 500;
    margin-bottom: 10px;
  }
  .slider {
    margin-top: 40px;
    padding-right: 6%;
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
  