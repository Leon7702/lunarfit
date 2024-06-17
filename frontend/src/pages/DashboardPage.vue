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
          <svg style="position: absolute; top: -1; left: 10;" width="250" height="250" viewBox="0 0 57 57">
              <!-- Paths for the text labels -->
              <path id="path1" d="M 30,30 m -26,0 a 26,26 0 1,1 52,0 a 26,26 0 1,1 -52,0" fill="transparent" />
              <path id="path2" d="M 30,30 m -26,0 a 26,26 0 1,0 52,0 a 26,26 0 1,0 -52,0" fill="transparent" />

              <!-- Text labels for the segments -->
              <text fill="#000" font-size="3">
                <textPath href="#path1" startOffset="35%">
                  Belastung
                </textPath>
              </text>

              <text fill="#000" font-size="3">
                <textPath href="#path2" startOffset="10%">
                  Erholung
                </textPath>
              </text>

              <text fill="#000" font-size="3">
                <textPath href="#path1" startOffset="8%">
                  Stimmung
                </textPath>
              </text>

              <text fill="#000" font-size="3">
                <textPath href="#path2" startOffset="32%">
                  Beschwerdefreiheit
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
