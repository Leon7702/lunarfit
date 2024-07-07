<template>
  <main>
    <div class="q-px-md flex flex-center">
      <svg width="240" height="240" viewBox="0 0 42 42" class="donut">

        <!-- Each circle represents a segment of the donut chart -->
        <!-- The stroke-dasharray property controls the length and spacing of the dashes, creating the donut effect -->
        <!-- The stroke-dashoffset property controls where the dash pattern starts -->
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
          <textPath :href="'#pathMens'" startOffset="25%">
            Menstruation
          </textPath>
        </text>

        <text fill="#000" font-size="2">
          <textPath :href="'#pathFollicular'" startOffset="35%">
            {{ $t('follicularInfo.title') }}
          </textPath>
        </text>

        <text fill="#fff" font-size="2">
          <textPath :href="'#pathEarlyLuteal'" startOffset="0%">
            frühe Lutealphase
          </textPath>
        </text>

        <text fill="#fff" font-size="2">
          <textPath :href="'#pathLateLuteal'" startOffset="12%">
            späte Luteal
          </textPath>
        </text>

        <!-- displays the current day of the cycle -->
        <foreignObject x="-7" y="-7" width="42" height="42">
          <div style="box-shadow: none;">
            <q-knob v-if="dataLoaded" readonly :step="1" :min="0.5" :max="cycleLength" v-model="currentDay" show-value
              size="24px" :thickness="0.05" color="teal" track-color="grey-3" class="q-ma-md" font-size="4px">
              <div style="display: flex; flex-direction: column; align-items: center; justify-content: center;">
                <p style="font-size: 3px; margin: 1px;"></p>
                <p style="font-size: 2.5px; margin: 0;">{{ $t('cycleDay') }}</p>
                <p style="font-size: 3px; margin: 0;">{{ currentDay }}</p>
              </div>
            </q-knob>
          </div>
        </foreignObject>
      </svg>
    </div>

  </main>
</template>

<script>
import axios from 'axios';
import { ref, onMounted, computed, watch } from 'vue';
import { calculateCycleAndPhases, calculateCurrentDay } from 'src/utils/cyclePhaseCalculator.js';

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

    const calculateLengthPortion = (calculatedLengths) => {
      mensLengthPortion.value = (calculatedLengths.phaseLengths[0].length / cycleLength.value) * 100;
      follicularLengthPortion.value = (calculatedLengths.phaseLengths[1].length / cycleLength.value) * 100;
      ovulationLengthPortion.value = (calculatedLengths.phaseLengths[2].length / cycleLength.value) * 100;
      earlyLutealLengthPortion.value = (calculatedLengths.phaseLengths[3].length / cycleLength.value) * 100;
      lateLutealLengthPortion.value = (calculatedLengths.phaseLengths[4].length / cycleLength.value) * 100;
    };

    const fetchData = async () => {
      try {
        const response = await axios.get('http://localhost:3000/menstrualcycle/');
        const cycleData = response.data;
        console.log('Fetched cycle data:', cycleData);
        const calculatedLengths = calculateCycleAndPhases(cycleData);

        cycleLength.value = calculatedLengths.cycleLength;
        console.log('Calculated cycle length:', cycleLength.value);
        calculateLengthPortion(calculatedLengths);

        // const today = "2024-07-10";  // for testing with a specific date
        const today = new Date().toISOString().split('T')[0];
        currentDay.value = calculateCurrentDay(cycleData.start, today);

        dataLoaded.value = true;  // Set the flag to true when data is loaded
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
      follicularOffset,
      ovulationOffset,
      earlyLutealOffset,
      lateLutealOffset,
    };
  }
};
</script>
