<template>
  <main>
    <div class="q-px-md flex flex-center">
      <!-- SVG element for the donut chart -->
      <svg width="250" height="250" viewBox="0 0 42 42" class="donut">
        <!-- Loop over each segment in the segments array -->
        <circle v-for="(segment, index) in segments"
                :key="'segment-' + index"
                :class="'donut-segment-' + segment.level"
                cx="21"
                cy="21"
                :r="segment.radius"
                fill="transparent"
                :stroke="segment.color"
                :stroke-width="segment.strokeWidth"
                :stroke-dasharray="segment.dasharray"
                :stroke-dashoffset="segment.dashoffset"
                :style="{ opacity: segment.opacity }"></circle>
        <!-- Text element for displaying the score in the middle of the donut chart -->
        <text x="21" y="21" text-anchor="middle" dominant-baseline="middle" font-size="2.5" transform="rotate(90, 21, 21)">
          {{ Math.round(score) }} %
        </text>
      </svg>
    </div>
  </main>
</template>

<script>
import { ref } from 'vue'

export default {
  setup() {
    const trsdata = {
      strain: 4,
      mood: 5,
      rest: 6,
      free: 5
    };

    // Colors for the different segments of the donut chart
    const colors = {
      strain: "#50C1BA", // 1. Quadrant
      mood: "#93EDE8", // 2. Quadrant
      rest: "#2D8781", // 3. Quadrant
      free: "#9CD3D0" // 4. Quadrant
    };

    // Array of radius levels for the segments of the donut chart
    const radiusLevels = [4.456338407, 6.047887837, 8.116902098, 10.66338119, 13.68732511, 17.18873385];

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

    return {
      score: ref(0),
      segments
    };
  }
}
</script>

<style scoped>
.donut {
  transform: rotate(-90deg);
}
</style>
