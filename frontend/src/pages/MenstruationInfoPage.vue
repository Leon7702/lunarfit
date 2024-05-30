<template>
  <div class="info-container">
    <BackButtonText />
    <PhaseInfoCard title="Menstruation"
      text="Der Zyklus beginnt mit dem ersten Tag der Blutung, die durch den Abfall con Progesteron und Östrogen ausgelöst wird. Das steigende Östrogen hebt die Launer, macht selbstbewusst und kreativ." />
    <img class="cycle-image" src="../assets/CyclePhaseGraph.jpg" alt="Graph" />
      <PhaseInformation :textNutrition="textNutrition" :textTraining="textTraining" :textHealth="textHealth" />
  </div>
</template>

<script>
import BackButtonText from 'components/BackButtonText.vue';
import PhaseInformation from 'src/components/PhaseInformation.vue';
import PhaseInfoCard from 'src/components/PhaseInfoCard.vue';

export default {
  components: {
    BackButtonText,
    PhaseInfoCard,
    PhaseInformation,
  },
  data() {
    return {
      textNutrition: "Probeotische Lebensmittel: Frische Sprossen, Sauerkraut",
      textTraining: "Die Sauerstoffaufnahme ist erhöht und die Erholungsfähigkeit verbessert sich. Kraftaufbau. Intervalltraining, Schnelligkeitstraining, neue Belastungsreite, hohe Intensität.",
      textHealth: "Text für Gesundheit"
    }
  }
}
</script>

<style scoped>

.info-container {
  display: flex;
  flex-direction: column;
  position: relative;
}

.cycle-image {
  width: 100%;
  height: auto;
}
</style>
