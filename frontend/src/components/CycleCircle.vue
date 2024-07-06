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
import { calculateCycleAndPhases } from 'src/utils/cyclePhaseCalculator.js';

export default {
  data() {
    return {
      // FIXME: cycleLength gets calculated by the cyclePhaseCalculator
      cycleLength: 34,
      // TODO: needs to get or calculate the current day of the cycle
      currentDay: 20,
      radius: 50 / Math.PI,
      mensLengthPortion: null,
      follicularLengthPortion: null,
      ovulationLengthPortion: null,
      earlyLutealLengthPortion: null,
      lateLutealLengthPortion: null,

      mensOffset: 0,
    };
  },
  // Fetch the data from the database when the component is created
  created() {
    this.fetchData();
  },
  methods: {

    // mensLengthPortion (100 - mensLengthPortion)
    getPhasePortion(phaseLengthPortion) {
      return "" + phaseLengthPortion + " " + (100 - phaseLengthPortion).toString();
    },


    calculateLengthPortion(calculatedLengths) {
      this.mensLengthPortion = (calculatedLengths.phaseLengths[0].length / this.cycleLength) * 100;
      this.follicularLengthPortion = (calculatedLengths.phaseLengths[1].length / this.cycleLength) * 100;
      this.ovulationLengthPortion = (calculatedLengths.phaseLengths[2].length / this.cycleLength) * 100;
      this.earlyLutealLengthPortion = (calculatedLengths.phaseLengths[3].length / this.cycleLength) * 100;
      this.lateLutealLengthPortion = (calculatedLengths.phaseLengths[4].length / this.cycleLength) * 100;
    },

    async fetchData() {
      // TODO: Fetch the data from the database and assign it to cycleData
      try {
        const response = await axios.get('http://localhost:3000/menstrualcycle/'); // TODO: change the URL
        const cycleData = response.data;
        const calculatedLengths = calculateCycleAndPhases(cycleData);

        this.cycleLength = calculatedLengths.cycleLength;
        this.calculateLengthPortion(calculatedLengths);
      } catch (error) {
        console.error('Failed to fetch data:', error);
      }
    },
  },
  computed: {
    follicularOffset() {
      return this.mensOffset - this.mensLengthPortion;
    },
    ovulationOffset() {
      return this.follicularOffset - this.follicularLengthPortion;
    },
    earlyLutealOffset() {
      return this.ovulationOffset - this.ovulationLengthPortion;
    },
    lateLutealOffset() {
      return this.earlyLutealOffset - this.earlyLutealLengthPortion;
    }
  }
};
</script>
