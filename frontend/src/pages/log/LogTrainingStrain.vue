<template>
  <div class="size-container">
  <div class="welcome-container">
    <div class="header">
      <q-btn flat dense round icon="arrow_back" @click="goBack" />
      <div class="title">{{ $t('logTrainingStrain.title') }}</div>
    </div>
    <div class="linie"></div>
    <div class="description">
      <span v-html="$t('logTrainingStrain.description')"></span>
    </div>
    <div class="slider">
      <SliderWithLabelVertical10 :topText="$t('logTrainingStrain.slider.topText')" :bottomText="$t('logTrainingStrain.slider.bottomText')" />
    </div>
    <div class="button-container">
      <StandardButton :label="$t('buttons.next')" @click="navigateToNextStep" />
    </div>
  </div>
  </div>
</template>
  
  <script>
  import SliderWithLabelVertical10 from 'components/SliderWithLabelVertical10.vue';
  import StandardButton from 'components/StandardButton.vue'
  
  export default {
    components: {
      SliderWithLabelVertical10,
      StandardButton
    },
    methods: {
      goBack() {
        window.history.back();
      },
    navigateToNextStep() {
      this.$router.push({ name: 'LogTrainingComplaints' });
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
    padding-right: 10%;
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
  