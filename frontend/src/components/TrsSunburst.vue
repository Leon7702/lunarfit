<template>
  <main>
    <div class="q-px-md flex flex-center">
      <!-- SVG element for the donut chart -->
      <svg width="250" height="250" viewBox="0 0 42 42" class="donut">
        <!-- Loop over each segment in the segments array -->
        <circle v-for="(segment, index) in segments" :key="'segment-' + index" :class="'donut-segment-' + segment.level"
          cx="21" cy="21" :r="segment.radius" fill="transparent" :stroke="segment.color"
          :stroke-width="segment.strokeWidth" :stroke-dasharray="segment.dasharray"
          :stroke-dashoffset="segment.dashoffset" :style="{ opacity: segment.opacity }"></circle>
        <!-- Text element for displaying the score in the middle of the donut chart -->
        <text x="21" y="21" text-anchor="middle" dominant-baseline="middle" font-size="2.5"
          transform="rotate(90, 21, 21)">
          {{ Math.round(score) }} %
        </text>
      </svg>
    </div>
  </main>
</template>

<script>
import { ref } from 'vue';
import axios from 'axios';

export default {
  // TODO: 1. Fetch data from the API (for now using mock database data)
  //       2. Populate 'trsdata' with the fetched data
  //       3. Recalculate the segments
  //       2. Calculate the score based on the fetched data
  data() {
    return {
      // TODO: Score should be calculated based on the fetched data!!
      score: 76,
      segments: [],

      // FIXME: this data needs to be fetched from the actual database, should get this from assessment
      strain: null,
      mood: null,
      rest: null,
      free: null,
    };
  },
  async created() {
    await this.fetchData();
  },
  methods: {
    async fetchData() {
      // TODO: Fetch the data from the database and assign it to strain, mood, rest, and free
      // FOR NOW: to test the method without having a real database, direct to db.json file and put in terminal: json-server --watch db.json --port 8000
      // then use curl: curl -X GET http://localhost:8000/trsdata/
      try {
        const response = await axios.get('http://localhost:8000/trsdata');
        const trsdata = {
          strain: response.data.strain,
          mood: response.data.mood,
          rest: response.data.rest,
          free: response.data.free
        };

        this.updateSegments(trsdata);
      } catch (error) {
        console.error('Failed to fetch data:', error);
      }
    },
    updateSegments(trsdata) {
      // Colors for the different segments of the donut chart
      const colors = {
        strain: "#50C1BA", // 1. Quadrant
        mood: "#93EDE8", // 2. Quadrant
        rest: "#2D8781", // 3. Quadrant
        free: "#9CD3D0" // 4. Quadrant
      };

      // Array of radius levels for the segments of the donut chart
      const radiusLevels = [4.456338407, 6.047887837, 8.116902098, 10.66338119, 13.68732511, 17.18873385];
      // 14, 19, 25.5, 33.5, 43, 54 divided by pi

      // const multipliedByPi = radiusLevels.map(value => value * Math.PI);
      // console.log(multipliedByPi);

      // Array of stroke widths for the segments of the donut chart
      const strokeWidths = [1, 1.5, 2, 2.5, 3, 3.5];

      // Array of dasharray objects for the segments of the donut chart
      const dasharrays = [
        { dash: 7, gap: 21 },
        { dash: 9.5, gap: 28.5 },
        { dash: 12.75, gap: 38.25 },
        { dash: 16.75, gap: 50.25 },
        { dash: 21.5, gap: 64.5 },
        { dash: 27, gap: 81 }
      ];

      // Array to hold the segment objects
      const segments = [];

      // Calculate the opacity of a segment based on its level
      const calculateOpacity = (maxLevel, currentLevel) => {
        return currentLevel <= maxLevel ? 1 : 0.2;
      };

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
            color: colors[key],
            strokeWidth: strokeWidths[j],
            dasharray: `${d.dash} ${d.gap}`, // Dash array for the segment stroke
            dashoffset: d.dash * i,
            opacity: calculateOpacity(level, j + 1)
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
