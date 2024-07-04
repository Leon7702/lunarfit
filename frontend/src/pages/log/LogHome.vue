<template>
  <div class="welcome-container">
    <!-- Inhalt des ersten Bildschirms hier... -->
    <div class="welcome-text">
      <h1 class="title">{{ $t('logEntry.title') }}</h1>
    </div>
    <DateTodayPicker class="date" />
    <img src="/src/assets/log_zyklus.svg" alt="Zyklus Button" class="image" @click="navigateToCycle" />
    <img src="/src/assets/log_training.svg" alt="Training Button" class="image" @click="navigateToTraining" />
    <img src="/src/assets/log_notes.svg" alt="Notizen Button" class="image" @click="navigateToNotes" />
  </div>
</template>

<script>
import DateTodayPicker from 'components/DateTodayPicker.vue'

export default {
  components: {
    DateTodayPicker
  },
  methods: {
    goBack() {
      window.history.back();
    },
    navigateToCycle() {
      this.$router.push({ name: 'LogCycleHome' });
    },
    navigateToTraining() {
      this.$router.push({ name: 'LogTrainingStrainPre' });
    },
    navigateToNotes() {
      this.$router.push({ name: 'LogNotes' });
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
  overflow: auto;
  margin: auto;
}

.image {
  margin-bottom: 5px;
  object-fit: auto;
  object-position: center;
  width: 100%;
}

.welcome-text {
  margin-top: 20px;
}

.title {
  font: 600 24px 'Inter', sans-serif; 
}

.date {
  margin-bottom: 10px;
}

@media only screen and (min-width: 200px) {
  .welcome-container {
    max-width: 350px;
    margin: auto;
  }
}
</style>
