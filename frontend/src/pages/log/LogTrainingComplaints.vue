<template>
  <div class="size-container">
    <div class="welcome-container">
      <div class="header">
        <q-btn flat dense round icon="arrow_back" @click="goBack" />
        <div class="title">{{ $t('logTrainingComplaints.title') }}</div>
      </div>
      <div class="linie"></div>
      <div class="description">
        {{ $t('logTrainingComplaints.descriptionPart1') }}<br>
        {{ $t('logTrainingComplaints.descriptionPart2') }}
      </div>
      <div class="slider">
        <SliderWithLabelVertical
          :topText="$t('logTrainingComplaints.slider.topText')"
          :bottomText="$t('logTrainingComplaints.slider.bottomText')"
          v-model="complaints"
        />
      </div>
      <div class="button-container">
        <StandardButton :label="$t('buttons.next')" @click="navigateToNextStep" />
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed } from 'vue';
import { useRouter } from 'vue-router';
import SliderWithLabelVertical from 'components/SliderWithLabelVertical.vue';
import StandardButton from 'components/StandardButton.vue';
import { useTrainingStore } from 'src/stores/training';

export default {
  components: {
    SliderWithLabelVertical,
    StandardButton
  },
  setup() {
    const router = useRouter();
    const trainingStore = useTrainingStore();
    const complaints = ref(6);

    // Berechne den invertierten Wert
    const invertedComplaints = computed(() => {
      return 6 - complaints.value;
    });

    const navigateToNextStep = () => {
      trainingStore.setComplaints(invertedComplaints.value); // Setze den umgerechneten Wert
      router.push({ name: 'LogTrainingMood' });
    };

    const goBack = () => {
      window.history.back();
    };

    return {
      complaints,
      navigateToNextStep,
      goBack
    };
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
  