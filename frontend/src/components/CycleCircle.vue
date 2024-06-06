<template>
  <main>
    <div class="q-px-md flex flex-center">
      <svg width="250" height="250" viewBox="0 0 42 42" class="donut">

        <!-- Each circle represents a segment of the donut chart -->
        <!-- The stroke-dasharray property controls the length and spacing of the dashes, creating the donut effect -->
        <!-- The stroke-dashoffset property controls where the dash pattern starts -->
        <circle class="donut-segment" cx="21" cy="21" r="15.91549430918954" fill="transparent" stroke="#50C1BA"
          stroke-width="5" stroke-dasharray="20 80" stroke-dashoffset="25"></circle>

        <circle class="donut-segment" cx="21" cy="21" r="15.91549430918954" fill="transparent" stroke="#9CD3D0"
          stroke-width="5" stroke-dasharray="30 70" stroke-dashoffset="105"></circle>

        <circle class="donut-segment" cx="21" cy="21" r="15.91549430918954" fill="transparent" stroke="#2D8781"
          stroke-width="5" stroke-dasharray="10 90" stroke-dashoffset="75"></circle>

        <circle class="donut-segment" cx="21" cy="21" r="15.91549430918954" fill="transparent" stroke="#93EDE8"
          stroke-width="5" stroke-dasharray="40 60" stroke-dashoffset="65"></circle>

        <!-- Paths for the text labels -->
        <path id="myPath1" d="M25 6 A15.91549430918954 15 0 0 1 35 15" fill="transparent"></path>
        <path id="myPath2" d="M33 32 A15.91549430918954 15 0 0 0 5 10" fill="transparent"></path>

        <!-- Text labels for the segments -->
        <!-- The textPath element allows the text to follow the path defined above -->
        <text fill="#fff" font-size="2">
          <textPath href="#myPath1">
            Menstruation
          </textPath>
        </text>

        <text fill="#fff" font-size="2" transform="rotate(15 21 21)">
          <textPath href="#myPath2">
            Follikelphase
          </textPath>
        </text>

        <text fill="#fff" font-size="2" transform="rotate(80 21 21)">
          <textPath href="#myPath2">
            Ovulation
          </textPath>
        </text>

        <text fill="#fff" font-size="2" transform="rotate(255 21 21)">
          <textPath href="#myPath1">
            Luthealphase
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
            <q-knob :step="1" :min="1" :max="cycleLength" v-model="currentDay" show-value size="24px" :thickness="0.05" color="teal"
              track-color="grey-3" class="q-ma-md" font-size="4px" />
          </div>
        </foreignObject>
      </svg>
    </div>

  </main>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      // TODO: this data needs to be fetched from the database, onboarding or user input
      cycleLength: null,
      currentDay: null,
    };
  },
  // Fetch the data from the database when the component is created
  created() {
    this.fetchData();
  },
  methods: {
    async fetchData() {
      // Fetch the data from the database and assign it to cycleLength and currentDay
      try {
        const response = await axios.get('http://localhost:8000/usersdata/'); // TODO: change the URL
        this.cycleLength = response.data.cycleLength;
        this.currentDay = response.data.currentDay;
      } catch (error) {
        console.error('Failed to fetch data:', error);
      }
    },
  },
};
</script>
