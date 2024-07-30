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
          :options="translatedTrainingOptions"
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
          input-class="text-left"
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
import { ref, computed } from 'vue';
import { useRouter } from 'vue-router';
import { useI18n } from 'vue-i18n';
import StandardButton from 'components/StandardButton.vue';
import RadioToggle from 'components/RadioToggle.vue';
import { useTrainingStore } from 'src/stores/training';

export default {
  components: {
    StandardButton,
    RadioToggle
  },
  setup() {
    const { t } = useI18n();
    const router = useRouter();
    const trainingStore = useTrainingStore();

    const trainingStatus = ref(null);
    const selectedActivity = ref(null);
    const duration = ref(null);

    const trainingOptions = [
      { key: 'other_sports', value: 1 },
      { key: 'aqua_fitness', value: 2 },
      { key: 'athletics', value: 3 },
      { key: 'badminton', value: 4 },
      { key: 'basketball', value: 5 },
      { key: 'canoeing', value: 6 },
      { key: 'climbing', value: 7 },
      { key: 'cross_country_skiing', value: 8 },
      { key: 'cycling', value: 9 },
      { key: 'dancing', value: 10 },
      { key: 'diving', value: 11 },
      { key: 'fitness_training', value: 12 },
      { key: 'floorball', value: 13 },
      { key: 'football', value: 14 },
      { key: 'golf', value: 15 },
      { key: 'gymnastics', value: 16 },
      { key: 'handball', value: 17 },
      { key: 'hiking', value: 18 },
      { key: 'horse_riding', value: 19 },
      { key: 'ice_hockey', value: 20 },
      { key: 'ice_skating', value: 21 },
      { key: 'inline_skating', value: 22 },
      { key: 'martial_arts', value: 23 },
      { key: 'mountain_biking', value: 24 },
      { key: 'rowing', value: 25 },
      { key: 'running', value: 26 },
      { key: 'sailing', value: 27 },
      { key: 'shooting', value: 28 },
      { key: 'ski_snowboard_tours', value: 29 },
      { key: 'skiing', value: 30 },
      { key: 'sledding', value: 31 },
      { key: 'snowboarding', value: 32 },
      { key: 'snowshoeing', value: 33 },
      { key: 'squash', value: 34 },
      { key: 'strength_training', value: 35 },
      { key: 'surfing', value: 36 },
      { key: 'swimming', value: 37 },
      { key: 'table_tennis', value: 38 },
      { key: 'tennis', value: 39 },
      { key: 'volleyball', value: 40 },
      { key: 'walking', value: 41 },
      { key: 'yoga', value: 42 }
    ];

    const translatedTrainingOptions = computed(() => {
      return trainingOptions.map(option => ({
        label: t(`logTrainingStrainPre.trainingOptions.options.${option.key}`),
        value: option.value
      }));
    });

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
      translatedTrainingOptions,
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



.form-group p {
  margin: 0;
  font-size: 16px;
  margin-left: 7px;
  margin-right: 7px;
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
