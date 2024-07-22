<template>
  <div class="q-pa-none">
    <div class="row justify-center">
      <!-- Quasar button toggle component to switch between slides -->
      <q-btn-toggle class="toggle-border" size="sm" v-model="slide" :options="[
        { label: '1', value: 'menstruation' },
        { label: '2', value: 'follicular' },
        { label: '3', value: 'ovulation' },
        { label: '4', value: 'lutealEarly' },
        { label: '5', value: 'lutealLate' }
      ]" />
    </div>
    <div class="q-gutter-md">
      <!-- Quasar carousel component to display in total 4 slides -->
      <q-carousel v-model="slide" transition-prev="slide-right" transition-next="slide-left" swipeable animated
        control-color="black" padding :style="{ height: '80vh' }"
        class="">

        <!-- Carousel slide for menstruation -->
        <q-carousel-slide name="menstruation" class="column no-wrap flex-center">
          <q-scroll-area class="fit">
            <div class="column no-wrap flex-center">
              <div class="text-h6">{{ $t('menstruationInfo.title') }}</div>
              <q-card flat bordered class="my-card">
                <q-card-section>
                  {{ $t('menstruationInfo.description') }}
                </q-card-section>
              </q-card>
              <img class="cycle-image" :src="$t('cyclePhase.images.menstruation')" alt="Menstruation Phase" />
              <PhaseInformation :textNutrition="[
                $t('menstruationInfo.nutrition[0]'),
                $t('menstruationInfo.nutrition[1]'),
                $t('menstruationInfo.nutrition[2]'),
                $t('menstruationInfo.nutrition[3]')
              ]" :textTraining="$t('menstruationInfo.training')"
              :textHealthString1="$t('menstruationInfo.health[0]')" :textHealthArray="[
                $t('menstruationInfo.health[1]'),
                $t('menstruationInfo.health[2]'),
                $t('menstruationInfo.health[3]'),
                $t('menstruationInfo.health[4]'),
                $t('menstruationInfo.health[5]')
              ]" :textHealthString2="$t('menstruationInfo.health[6]')" />
            </div>
          </q-scroll-area>
        </q-carousel-slide>

        <!-- Carousel slide for follicular phase -->
        <q-carousel-slide name="follicular" class="column no-wrap flex-center">
          <q-scroll-area class="fit">
            <div class="column no-wrap flex-center">
              <div class="text-h6">{{ $t('follicularInfo.title') }}</div>
              <q-card flat bordered class="my-card">
                <q-card-section>
                  {{ $t('follicularInfo.description') }}
                </q-card-section>
              </q-card>
              <img class="cycle-image" :src="$t('cyclePhase.images.follicular')" alt="Follicular Phase" />
              <PhaseInformation :textNutrition="[
                $t('follicularInfo.nutrition[0]'),
                $t('follicularInfo.nutrition[1]'),
                $t('follicularInfo.nutrition[2]'),
                $t('follicularInfo.nutrition[3]'),
                $t('follicularInfo.nutrition[4]')
              ]" :textTraining="$t('follicularInfo.training')" :textHealthString1="$t('follicularInfo.health')" />
            </div>
          </q-scroll-area>
        </q-carousel-slide>

        <!-- Carousel slide for ovulation day -->
        <q-carousel-slide name="ovulation" class="column no-wrap flex-center">
          <q-scroll-area class="fit">
            <div class="column no-wrap flex-center">
              <div class="text-h6">{{ $t('ovulationInfo.title') }}</div>
              <q-card flat bordered class="my-card">
                <q-card-section>
                  {{ $t('ovulationInfo.description') }}
                </q-card-section>
              </q-card>
              <img class="cycle-image" :src="$t('cyclePhase.images.ovulation')" alt="Ovulation Phase" />
              <PhaseInformation :textNutrition="[
                $t('ovulationInfo.nutrition[0]'),
                $t('ovulationInfo.nutrition[1]')
              ]" :textTraining="$t('ovulationInfo.training')" :textHealthString1="$t('ovulationInfo.health')" />
            </div>
          </q-scroll-area>
        </q-carousel-slide>

        <!-- Carousel slide for early luteal phase -->
        <q-carousel-slide name="lutealEarly" class="column no-wrap flex-center">
          <q-scroll-area class="fit">
            <div class="column no-wrap flex-center">
              <div class="text-h6">{{ $t('lutealInfoEarly.title') }}</div>
              <q-card flat bordered class="my-card">
                <q-card-section>
                  {{ $t('lutealInfoEarly.description') }}
                </q-card-section>
              </q-card>
              <img class="cycle-image" :src="$t('cyclePhase.images.earlyLuteal')" alt="Early Luteal Phase" />
              <PhaseInformation
                :textNutrition="[
                  $t('lutealInfoEarly.nutrition[0]'),
                  $t('lutealInfoEarly.nutrition[1]'),
                  $t('lutealInfoEarly.nutrition[2]'),
                  $t('lutealInfoEarly.nutrition[3]'),
                  $t('lutealInfoEarly.nutrition[4]'),
                  $t('lutealInfoEarly.nutrition[5]')
                ]"
                :textTraining="$t('lutealInfoEarly.training')" :textHealthString1="$t('lutealInfoEarly.health')" />
            </div>
          </q-scroll-area>
        </q-carousel-slide>

        <!-- Carousel slide for late lutheal phase -->
        <q-carousel-slide name="lutealLate" class="column no-wrap flex-center">
          <q-scroll-area class="fit">
            <div class="column no-wrap flex-center">
              <div class="text-h6">{{ $t('lutealInfoLate.title') }}</div>
              <q-card flat bordered class="my-card">
                <q-card-section>
                  {{ $t('lutealInfoLate.description') }}
                </q-card-section>
              </q-card>
              <img class="cycle-image" :src="$t('cyclePhase.images.lateLuteal')" alt="Late Luteal Phase" />
              <PhaseInformation
                :textNutrition="[
                  $t('lutealInfoLate.nutrition[0]'),
                  $t('lutealInfoLate.nutrition[1]'),
                  $t('lutealInfoLate.nutrition[2]'),
                  $t('lutealInfoLate.nutrition[3]'),
                  $t('lutealInfoLate.nutrition[4]')
                ]"
                :textTraining="$t('lutealInfoLate.training')"
                :textHealthString1="$t('lutealInfoLate.health[0]')" :textHealthArray="[
                $t('lutealInfoLate.health[1]'),
                $t('lutealInfoLate.health[2]'),
                $t('lutealInfoLate.health[3]'),
                $t('lutealInfoLate.health[4]'),
                $t('lutealInfoLate.health[5]')
              ]" :textHealthString2="$t('lutealInfoLate.health[6]')" />
            </div>
          </q-scroll-area>
        </q-carousel-slide>
      </q-carousel>
    </div>
  </div>
</template>


<script>
import axios from 'axios';
import { ref, onMounted } from 'vue';
import PhaseInformation from 'src/components/PhaseInformation.vue';
import { calculateCycleAndPhases, calculateCurrentDay, getCurrentCycle } from 'src/utils/cyclePhaseCalculator.js';

export default {
  setup() {
    const slide = ref('');
    const cycleLength = ref(null);
    const currentDay = ref(16);

    const mensLengthPortion = ref(null);
    const follicularLengthPortion = ref(null);
    const ovulationLengthPortion = ref(null);
    const earlyLutealLengthPortion = ref(null);
    const lateLutealLengthPortion = ref(null);

    const roundToTwoDecimals = (num) => {
      return parseFloat(num.toFixed(2));
    };

    const calculateLengthPortion = (calculatedLengths) => {
      mensLengthPortion.value = (calculatedLengths.phaseLengths[0].length / cycleLength.value) * 100;
      follicularLengthPortion.value = (calculatedLengths.phaseLengths[1].length / cycleLength.value) * 100;
      ovulationLengthPortion.value = (calculatedLengths.phaseLengths[2].length / cycleLength.value) * 100;
      earlyLutealLengthPortion.value = (calculatedLengths.phaseLengths[3].length / cycleLength.value) * 100;
      lateLutealLengthPortion.value = (calculatedLengths.phaseLengths[4].length / cycleLength.value) * 100;
    };

    const fetchData = async () => {
      try {
        const response = await axios.get('http://localhost:3000/cycles/');
        const cycleData = response.data;
        const today = new Date().toISOString().split('T')[0]; // Use the current date in production
        // const today = "2024-07-13"; // For testing, set a specific date instead of the current date
        // const today = "2024-05-05";  // for testing with a specific date - cycle 0
        // const today = "2024-06-09";  // for testing with a specific date - cycle 1
        // const today = "2024-11-11";  // for testing with a specific date - no cycle found

        const currentCycle = getCurrentCycle(cycleData, today);

        if (currentCycle) {
          const calculatedLengths = calculateCycleAndPhases(currentCycle);

          cycleLength.value = calculatedLengths.cycleLength;
          calculateLengthPortion(calculatedLengths);

          currentDay.value = calculateCurrentDay(currentCycle.start, today);

          console.log('Menstruation:', roundToTwoDecimals(mensLengthPortion.value));
          console.log('Follicular:', roundToTwoDecimals(mensLengthPortion.value + follicularLengthPortion.value));
          console.log('Ovulation:', roundToTwoDecimals(mensLengthPortion.value + follicularLengthPortion.value + ovulationLengthPortion.value));
          console.log('Early Luteal:', roundToTwoDecimals(mensLengthPortion.value + follicularLengthPortion.value + ovulationLengthPortion.value + earlyLutealLengthPortion.value));
          console.log('Late Luteal:', roundToTwoDecimals(mensLengthPortion.value + follicularLengthPortion.value + ovulationLengthPortion.value + earlyLutealLengthPortion.value + lateLutealLengthPortion.value));

          // Calculate currentPhase depending on phaseProportion
          const currentPhase = roundToTwoDecimals((currentDay.value / cycleLength.value) * 100);
          console.log('Current Phase:', currentPhase);
          if (currentPhase <= roundToTwoDecimals(mensLengthPortion.value)) {
            slide.value = 'menstruation';
          } else if (currentPhase <= roundToTwoDecimals(mensLengthPortion.value + follicularLengthPortion.value)) {
            slide.value = 'follicular';
          } else if (currentPhase <= roundToTwoDecimals(mensLengthPortion.value + follicularLengthPortion.value + ovulationLengthPortion.value)) {
            slide.value = 'ovulation';
          } else if (currentPhase <= roundToTwoDecimals(mensLengthPortion.value + follicularLengthPortion.value + ovulationLengthPortion.value + earlyLutealLengthPortion.value)) {
            slide.value = 'lutealEarly';
          } else {
            slide.value = 'lutealLate';
          }
          console.log('Selected Slide:', slide.value);
        } else {
          console.error('No cycle found for today\'s date');
        }
      } catch (error) {
        console.error('Failed to fetch data:', error);
      }
    };

    onMounted(() => {
      fetchData();
    });

    return {
      slide,
      mensLengthPortion,
      follicularLengthPortion,
      ovulationLengthPortion,
      earlyLutealLengthPortion,
      lateLutealLengthPortion
    };
  },
  components: {
    PhaseInformation,
  },
};
</script>


<style scoped>

.my-card {
  width: 100%;
  max-width: 100vw;
}

.cycle-image {
  max-width: 100%;
  padding-top: 16px;
}

.toggle-border {
  border: 1px solid #D9D9D9;
}

li {
  margin: 0;
}
</style>
