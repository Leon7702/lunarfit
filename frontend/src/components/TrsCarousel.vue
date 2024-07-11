<template>
  <div class="q-px-md">
    <div class="row justify-center">
      <q-btn-toggle class="toggle-border" size="sm" v-model="slide" :options="[
        { label: '1', value: 'training' },
        { label: '2', value: 'mood' },
        { label: '3', value: 'strain' },
        { label: '4', value: 'free' },
        { label: '5', value: 'rest' }
      ]" />
    </div>
    <div class="q-gutter-md">
      <q-carousel v-model="slide" transition-prev="slide-right" transition-next="slide-left" swipeable animated
        control-color="black" padding :style="{ height: '80vh' }">

        <q-carousel-slide name="training" class="column no-wrap flex-center">
          <q-scroll-area class="fit">
            <div class="column no-wrap flex-center">
              <div class="text-h6">{{ $t('training') }}</div>
              <TrsSunburst />
              <div class="text-p">
                <strong>Training Readiness Score: {{ trainingReadinessScore }}%</strong>
              </div>
              <p></p>
              <q-card flat bordered class="my-card">
                <q-card-section>
                  {{ $t(`${trainingTextKey}.description`) }}
                  <ul>
                    <li>{{ $t(`${trainingTextKey}.recommendations[0]`) }}</li>
                    <li>{{ $t(`${trainingTextKey}.recommendations[1]`) }}</li>
                    <li>{{ $t(`${trainingTextKey}.recommendations[2]`) }}</li>
                    <li>{{ $t(`${trainingTextKey}.recommendations[3]`) }}</li>
                  </ul>
                </q-card-section>
                <q-card flat bordered class="my-card">
                  <q-card-section>
                    <div v-if="phaseTextKey">{{ $t(phaseTextKey) }}</div>
                  </q-card-section>
                </q-card>
              </q-card>
            </div>
          </q-scroll-area>
        </q-carousel-slide>

        <q-carousel-slide name="mood" class="column no-wrap flex-center">
          <q-scroll-area class="fit">
            <div class="column no-wrap flex-center">
              <div class="text-h6">{{ $t('mood') }}</div>
              <div class="q-mt-md text-center">
                <q-card flat bordered class="my-card">
                  <q-card-section>
                    <div class="info-text">
                      <strong>{{ $t(`moodInfo.${moodScore}.description`) }}</strong>
                      <div>{{ $t(`moodInfo.${moodScore}.advice`) }}</div>
                    </div>
                  </q-card-section>
                </q-card>
                <div class="q-pa-md">
                  <p>Deine heutige Stimmung:</p>
                  <div class="q-gutter-y-md column justify-center items-center">
                    <q-rating v-model="moodScore" size="2em" :max="6" color="grey" :color-selected="ratingColors"
                      icon="rectangle" readonly />
                  </div>
                </div>
              </div>
            </div>
          </q-scroll-area>
        </q-carousel-slide>

        <q-carousel-slide name="strain" class="column no-wrap flex-center">
          <q-scroll-area class="fit">
            <div class="column no-wrap flex-center">
              <div class="text-h6">{{ $t('strain') }}</div>
              <div class="q-mt-md text-center">
                <q-card flat bordered class="my-card">
                  <q-card-section>
                    <div class="info-text">
                      <strong>{{ $t(`acwrInfo`) }} {{ acwr }}</strong>
                      <div>{{ $t(`strainInfo.${acwrScore}.description`) }}</div>
                      <p></p>
                      <div>{{ $t(`strainInfo.${acwrScore}.recommendations[0]`) }}</div>
                      <div>{{ $t(`strainInfo.${acwrScore}.recommendations[1]`) }}</div>
                      <div>{{ $t(`strainInfo.${acwrScore}.recommendations[2]`) }}</div>
                      <div>{{ $t(`strainInfo.${acwrScore}.recommendations[3]`) }}</div>
                    </div>
                  </q-card-section>
                </q-card>
              </div>
            </div>
          </q-scroll-area>
        </q-carousel-slide>

        <q-carousel-slide name="free" class="column no-wrap flex-center">
          <q-scroll-area class="fit">
            <div class="column no-wrap flex-center">
              <div class="text-h6">{{ $t('free') }}</div>
              <div class="q-mt-md text-center">
                <q-card flat bordered class="my-card">
                  <q-card-section>
                    <div class="info-text">
                      <div>{{ $t(`freeInfo.${freeScore}.description`) }}</div>
                      <p></p>
                      <div>{{ $t(`freeInfo.${freeScore}.recommendations[0]`) }}</div>
                      <div>{{ $t(`freeInfo.${freeScore}.recommendations[1]`) }}</div>
                      <div>{{ $t(`freeInfo.${freeScore}.recommendations[2]`) }}</div>
                      <div>{{ $t(`freeInfo.${freeScore}.recommendations[3]`) }}</div>
                      <div>{{ $t(`freeInfo.${freeScore}.recommendations[4]`) }}</div>
                    </div>
                  </q-card-section>
                </q-card>
                <div class="q-pa-md">
                  <p>Deine heutige Beschwerdefreiheit:</p>
                  <div class="q-gutter-y-md column justify-center items-center">
                    <q-rating v-model="freeScore" size="2em" :max="6" color="grey" :color-selected="ratingColors"
                      icon="rectangle" readonly />
                  </div>
                </div>
              </div>
            </div>
          </q-scroll-area>
        </q-carousel-slide>

        <q-carousel-slide name="rest" class="column no-wrap flex-center">
          <q-scroll-area class="fit">
            <div class="column no-wrap flex-center">
              <div class="text-h6">{{ $t('rest') }}</div>
              <div class="q-mt-md text-center">
                <q-card flat bordered class="my-card">
                  <q-card-section>
                    {{ $t(`restInfo.${restScore}`) }}
                  </q-card-section>
                </q-card>
                <div class="q-pa-md">
                  <p>Deine heutige Erholung:</p>
                  <div class="q-gutter-y-md column justify-center items-center">
                    <q-rating v-model="restScore" size="2em" :max="6" color="grey" :color-selected="ratingColors"
                      icon="rectangle" readonly />
                  </div>
                </div>
              </div>
            </div>
          </q-scroll-area>
        </q-carousel-slide>
      </q-carousel>
    </div>
  </div>
</template>

<script>
import { ref, computed } from 'vue';
import axios from 'axios';
import TrsSunburst from 'components/TrsSunburst.vue';
import { calculateScore } from 'src/utils/scoreCalculator';
import { calculateCycleAndPhases, calculateCurrentDay } from 'src/utils/cyclePhaseCalculator.js';

export default {
  setup() {
    const slide = ref('training');
    const moodScore = ref(0);
    const strainScore = ref(0);
    const freeScore = ref(0);
    const restScore = ref(0);
    const acwr = ref(1.2);
    const trainingReadinessScore = ref(0);

    const cycleLength = ref(null);
    const currentDay = ref(16);

    const phaseTextKey = ref('');

    const mensLengthPortion = ref(null);
    const follicularLengthPortion = ref(null);
    const ovulationLengthPortion = ref(null);
    const earlyLutealLengthPortion = ref(null);
    const lateLutealLengthPortion = ref(null);

    const roundToTwoDecimals = (num) => parseFloat(num.toFixed(2));

    const calculateLengthPortion = (calculatedLengths) => {
      mensLengthPortion.value = (calculatedLengths.phaseLengths[0].length / cycleLength.value) * 100;
      follicularLengthPortion.value = (calculatedLengths.phaseLengths[1].length / cycleLength.value) * 100;
      ovulationLengthPortion.value = (calculatedLengths.phaseLengths[2].length / cycleLength.value) * 100;
      earlyLutealLengthPortion.value = (calculatedLengths.phaseLengths[3].length / cycleLength.value) * 100;
      lateLutealLengthPortion.value = (calculatedLengths.phaseLengths[4].length / cycleLength.value) * 100;
    };

    const fetchData = async () => {
      try {
        const [cycleResponse, trsResponse] = await Promise.all([
          axios.get('http://localhost:3000/menstrualcycle/'),
          axios.get('http://localhost:3000/trsdata')
        ]);

        // Handle cycle data
        const cycleData = cycleResponse.data;
        const calculatedLengths = calculateCycleAndPhases(cycleData);

        cycleLength.value = calculatedLengths.cycleLength;
        calculateLengthPortion(calculatedLengths);

        const today = new Date().toISOString().split('T')[0]; // Use the current date in production
        // const today = "2024-07-26"; // For testing, set a specific date instead of the current date
        currentDay.value = calculateCurrentDay(cycleData.start, today);

        const currentPhase = roundToTwoDecimals((currentDay.value / cycleLength.value) * 100);
        if (currentPhase <= roundToTwoDecimals(mensLengthPortion.value)) {
          phaseTextKey.value = 'menstruationPhaseText';
        } else if (currentPhase <= roundToTwoDecimals(mensLengthPortion.value + follicularLengthPortion.value)) {
          phaseTextKey.value = 'follicularPhaseText';
        } else if (currentPhase <= roundToTwoDecimals(mensLengthPortion.value + follicularLengthPortion.value + ovulationLengthPortion.value)) {
          phaseTextKey.value = 'ovulationPhaseText';
        } else if (currentPhase <= roundToTwoDecimals(mensLengthPortion.value + follicularLengthPortion.value + ovulationLengthPortion.value + earlyLutealLengthPortion.value)) {
          phaseTextKey.value = 'earlyLutealPhaseText';
        } else {
          phaseTextKey.value = 'lateLutealPhaseText';
        }

        // Log the phaseTextKey to ensure it's being set correctly
        console.log('phaseTextKey:', phaseTextKey.value);

        // Handle TRS data
        const trsdata = trsResponse.data;
        moodScore.value = trsdata.mood;
        strainScore.value = trsdata.strain;
        freeScore.value = trsdata.free;
        restScore.value = trsdata.rest;
        acwr.value = trsdata.acwr;
        trainingReadinessScore.value = calculateScore(trsdata); // calculate the trs
      } catch (error) {
        console.error('Failed to fetch data:', error);
      }
    };

    fetchData();

    const acwrScore = computed(() => {
      if (acwr.value < 0.8) return 1;
      if (acwr.value < 1.5) return 2;
      if (acwr.value < 1.8) return 3;
      return 4;
    });

    // Computed property to get the correct training text key based on trainingReadinessScore
    const trainingTextKey = computed(() => {
      if (trainingReadinessScore.value <= 25) return 'scores.1';
      if (trainingReadinessScore.value <= 50) return 'scores.2';
      if (trainingReadinessScore.value <= 75) return 'scores.3';
      return 'scores.4';
    });

    return {
      slide,
      moodScore,
      strainScore,
      freeScore,
      restScore,
      acwr,
      acwrScore,
      trainingReadinessScore,
      trainingTextKey,
      phaseTextKey,
      ratingColors: ['teal-2', 'teal-3', 'teal-4', 'teal-5', 'teal-6', 'teal-7']
    };
  },
  components: {
    TrsSunburst,
  },
};
</script>

<style scoped>
ul {
  padding-left: 15px;
  margin: 0;
}

.border-black {
  border: 1px solid black;
}

.my-card {
  width: 100%;
  max-width: 100vw;
}

.toggle-border {
  border: 1px solid #D9D9D9;
}

.info-text {
  text-align: left;
}
</style>
