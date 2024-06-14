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
          <div style="position: relative;">
          <TrsSunburst />
          <!-- Add your SVG paths and text labels here -->
          <svg style="position: absolute; top: -15; left: 0;" viewBox="0 0 40 40">
            <!-- Paths for the text labels -->
            <path id="myPath1" d="M25 6 A15.91549430918954 15 0 0 1 35 15" fill="transparent"></path>
            <path id="myPath2" d="M32.5 33 A15.91549430918954 15 0 0 0 5 10" fill="transparent"></path>

            <!-- Text labels for the segments -->
            <!-- The textPath element allows the text to follow the path defined above -->
            <text fill="#000" font-size="1.8" transform="rotate(10 21 21)">
              <textPath href="#myPath1">
                Belastung
              </textPath>
            </text>

            <text fill="#000" font-size="1.8" transform="rotate(20 21 21)">
              <textPath href="#myPath2">
                Beschwerdefreiheit
              </textPath>
            </text>

            <text fill="#000" font-size="1.8" transform="rotate(105 21 21)">
              <textPath href="#myPath2">
                Erholung
              </textPath>
            </text>

            <text fill="#000" font-size="1.8" transform="rotate(280 21 21)">
              <textPath href="#myPath1">
                Stimmung
              </textPath>
            </text>
          </svg>
        </div>
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
