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
        <DropDownSingleSelect :options="trainingOptions" v-model="selectedActivity"/>
      </div>
      <div class="form-group spacer" v-if="trainingStatus === 'ja'"></div> 
      <div class="form-group" v-if="trainingStatus === 'ja'">
        <p>{{ $t('logTrainingStrainPre.durationOptions.prompt') }}</p>
        <FormFieldText id="duration" label="" iconName="" inputType="number" />
      </div>
      <div class="button-container">
        <StandardButton :label="$t('buttons.next')" @click="navigateToNextStep" />
      </div>
    </div>
  </div>
  </template>
  
  <script>
  import StandardButton from 'components/StandardButton.vue';
  import RadioToggle from 'components/RadioToggle.vue';
  import DropDownSingleSelect from 'components/DropDownSingleSelect.vue';
  import FormFieldText from 'components/FormFieldText.vue';
  
  export default {
    components: {
      StandardButton,
      RadioToggle,
      DropDownSingleSelect,
      FormFieldText
    },
    data() {
      return {
        trainingStatus: null,
        trainingOptions: [
          this.$t('logTrainingStrainPre.trainingOptions.options.hiking'),
          this.$t('logTrainingStrainPre.trainingOptions.options.cycling'),
          this.$t('logTrainingStrainPre.trainingOptions.options.swimming'),
          this.$t('logTrainingStrainPre.trainingOptions.options.skiing'),
          this.$t('logTrainingStrainPre.trainingOptions.options.running'),
          this.$t('logTrainingStrainPre.trainingOptions.options.strength_training'),
          this.$t('logTrainingStrainPre.trainingOptions.options.fitness_training'),
          this.$t('logTrainingStrainPre.trainingOptions.options.yoga'),
          this.$t('logTrainingStrainPre.trainingOptions.options.walking'),
          this.$t('logTrainingStrainPre.trainingOptions.options.mountain_biking'),
          this.$t('logTrainingStrainPre.trainingOptions.options.snowshoeing'),
          this.$t('logTrainingStrainPre.trainingOptions.options.sledding'),
          this.$t('logTrainingStrainPre.trainingOptions.options.gymnastics'),
          this.$t('logTrainingStrainPre.trainingOptions.options.dancing'),
          this.$t('logTrainingStrainPre.trainingOptions.options.football'),
          this.$t('logTrainingStrainPre.trainingOptions.options.cross_country_skiing'),
          this.$t('logTrainingStrainPre.trainingOptions.options.volleyball'),
          this.$t('logTrainingStrainPre.trainingOptions.options.badminton'),
          this.$t('logTrainingStrainPre.trainingOptions.options.inline_skating'),
          this.$t('logTrainingStrainPre.trainingOptions.options.climbing'),
          this.$t('logTrainingStrainPre.trainingOptions.options.snowboarding'),
          this.$t('logTrainingStrainPre.trainingOptions.options.ski_snowboard_tours'),
          this.$t('logTrainingStrainPre.trainingOptions.options.table_tennis'),
          this.$t('logTrainingStrainPre.trainingOptions.options.tennis'),
          this.$t('logTrainingStrainPre.trainingOptions.options.shooting'),
          this.$t('logTrainingStrainPre.trainingOptions.options.diving'),
          this.$t('logTrainingStrainPre.trainingOptions.options.ice_skating'),
          this.$t('logTrainingStrainPre.trainingOptions.options.aqua_fitness'),
          this.$t('logTrainingStrainPre.trainingOptions.options.surfing'),
          this.$t('logTrainingStrainPre.trainingOptions.options.horse_riding'),
          this.$t('logTrainingStrainPre.trainingOptions.options.floorball'),
          this.$t('logTrainingStrainPre.trainingOptions.options.basketball'),
          this.$t('logTrainingStrainPre.trainingOptions.options.golf'),
          this.$t('logTrainingStrainPre.trainingOptions.options.squash'),
          this.$t('logTrainingStrainPre.trainingOptions.options.martial_arts'),
          this.$t('logTrainingStrainPre.trainingOptions.options.sailing'),
          this.$t('logTrainingStrainPre.trainingOptions.options.athletics'),
          this.$t('logTrainingStrainPre.trainingOptions.options.rowing'),
          this.$t('logTrainingStrainPre.trainingOptions.options.canoeing'),
          this.$t('logTrainingStrainPre.trainingOptions.options.ice_hockey'),
          this.$t('logTrainingStrainPre.trainingOptions.options.handball'),
          this.$t('logTrainingStrainPre.trainingOptions.options.other_sports')
        ],
        selectedActivity: null
      };
    },
    methods: {
      goBack() {
        window.history.back();
      },
      navigateToNextStep() {
        if (this.trainingStatus === 'ja') {
          this.$router.push({ name: 'LogTrainingStrain' });
        } else {
          this.$router.push({ name: 'LogTrainingComplaints' });
        }
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
