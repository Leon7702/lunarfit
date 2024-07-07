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
        <path id="myPath1" d="M25 6 A15.91549430918954 15 0 0 1 35 15" fill="transparent"></path>
        <!-- <path id="myPath5" d="M32.5 33 A15.91549430918954 15 0 0 0 5 10" fill="transparent"></path> Follikelphase alt -->
        <path id="myPath2" d="M25 5 A15.91549430918954 15 0 0 0 9 10" fill="transparent"></path>
        <path id="myPath3" d="M22 6 A15.91549430918954 15 0 0 1 35 15" fill="transparent"></path>
        <path id="myPath4" d="M25 5 A15.91549430918954 15 0 0 0 9 10" fill="transparent"></path>

        <!-- Text labels for the segments -->
        <!-- The textPath element allows the text to follow the path defined above -->
        <text fill="#000" font-size="2">
          <textPath href="#myPath1">
            {{ $t('menstruationInfo.title') }}
          </textPath>
        </text>

        <text fill="#000" font-size="2" transform="rotate(130 21 21)">
          <textPath href="#myPath2">
            {{ $t('follicularInfo.title') }}
          </textPath>
        </text>

        <text fill="#fff" font-size="2" transform="rotate(245 21 21)">
          <textPath href="#myPath4">
            {{ $t('lutealInfoEarly.title') }}
          </textPath>
        </text>

        <text fill="#fff" font-size="2" transform="rotate(292 21 21)">
          <textPath href="#myPath3">
            {{ $t('lutealInfoLate.title') }}
          </textPath>
        </text>


        <!-- <text x="20" y="5.5" text-anchor="middle" fill="#fff" dy=".3em" font-size="2"
          transform="rotate(40 21 21)">Menstruation</text> -->

        <!-- <text x="20" y="37" text-anchor="middle" fill="#fff" dy=".3em" font-size="2"
          transform="rotate(15 21 21)">Ovulation</text> -->

        <!-- <text x="21" y="5.5" text-anchor="middle" fill="#fff" dy=".3em" font-size="2"
          transform="rotate(-62 21 21)">Luthealphase</text> -->

        <!-- displays the current day of the cycle -->
        <foreignObject x="-7" y="-7" width="42" height="42">
          <div style="box-shadow: none;">
            <q-knob readonly :step="1" :min="1" :max="cycleLength" v-model="currentDay" show-value size="24px"
              :thickness="0.05" color="teal" track-color="grey-3" class="q-ma-md" font-size="4px">
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
import { ref, onMounted, computed } from 'vue';
import { calculateCycleAndPhases } from 'src/utils/cyclePhaseCalculator.js';

export default {
  setup() {
    // FIXME: cycleLength gets calculated by the cyclePhaseCalculator
    const cycleLength = ref(34);
    // TODO: needs to get or calculate the current day of the cycle
    const currentDay = ref(20);
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
        const calculatedLengths = calculateCycleAndPhases(cycleData);

        cycleLength.value = calculatedLengths.cycleLength;
        calculateLengthPortion(calculatedLengths);
      } catch (error) {
        console.error('Failed to fetch data:', error);
      }
    };

    onMounted(() => {
      fetchData();
    });

    const follicularOffset = computed(() => mensOffset.value - mensLengthPortion.value);
    const ovulationOffset = computed(() => follicularOffset.value - follicularLengthPortion.value);
    const earlyLutealOffset = computed(() => ovulationOffset.value - ovulationLengthPortion.value);
    const lateLutealOffset = computed(() => earlyLutealOffset.value - earlyLutealLengthPortion.value);

    return {
      cycleLength,
      currentDay,
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
