<template>
  <!-- TODO: Change size of the cards, because needs to fit with the toolbar in one screen. -->
  <main class="card-container">
    <!-- Card for Cycle information -->
    <div class="q-pa-sm q-pt-lg">
      <q-card class="my-card" @click="navigateToCyclePage">
        <q-img class="top-left-png" src="/src/assets/CycleIcon.png" />
        <q-card-section class="card-content q-py-none">
          <div class="text-h6">ZYKLUS</div>
          <CycleCircle />
          <div class="text-p">
            Erfahre jetzt mehr über deinen Zyklus
            <img class="aligned-svg" src="/src/assets/ForwardArrow.svg" alt="Weiter" />
          </div>
        </q-card-section>
      </q-card>
    </div>

    <!-- Card for Training information -->
    <div class="q-pa-sm">
      <q-card class="my-card" @click="navigateToTrainingPage">
        <q-img class="top-left-png" src="/src/assets/TrainingIcon.png" />
        <q-card-section class="card-content q-py-none">
          <div class="text-h6">TRAINING</div>
          <TrsSunburst />
          <div class="text-p">
            Erfahre jetzt mehr über dein Training
            <img class="aligned-svg" src="/src/assets/ForwardArrow.svg" alt="Weiter" />
          </div>
        </q-card-section>
      </q-card>
    </div>
  </main>
</template>

<script>
import CycleCircle from 'components/CycleCircle.vue';
import TrsSunburst from 'components/TrsSunburst.vue';

export default {
  components: {
    CycleCircle,
    TrsSunburst,
  },
  methods: {
    navigateToTrainingPage() {
      this.$router.push({ name: 'TrsInfoPage' });
    },
    navigateToCyclePage() {
      this.$router.push({ name: 'CycleInfoPage' });
    },
  },
}
</script>

<style scoped>
.card-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  position: relative;
  height: 100vh;
}

.my-card {
  display: flex;
  border-radius: 40px;
  align-items: center;
  justify-content: center;
}

.card-content {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding-bottom: 16px;
  padding-top: 8px;
}

.aligned-svg {
  vertical-align: middle;
  /* Zentriert das SVG-Bild vertikal relativ zum umgebenden Text */
}

.top-left-png {
  position: absolute;
  top: 14px;
  left: 14px;
  max-width: 37px;
  max-height: 37px;
}
</style>
