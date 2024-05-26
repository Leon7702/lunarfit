<template>
  <main>
    <div class="q-pa-md flex flex-center">
      <svg width="250" height="250" viewBox="0 0 42 42" class="donut">
        <!-- <circle class="donut-hole" cx="21" cy="21" r="10" fill="transparent"></circle> -->
        <!-- <circle class="donut-ring" cx="10" cy="10" r="6" fill="000" stroke="#50C1BA" stroke-width="3"></circle> -->
        <!-- 54/ pi = 17,18873385-->
        <circle class="donut-segment-out" cx="21" cy="21" r="17.18873385" fill="transparent"
          :stroke="segmentStates[0] ? '#50C1BA' : '#D9D9D9'" stroke-width="3" stroke-dasharray="27 81"
          stroke-dashoffset="0" @click="toggleSegment(0)"></circle>

        <circle class="donut-segment-out" cx="21" cy="21" r="17.18873385" fill="transparent"
          :stroke="segmentStates[1] ? '#9CD3D0' : '#D9D9D9'" stroke-width="3" stroke-dasharray="27 81"
          stroke-dashoffset="27" @click="toggleSegment(1)"></circle>

        <circle class="donut-segment-out" cx="21" cy="21" r="17.18873385" fill="transparent"
          :stroke="segmentStates[2] ? '#2D8781' : '#D9D9D9'" stroke-width="3" stroke-dasharray="27 81"
          stroke-dashoffset="54" @click="toggleSegment(2)"></circle>

        <circle class="donut-segment-out" cx="21" cy="21" r="17.18873385" fill="transparent"
          :stroke="segmentStates[3] ? '#93EDE8' : '#D9D9D9'" stroke-width="3" stroke-dasharray="27 81"
          stroke-dashoffset="81" @click="toggleSegment(3)"></circle>

        <!-- 44/pi = 14,00563499 -->
        <circle class="donut-segment-mid" cx="21" cy="21" r="14.00563499" fill="transparent"
          :stroke="segmentStates[4] ? '#50C1BA' : '#D9D9D9'" stroke-width="3" stroke-dasharray="22 66"
          stroke-dashoffset="0" @click="toggleSegment(4)"></circle>

        <circle class="donut-segment-mid" cx="21" cy="21" r="14.00563499" fill="transparent"
          :stroke="segmentStates[5] ? '#9CD3D0' : '#D9D9D9'" stroke-width="3" stroke-dasharray="22 66"
          stroke-dashoffset="22" @click="toggleSegment(5)"></circle>

        <circle class="donut-segment-mid" cx="21" cy="21" r="14.00563499" fill="transparent"
          :stroke="segmentStates[6] ? '#2D8781' : '#D9D9D9'" stroke-width="3" stroke-dasharray="22 66"
          stroke-dashoffset="44" @click="toggleSegment(6)"></circle>

        <circle class="donut-segment-mid" cx="21" cy="21" r="14.00563499" fill="transparent"
          :stroke="segmentStates[7] ? '#93EDE8' : '#D9D9D9'" stroke-width="3" stroke-dasharray="22 66"
          stroke-dashoffset="66" @click="toggleSegment(7)"></circle>

        <!-- 34/pi = 10,82253613 -->
        <circle class="donut-segment-in" cx="21" cy="21" r="10.82253613" fill="transparent"
          :stroke="segmentStates[8] ? '#50C1BA' : '#D9D9D9'" stroke-width="3" stroke-dasharray="17 51"
          stroke-dashoffset="0" @click="toggleSegment(8)"></circle>

        <circle class="donut-segment-in" cx="21" cy="21" r="10.82253613" fill="transparent"
          :stroke="segmentStates[9] ? '#9CD3D0' : '#D9D9D9'" stroke-width="3" stroke-dasharray="17 51"
          stroke-dashoffset="17" @click="toggleSegment(9)"></circle>

        <circle class="donut-segment-in" cx="21" cy="21" r="10.82253613" fill="transparent"
          :stroke="segmentStates[10] ? '#2D8781' : '#D9D9D9'" stroke-width="3" stroke-dasharray="17 51"
          stroke-dashoffset="34" @click="toggleSegment(10)"></circle>

        <circle class="donut-segment-in" cx="21" cy="21" r="10.82253613" fill="transparent"
          :stroke="segmentStates[11] ? '#93EDE8' : '#D9D9D9'" stroke-width="3" stroke-dasharray="17 51"
          stroke-dashoffset="51" @click="toggleSegment(11)"></circle>

        <text x="21" y="21" text-anchor="middle" dominant-baseline="middle" font-size="3">
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
    const score = ref(0)
    const segmentStates = ref([false, false, false, false, false, false, false, false, false, false, false, false]) // Zustand für jedes Segment

    const incrementScore = () => {
      score.value += 25 / 3
      if (score.value > 100) {
        score.value = 100
      }
    }

    const toggleSegment = (index) => {
      segmentStates.value[index] = !segmentStates.value[index]
      incrementScore()
    }

    return {
      score,
      segmentStates,
      toggleSegment
    }
  }
}
</script>
