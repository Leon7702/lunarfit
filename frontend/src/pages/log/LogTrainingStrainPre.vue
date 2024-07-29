<template>
  <div class="size-container">
    <div class="welcome-container">
      <div class="header">
        <q-btn flat dense round icon="arrow_back" @click="goBack" />
        <div class="title">{{ $t('logTrainingStrainPre.title') }}</div>
      </div>
      <div class="linie"></div>
      <div class="form-group">
        <p>{{ $t('logTrainingStrainPre.description1') }}</p>
        <RadioToggle v-model="trainingStatus" />
      </div>
      <div class="form-group" v-if="trainingStatus === 'ja'">
        <p>{{ $t('logTrainingStrainPre.trainingOptions.prompt') }}</p>
        <q-select
          filled
          v-model="selectedActivity"
          :options="trainingOptions"
          input-class="text-right"
          class="q-mb-sm"
          emit-value
          map-options
        />
      </div>
      <div class="form-group spacer" v-if="trainingStatus === 'ja'"></div>
      <div class="form-group" v-if="trainingStatus === 'ja'">
        <p>{{ $t('logTrainingStrainPre.durationOptions.prompt') }}</p>
        <q-input
          filled
          v-model="duration"
          type="number"
          input-class="text-right"
          class="q-mb-sm"
        />
      </div>
      <div class="button-container">
        <StandardButton :label="$t('buttons.next')" @click="navigateToNextStep" />
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import StandardButton from 'components/StandardButton.vue';
import RadioToggle from 'components/RadioToggle.vue';
import { useTrainingStore } from 'src/stores/training';

export default {
  components: {
    StandardButton,
    RadioToggle
  },
  setup() {
    const router = useRouter();
    const trainingStore = useTrainingStore();

    const trainingStatus = ref(null);
    const selectedActivity = ref(null);
    const duration = ref(null);

    const trainingOptions = [
      { label: 'Other Sports', value: 1 },
      { label: 'Aqua Fitness', value: 2 },
      { label: 'Athletics', value: 3 },
      { label: 'Badminton', value: 4 },
      { label: 'Basketball', value: 5 },
      { label: 'Canoeing', value: 6 },
      { label: 'Climbing', value: 7 },
      { label: 'Cross Country Skiing', value: 8 },
      { label: 'Cycling', value: 9 },
      { label: 'Dancing', value: 10 },
      { label: 'Diving', value: 11 },
      { label: 'Fitness Training', value: 12 },
      { label: 'Floorball', value: 13 },
      { label: 'Football', value: 14 },
      { label: 'Golf', value: 15 },
      { label: 'Gymnastics', value: 16 },
      { label: 'Handball', value: 17 },
      { label: 'Hiking', value: 18 },
      { label: 'Horse Riding', value: 19 },
      { label: 'Ice Hockey', value: 20 },
      { label: 'Ice Skating', value: 21 },
      { label: 'Inline Skating', value: 22 },
      { label: 'Martial Arts', value: 23 },
      { label: 'Mountain Biking', value: 24 },
      { label: 'Rowing', value: 25 },
      { label: 'Running', value: 26 },
      { label: 'Sailing', value: 27 },
      { label: 'Shooting', value: 28 },
      { label: 'Ski Snowboard Tours', value: 29 },
      { label: 'Skiing', value: 30 },
      { label: 'Sledding', value: 31 },
      { label: 'Snowboarding', value: 32 },
      { label: 'Snowshoeing', value: 33 },
      { label: 'Squash', value: 34 },
      { label: 'Strength Training', value: 35 },
      { label: 'Surfing', value: 36 },
      { label: 'Swimming', value: 37 },
      { label: 'Table Tennis', value: 38 },
      { label: 'Tennis', value: 39 },
      { label: 'Volleyball', value: 40 },
      { label: 'Walking', value: 41 },
      { label: 'Yoga', value: 42 }
    ];

    const navigateToNextStep = () => {
      if (trainingStatus.value === 'ja') {
        trainingStore.setStart(new Date().toISOString()); // Zeit des Trainings
        trainingStore.setSport(selectedActivity.value);
        trainingStore.setDuration(duration.value);
        router.push({ name: 'LogTrainingStrain' });
      } else {
        router.push({ name: 'LogTrainingComplaints' });
      }
    };

    return {
      trainingStatus,
      selectedActivity,
      duration,
      trainingOptions,
      navigateToNextStep,
      goBack() {
        window.history.back();
      }
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
    margin-bottom: 30px;
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

.form-group {
    width: 100%;
}

.form-group p {
    text-align: left;
    width: 100%;
    font-size: 16px;
    font-weight: 500;
}

.form-group.spacer {
    margin-bottom: 20px; 
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
