<template>
  <main class="card-container">
    <div class="q-pa-md row items-start q-gutter-md">
      <q-card class="my-card" @click="navigateToCyclePage">
        <q-card-section class="card-content">
          <div class="text-h6">ZYKLUS</div>
          <CycleCircle />
          <div class="text-p">
            Erfahre jetzt mehr über deinen Zyklus
            <img class="aligned-svg" src="/src/assets/ForwardArrow.svg" alt="Weiter" />
          </div>
        </q-card-section>
      </q-card>
    </div>

    <div class="q-pa-md row items-start q-gutter-md">
      <q-card class="my-card" @click="navigateToTrainingPage">
        <q-card-section class="card-content">
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
  setup() {
    return {

    }
  },
  methods: {
    navigateToTrainingPage() {
      this.$router.push({ name: 'TrainingInfoPage' });
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
  /* width: 324px;
  height: 318px; */
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
}

.aligned-svg {
  vertical-align: middle;
  /* Zentriert das SVG-Bild vertikal relativ zum umgebenden Text */
}
</style>
