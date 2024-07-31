<template>
  <main>
    <div class="q-px-md flex flex-center">
      <svg width="240" height="240" viewBox="0 0 42 42" class="donut">

        <!-- Each circle represents a segment of the donut chart -->
        <circle class="donut-segment" cx="21" cy="21" :r="radius" fill="transparent" stroke="#A6EFEB" stroke-width="5"
          :stroke-dasharray="getPhasePortion(mensLengthPortion)" :stroke-dashoffset="(mensOffset + 25)"></circle>

        <circle class="donut-segment" cx="21" cy="21" :r="radius" fill="transparent" stroke="#9CD3D0" stroke-width="5"
          :stroke-dasharray="getPhasePortion(follicularLengthPortion)" :stroke-dashoffset="(follicularOffset + 25)">
        </circle>

        <circle class="donut-segment" cx="21" cy="21" :r="radius" fill="transparent" stroke="#1D706A" stroke-width="5"
          :stroke-dasharray="getPhasePortion(ovulationLengthPortion)" :stroke-dashoffset="(ovulationOffset + 25)">
        </circle>

        <circle class="donut-segment" cx="21" cy="21" :r="radius" fill="transparent" stroke="#2D8781" stroke-width="5"
          :stroke-dasharray="getPhasePortion(earlyLutealLengthPortion)" :stroke-dashoffset="(earlyLutealOffset + 25)">
        </circle>

        <circle class="donut-segment" cx="21" cy="21" :r="radius" fill="transparent" stroke="#50C1BA" stroke-width="5"
          :stroke-dasharray="getPhasePortion(lateLutealLengthPortion)" :stroke-dashoffset="(lateLutealOffset + 25)">
        </circle>

        <!-- Paths for the text labels -->
        <path id="pathMens" d="M21,21 m -15,0 a 15,15 0 1,1 30,0 a 15,15 0 1,1 -30,0" fill="transparent"></path>
        <path id="pathFollicular" d="M21,21 m -16.5,0 a 16.5,16.5 0 1,0 33,0 a 16.5,16.5 0 1,0 -33,0" fill="transparent"></path>
        <path id="pathEarlyLuteal" d="M21,21 m -16.5,0 a 16.5,16.5 0 1,0 33,0 a 16.5,16.5 0 1,0 -33,0" fill="transparent"></path>
        <path id="pathLateLuteal" d="M21,21 m -15,0 a 15,15 0 1,1 30,0 a 15,15 0 1,1 -30,0" fill="transparent"></path>

        <!-- Text labels for the segments -->
        <text fill="#000" font-size="2">
          <!-- <textPath :href="'#pathMens'" startOffset="24"> -->
          <textPath :href="'#pathMens'" :startOffset="`${mensLengthPortion <= 15 ? 24 + Math.round(mensLengthPortion / 5) : 19 + Math.round(mensLengthPortion / 2.5)}`">
            {{ mensLengthPortion < 5 ? '' : mensLengthPortion <= 15 ? $t('mens') : $t('menstruation') }}
          </textPath>
        </text>

        <text fill="#000" font-size="2">
          <!-- <textPath :href="'#pathFollicular'" startOffset="40"> -->
          <textPath :href="'#pathFollicular'" :startOffset="`${30 + Math.round(follicularLengthPortion / 5)}`">
            {{ follicularLengthPortion < 5 ? '' : follicularLengthPortion <= 15 ? $t('follicular') : $t('follicularPhase') }}
          </textPath>
        </text>

        <text fill="#fff" font-size="2" >
          <!-- <textPath :href="'#pathEarlyLuteal'" startOffset="0"> -->
          <textPath :href="'#pathEarlyLuteal'" :startOffset="`${earlyLutealLengthPortion <= 30 ? 0 : -4 + Math.round(earlyLutealLengthPortion / 5)}`">
            {{ earlyLutealLengthPortion < 5 ? '' : earlyLutealLengthPortion <= 30 ? $t('earlyLuteal') : $t('earlyLutealPhase') }}
          </textPath>
        </text>

        <text fill="#fff" font-size="2">
          <!-- <textPath :href="'#pathLateLuteal'" startOffset="12"> -->
          <textPath :href="'#pathLateLuteal'" :startOffset="`${lateLutealLengthPortion <= 20 ? 14 - Math.round(lateLutealLengthPortion / 5) : 18 - Math.round(lateLutealLengthPortion / 2.5)}`">
            {{ lateLutealLengthPortion < 5 ? '' : lateLutealLengthPortion <= 20 ? $t('lateLuteal') : $t('lateLutealPhase') }}
          </textPath>
        </text>

        <!-- displays the current day of the cycle -->
        <circle v-if="dataLoaded" class="donut-segment" cx="21" cy="21" :r="radius" fill="transparent" stroke="#E0E0E0" stroke-width="0.8"
          stroke-dasharray="100" style="transform: scale(0.75); transform-origin: center">
        </circle>

        <circle v-if="dataLoaded" class="donut-segment" cx="21" cy="21" :r="radius" fill="transparent" stroke="#009688" stroke-width="0.8"
          :stroke-dasharray="getDayPortion()" :stroke-dashoffset="25" style="transform: scale(0.75); transform-origin: center">
        </circle>

        <text v-if="dataLoaded" x="21" y="21" text-anchor="middle" dominant-baseline="middle" font-size="2.5" fill="#000">
          <tspan x="21" dy="-0.4em">{{ $t('cycleDay') }}</tspan>
          <tspan x="21" dy="1.2em">{{ currentDay }}</tspan>
        </text>

      </svg>
    </div>

  </main>
</template>

<script>
import { api } from 'src/boot/axios';
import { ref, onMounted, computed, watch } from 'vue';
import { calculateCycleAndPhases, calculateCurrentDay, getCurrentCycle } from 'src/utils/cyclePhaseCalculator.js';

export default {
  setup() {
    // FIXME: cycleLength gets calculated by the cyclePhaseCalculator
    const cycleLength = ref(null);
    // TODO: needs to get or calculate the current day of the cycle
    const currentDay = ref(1);
    const dataLoaded = ref(false);  // Add a flag to indicate data loading status
    const radius = ref(50 / Math.PI);

    const mensLengthPortion = ref(null);
    const follicularLengthPortion = ref(null);
    const ovulationLengthPortion = ref(null);
    const earlyLutealLengthPortion = ref(null);
    const lateLutealLengthPortion = ref(null);

    const mensOffset = ref(0);

    const getPhasePortion = (phaseLengthPortion) => {
      // "" + phaseLengthPortion + " " + (100 - phaseLengthPortion).toString()
      return `${phaseLengthPortion} ${100 - phaseLengthPortion}`;
    };

    const getDayPortion = () => {
      let percentage = (currentDay.value / cycleLength.value) * 100
      return `${percentage} ${100 - percentage}`;
    };

    const calculateLengthPortion = (calculatedLengths) => {
      mensLengthPortion.value = (calculatedLengths.phaseLengths[0].length / cycleLength.value) * 100;
      follicularLengthPortion.value = (calculatedLengths.phaseLengths[1].length / cycleLength.value) * 100;
      ovulationLengthPortion.value = (calculatedLengths.phaseLengths[2].length / cycleLength.value) * 100;
      earlyLutealLengthPortion.value = (calculatedLengths.phaseLengths[3].length / cycleLength.value) * 100;
      lateLutealLengthPortion.value = (calculatedLengths.phaseLengths[4].length / cycleLength.value) * 100;
    };

    // Fetches the cycle data and determines the current cycle
    const fetchData = async () => {
      try {
        const response = await api.get('/cycles/');
        const cycleData = response.data;
        console.log('Fetched cycle data:', cycleData);
        const today = new Date().toISOString().split('T')[0];
        // const today = "2024-08-20";  // for testing with a specific date
        // const today = "2024-05-05";  // for testing with a specific date - cycle 0
        // const today = "2024-06-09";  // for testing with a specific date - cycle 1
        // const today = "2024-11-11";  // for testing with a specific date - no cycle found

        const cycles = cycleData.results;

        if (Array.isArray(cycles)) {
          const currentCycle = getCurrentCycle(cycles, today);

          if(currentCycle) {
            const calculatedLengths = calculateCycleAndPhases(currentCycle);

            cycleLength.value = calculatedLengths.cycleLength;
            console.log('Calculated cycle length:', cycleLength.value);
            calculateLengthPortion(calculatedLengths);

            currentDay.value = calculateCurrentDay(currentCycle.start, today);
          } else {
            console.error('No cycle found for today\'s date');
          }

          dataLoaded.value = true;  // Set the flag to true when data is loaded
        } else {
          console.error('Cycle data is not an array:', cycleData);
        }
      } catch (error) {
        console.error('Failed to fetch data:', error);
      }
    };

    console.log('Initial currentDay:', currentDay.value);

    onMounted(() => {
      console.log('Mounted currentDay:', currentDay.value);
      fetchData();
    });

    watch(currentDay, (newValue) => {
      console.log('currentDay updated to:', newValue);
    });


    const follicularOffset = computed(() => mensOffset.value - mensLengthPortion.value);
    const ovulationOffset = computed(() => follicularOffset.value - follicularLengthPortion.value);
    const earlyLutealOffset = computed(() => ovulationOffset.value - ovulationLengthPortion.value);
    const lateLutealOffset = computed(() => earlyLutealOffset.value - earlyLutealLengthPortion.value);

    return {
      cycleLength,
      currentDay,
      dataLoaded,
      radius,
      mensLengthPortion,
      follicularLengthPortion,
      ovulationLengthPortion,
      earlyLutealLengthPortion,
      lateLutealLengthPortion,
      mensOffset,
      getPhasePortion,
      getDayPortion,
      follicularOffset,
      ovulationOffset,
      earlyLutealOffset,
      lateLutealOffset,
    };
  }
};
</script>
