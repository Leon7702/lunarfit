<template>
  <main>
    <div class="q-px-md flex flex-center">
      <!-- SVG element for the donut chart -->
      <svg width="240" height="240" viewBox="0 0 42 42" class="donut">
        <!-- Loop over each segment in the segments array -->
        <circle v-for="(segment, index) in segments" :key="'segment-' + index" :class="'donut-segment-' + segment.level"
          cx="21" cy="21" :r="segment.radius" fill="transparent" :stroke="segment.color"
          :stroke-width="segment.strokeWidth" :stroke-dasharray="segment.dasharray"
          :stroke-dashoffset="segment.dashoffset" :style="{ opacity: segment.opacity }"></circle>
        <!-- Text element for displaying the score in the middle of the donut chart -->
        <text x="21" y="21" text-anchor="middle" dominant-baseline="middle" font-size="2.2" font-weight="bold"
          transform="rotate(90, 21, 21)">
          {{ Math.round(score) }}%
        </text>
      </svg>
    </div>
  </main>
</template>

<script>
import { ref } from 'vue';
import axios from 'axios';
import { calculateScore } from 'src/utils/scoreCalculator';

export default {
  // TODO: 1. Fetch data from the API (for now use test database data)
  //       2. Calculate the score based on the fetched data
  data() {
    return {
      score: 0,
      segments: [],

      // FIXME: this data needs to be fetched from the actual database, should get this from assessment
      trs_acwr: null,
      mood: null,
      recovery: null,
      complaints: null,
    };
  },
  async created() {
    await this.fetchData();
  },
  methods: {
    async fetchData() {
      // TODO: Fetch the data from the database and assign it to trs_acwr, mood, recovery, and complaints
      // FOR NOW: to test the method without having a real database, use json-server
      try {
        const response = await axios.get('http://localhost:3000/trs?user_id=1');
        const today = new Date().toISOString().split("T")[0];
        // const today = "2024-07-23"; // For testing, set a specific date instead of the current date
        const todayData = response.data.find((entry) => entry.day === today);

        let trsdata;
        if (todayData) {
          trsdata = {
            trs_acwr: todayData.trs_acwr,
            mood: todayData.mood,
            recovery: todayData.recovery,
            complaints: todayData.complaints
          };
          this.score = calculateScore(trsdata);
        } else {
          console.log('No data available for today');
          trsdata = {
            trs_acwr: 0,
            mood: 0,
            recovery: 0,
            complaints: 0
          };
          this.score = 0;
        }

        this.updateSegments(trsdata);
      } catch (error) {
        console.error('Failed to fetch data:', error);
      }
    },
    updateSegments(trsdata) {
      // Colors for the different segments of the donut chart
      const colors = {
        trs_acwr: "#50C1BA", // 1. Quadrant
        mood: "#A6EFEB", // 2. Quadrant
        recovery: "#2D8781", // 3. Quadrant
        complaints: "#9CD3D0" // 4. Quadrant
      };

      const greyColors = {
        trs_acwr: "#E0E0E0", // 1. Quadrant unused
        mood: "#EDEDED", // 2. Quadrant unused
        recovery: "#E0E0E0", // 3. Quadrant unused
        complaints: "#EDEDED" // 4. Quadrant unused
      };

      // Array of radius levels for the segments of the donut chart
      const radiusLevels = [3.183098862, 4.774648293, 6.843662553, 9.390141642, 12.41408556, 15.91549431];
      // 14, 19, 25.5, 33.5, 43, 54 divided by pi
      // new: 10, 15, 21.5, 29.5, 39, 50 divided by pi

      // const multipliedByPi = radiusLevels.map(value => value * Math.PI);
      // console.log(multipliedByPi);

      // Array of stroke widths for the segments of the donut chart
      const strokeWidths = [1, 1.5, 2, 2.5, 3, 3.5];

      // Array of dasharray objects for the segments of the donut chart
      const dasharrays = [
        { dash: 5, gap: 15 },
        { dash: 7.5, gap: 22.5 },
        { dash: 10.75, gap: 32.25 },
        { dash: 14.75, gap: 44.25 },
        { dash: 19.5, gap: 58.5 },
        { dash: 25, gap: 75 }
      ];

      // Array to hold the segment objects
      const segments = [];

      // Loop over each key in the trsdata object
      Object.keys(trsdata).forEach((key, i) => {
        // Get the level for the current key
        const level = trsdata[key];

        // Loop over each dasharray object
        dasharrays.forEach((d, j) => {
          // Push a new segment object to the segments array
          segments.push({
            level: j + 1,
            radius: radiusLevels[j],
            color: level >= j + 1 ? colors[key] : greyColors[key],
            strokeWidth: strokeWidths[j],
            dasharray: `${d.dash} ${d.gap}`, // Dash array for the segment stroke
            dashoffset: d.dash * i,
          });
        });
      });
      this.segments = segments;
    }
  },
}
</script>

<style scoped>
.donut {
  transform: rotate(-90deg);
}
</style>
