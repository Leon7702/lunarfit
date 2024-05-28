<template>
  <main>
    <div class="q-pa-md flex flex-center">
      <svg width="250" height="250" viewBox="0 0 42 42" class="donut">
        <!-- <circle class="donut-hole" cx="21" cy="21" r="10" fill="transparent"></circle> -->
        <!-- <circle class="donut-ring" cx="10" cy="10" r="6" fill="000" stroke="#50C1BA" stroke-width="3"></circle> -->
        <!-- 54/ pi = 17,18873385-->
        <circle class="donut-segment-out" cx="21" cy="21" r="17.18873385" fill="transparent" stroke="#50C1BA"
          stroke-width="3" stroke-dasharray="27 81" stroke-dashoffset="0" @click="incrementScore"></circle>

        <circle class="donut-segment-out" cx="21" cy="21" r="17.18873385" fill="transparent" stroke="#9CD3D0"
          stroke-width="3" stroke-dasharray="27 81" stroke-dashoffset="27" @click="incrementScore"></circle>

        <circle class="donut-segment-out" cx="21" cy="21" r="17.18873385" fill="transparent" stroke="#2D8781"
          stroke-width="3" stroke-dasharray="27 81" stroke-dashoffset="54" @click="incrementScore"></circle>

        <circle class="donut-segment-out" cx="21" cy="21" r="17.18873385" fill="transparent" stroke="#93EDE8"
          stroke-width="3" stroke-dasharray="27 81" stroke-dashoffset="81" @click="incrementScore"></circle>

        <!-- 44/pi = 14,00563499 -->
        <circle class="donut-segment-mid" cx="21" cy="21" r="14.00563499" fill="transparent" stroke="#50C1BA"
          stroke-width="3" stroke-dasharray="22 66" stroke-dashoffset="0" @click="incrementScore"></circle>

        <circle class="donut-segment-mid" cx="21" cy="21" r="14.00563499" fill="transparent" stroke="#9CD3D0"
          stroke-width="3" stroke-dasharray="22 66" stroke-dashoffset="22" @click="incrementScore"></circle>

        <circle class="donut-segment-mid" cx="21" cy="21" r="14.00563499" fill="transparent" stroke="#2D8781"
          stroke-width="3" stroke-dasharray="22 66" stroke-dashoffset="44" @click="incrementScore"></circle>

        <circle class="donut-segment-mid" cx="21" cy="21" r="14.00563499" fill="transparent" stroke="#93EDE8"
          stroke-width="3" stroke-dasharray="22 66" stroke-dashoffset="66" @click="incrementScore"></circle>

        <!-- 34/pi = 10,82253613 -->
        <circle class="donut-segment-in" cx="21" cy="21" r="10.82253613" fill="transparent" stroke="#50C1BA"
          stroke-width="3" stroke-dasharray="17 51" stroke-dashoffset="0" @click="incrementScore"></circle>

        <circle class="donut-segment-in" cx="21" cy="21" r="10.82253613" fill="transparent" stroke="#9CD3D0"
          stroke-width="3" stroke-dasharray="17 51" stroke-dashoffset="17" @click="incrementScore"></circle>

        <circle class="donut-segment-in" cx="21" cy="21" r="10.82253613" fill="transparent" stroke="#2D8781"
          stroke-width="3" stroke-dasharray="17 51" stroke-dashoffset="34" @click="incrementScore"></circle>

        <circle class="donut-segment-in" cx="21" cy="21" r="10.82253613" fill="transparent" stroke="#93EDE8"
          stroke-width="3" stroke-dasharray="17 51" stroke-dashoffset="51" @click="incrementScore"></circle>

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

    const incrementScore = () => {
      score.value += 25/3
      if (score.value > 100) {
        score.value = 100
      }
    }

    return {
      score,
      incrementScore
    }
  }
}
</script>
