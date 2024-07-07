<template>
  <div class="size-container">
    <!-- TODO: Change size of the cards, because needs to fit with the toolbar in one screen. -->
    <div class="card-container">
      <!-- Card for Cycle information -->
      <div class="q-pa-sm q-pt-lg">
        <q-card class="my-card" @click="navigateToCyclePage">
          <q-img class="top-left-png" src="/src/assets/CycleIcon.png" />
          <q-card-section class="card-content q-py-none">
            <div class="text-h6">{{ $t('cycleTitle') }}</div>
            <CycleCircle />
            <div class="more-text">
              {{ $t('moreCycleInfo') }}
              <img class="aligned-svg" src="/src/assets/ForwardArrow.svg" alt="Weiter" />
            </div>
          </q-card-section>
          <div>
            <q-btn class="top-right-button" fab1 flat round icon="info" color="grey-5" @click="openLegendDialog" />
            <q-dialog v-model="legend">
              <q-card style="width: 240px">
                <q-card-section>
                  <div class="text-h6">Zyklusphasen</div>
                </q-card-section>

                <q-card-section class="q-pt-none">
                  <div style="display: flex; align-items: center;">
                    <q-avatar size="xs" style="background-color: #A6EFEB;"></q-avatar>
                    <p style="margin: 10px;">I. Menstruation</p>
                  </div>
                  <div style="display: flex; align-items: center;">
                    <q-avatar size="xs" style="background-color: #9CD3D0;"></q-avatar>
                    <p style="margin: 10px;">II. Follikelphase</p>
                  </div>
                  <div style="display: flex; align-items: center;">
                    <q-avatar size="xs" style="background-color: #1D706A;"></q-avatar>
                    <p style="margin: 10px;">III. Ovulation</p>
                  </div>
                  <div style="display: flex; align-items: center;">
                    <q-avatar size="xs" style="background-color: #2D8781;"></q-avatar>
                    <p style="margin: 10px;">IV. frühe Lutealphase</p>
                  </div>
                  <div style="display: flex; align-items: center;">
                    <q-avatar size="xs" style="background-color: #50C1BA;"></q-avatar>
                    <p style="margin: 10px;">V. späte Lutealphase</p>
                  </div>
                </q-card-section>

                <q-card-actions align="right">
                  <q-btn flat label="OK" color="primary" v-close-popup />
                </q-card-actions>
              </q-card>
            </q-dialog>
          </div>
        </q-card>
      </div>

      <!-- Card for Training information -->
      <div class="q-pa-sm">
        <q-card class="my-card" @click="navigateToTrainingPage">
          <q-img class="top-left-png" src="/src/assets/TrainingIcon.png" />
          <q-card-section class="card-content q-py-none">
            <div class="text-h6">{{ $t('trainingTitle') }}</div>
            <div style="position: relative;">
              <TrsSunburst />
              <div class="browser-svg-container">
                <!-- Add your SVG paths and text labels here -->
                <svg width="240" height="240" viewBox="0 0 57 57">
                  <!-- Paths for the text labels -->
                  <path id="path1" d="M 30,30 m -26,0 a 26,26 0 1,1 52,0 a 26,26 0 1,1 -52,0" fill="transparent" />
                  <path id="path2" d="M 30,30 m -26,0 a 26,26 0 1,0 52,0 a 26,26 0 1,0 -52,0" fill="transparent" />

                  <!-- Text labels for the segments -->
                  <text fill="#000" font-size="3">
                    <textPath href="#path1" startOffset="35%">
                      {{ $t('strain') }}
                    </textPath>
                  </text>

                  <text fill="#000" font-size="3">
                    <textPath href="#path2" startOffset="10%">
                      {{ $t('rest') }}
                    </textPath>
                  </text>

                  <text fill="#000" font-size="3">
                    <textPath href="#path1" startOffset="8%">
                      {{ $t('mood') }}
                    </textPath>
                  </text>

                  <text fill="#000" font-size="3">
                    <textPath href="#path2" startOffset="32%">
                      {{ $t('free') }}
                    </textPath>
                  </text>
                </svg>
              </div>
            </div>
            <div class="more-text">
              {{ $t('moreTrainingInfo') }}
              <img class="aligned-svg" src="/src/assets/ForwardArrow.svg" alt="Weiter" />
            </div>
          </q-card-section>
        </q-card>
      </div>
    </div>
  </div>
</template>

<script>
import CycleCircle from 'components/CycleCircle.vue';
import TrsSunburst from 'components/TrsSunburst.vue';
import { ref } from 'vue';

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
    openLegendDialog(event) {
      event.stopPropagation();
      this.legend = true;
    }
  },
  setup() {
    const legend = ref(false);

    return {
      legend
    };
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
  padding-bottom: 8px;
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

.top-right-button {
  position: absolute;
  top: 8px;
  right: 8px;
}

.more-text {
  padding-left: 1.2rem;
}

/* Browser-specific styles */
.browser-svg-container {
  position: absolute;
  top: 0;
  left: 10px;
}
</style>
