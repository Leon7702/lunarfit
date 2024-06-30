<template>
  <main>
    <div class="q-px-md flex flex-center">
      <svg width="240" height="240" viewBox="0 0 42 42" class="donut">

        <!-- Each circle represents a segment of the donut chart -->
        <!-- The stroke-dasharray property controls the length and spacing of the dashes, creating the donut effect -->
        <!-- The stroke-dashoffset property controls where the dash pattern starts -->
        <!-- TODO: calculate stroke dasharray based on proportion values -->
        <!-- TODO: determine stroke-dashoffset value -> always staring at 25 for mensPhase -->
        <circle class="donut-segment" cx="21" cy="21" :r="radius" fill="transparent" stroke="#50C1BA" stroke-width="5"
          :stroke-dasharray="calculatePhasePortion(mensLengthPortion)" :stroke-dashoffset="(mensOffset + 25)"></circle>

        <circle class="donut-segment" cx="21" cy="21" :r="radius" fill="transparent" stroke="#9CD3D0" stroke-width="5"
          :stroke-dasharray="calculatePhasePortion(follicularLengthPortion)" :stroke-dashoffset="(follicularOffset + 25)">
        </circle>

        <circle class="donut-segment" cx="21" cy="21" :r="radius" fill="transparent" stroke="#2D8781" stroke-width="5"
          :stroke-dasharray="calculatePhasePortion(earlyLutealLengthPortion)" :stroke-dashoffset="(earlyLutealOffset + 25)">
        </circle>

        <circle class="donut-segment" cx="21" cy="21" :r="radius" fill="transparent" stroke="#93EDE8" stroke-width="5"
          :stroke-dasharray="calculatePhasePortion(lateLutealLengthPortion)" :stroke-dashoffset="(lateLutealOffset + 25)">
        </circle>

        <!-- Paths for the text labels -->
        <path id="myPath1" d="M25 6 A15.91549430918954 15 0 0 1 35 15" fill="transparent"></path>
        <!-- <path id="myPath5" d="M32.5 33 A15.91549430918954 15 0 0 0 5 10" fill="transparent"></path> Follikelphase alt -->
        <path id="myPath2" d="M25 5 A15.91549430918954 15 0 0 0 9 10" fill="transparent"></path>
        <path id="myPath3" d="M22 6 A15.91549430918954 15 0 0 1 35 15" fill="transparent"></path>
        <path id="myPath4" d="M25 5 A15.91549430918954 15 0 0 0 9 10" fill="transparent"></path>

        <!-- Text labels for the segments -->
        <!-- The textPath element allows the text to follow the path defined above -->
        <text fill="#fff" font-size="2">
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

        <text fill="#000" font-size="2" transform="rotate(292 21 21)">
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
import { computed } from 'vue';

export default {
  data() {
    return {
      // FIXME: this data needs to be fetched from the actual database, onboarding or user input
      cycleLength: null,
      currentDay: 1, // needs to be initialized with a number (not null)
      radius: 50 / Math.PI,

      // TODO: need to create methods to calculate the portion of each phase
      // we need: cycleLength, mensLength, follicularLength, earlyLutealLength, lateLutealLength
      // mensLengthPortion: 11.8,
      // follicularLengthPortion: 47.1,
      // earlyLutealLengthPortion: 27.5,
      // lateLutealLengthPortion: 13.7,

      // for cycleLength = 28
      mensLengthPortion: 21.4,
      follicularLengthPortion: 28.6,
      earlyLutealLengthPortion: 32.1,
      lateLutealLengthPortion: 17.9,

      mensOffset: 0,
    };
  },
  // Fetch the data from the database when the component is created
  created() {
    this.fetchData();
  },
  methods: {

    // mensLengthPortion (100 - mensLengthPortion)
    calculatePhasePortion(phaseLengthPortion) {
      return "" + phaseLengthPortion + " " + (100 - phaseLengthPortion).toString();
    },

    async fetchData() {
      // TODO: Fetch the data from the database and assign it to cycleLength and currentDay
      // FOR NOW: to test the method without having a real database, use json-server
      try {
        const response = await axios.get('http://localhost:3000/usersdata/'); // TODO: change the URL
        this.cycleLength = response.data.cycleLength;
        this.currentDay = response.data.currentDay;
      } catch (error) {
        console.error('Failed to fetch data:', error);
      }
    },
  },
  computed: {
    follicularOffset() {
      return this.mensOffset - this.mensLengthPortion;
    },
    earlyLutealOffset() {
      return this.follicularOffset - this.follicularLengthPortion;
    },
    lateLutealOffset() {
      return this.earlyLutealOffset - this.earlyLutealLengthPortion;
    }
  }
};
</script>
