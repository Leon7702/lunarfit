<template>
  <main>
    <div class="q-pa-md flex flex-center">
      <svg width="250" height="250" viewBox="0 0 42 42" class="donut">
        <!-- <circle class="donut-hole" cx="21" cy="21" r="10" fill="transparent"></circle> -->
        <!-- <circle class="donut-ring" cx="10" cy="10" r="6" fill="000" stroke="#50C1BA" stroke-width="3"></circle> -->
        <!-- 54/ pi = 17,18873385-->
        <circle class="donut-segment-out" cx="21" cy="21" r="17.18873385" fill="transparent" stroke="#50C1BA"
          stroke-width="3" stroke-dasharray="27 81" stroke-dashoffset="0"></circle>

        <circle class="donut-segment-out" cx="21" cy="21" r="17.18873385" fill="transparent" stroke="#9CD3D0"
          stroke-width="3" stroke-dasharray="27 81" stroke-dashoffset="27"></circle>

        <circle class="donut-segment-out" cx="21" cy="21" r="17.18873385" fill="transparent" stroke="#2D8781"
          stroke-width="3" stroke-dasharray="27 81" stroke-dashoffset="54"></circle>

        <circle class="donut-segment-out" cx="21" cy="21" r="17.18873385" fill="transparent" stroke="#93EDE8"
          stroke-width="3" stroke-dasharray="27 81" stroke-dashoffset="81"></circle>

        <!-- 44/pi = 14,00563499 -->
        <circle class="donut-segment-mid" cx="21" cy="21" r="14.00563499" fill="transparent" stroke="#50C1BA"
          stroke-width="3" stroke-dasharray="22 66" stroke-dashoffset="0"></circle>

        <circle class="donut-segment-mid" cx="21" cy="21" r="14.00563499" fill="transparent" stroke="#9CD3D0"
          stroke-width="3" stroke-dasharray="22 66" stroke-dashoffset="22"></circle>

        <circle class="donut-segment-mid" cx="21" cy="21" r="14.00563499" fill="transparent" stroke="#2D8781"
          stroke-width="3" stroke-dasharray="22 66" stroke-dashoffset="44"></circle>

        <circle class="donut-segment-mid" cx="21" cy="21" r="14.00563499" fill="transparent" stroke="#93EDE8"
          stroke-width="3" stroke-dasharray="22 66" stroke-dashoffset="66"></circle>

        <!-- 34/pi = 10,82253613 -->
        <circle class="donut-segment-in" cx="21" cy="21" r="10.82253613" fill="transparent" stroke="#50C1BA"
          stroke-width="3" stroke-dasharray="17 51" stroke-dashoffset="0"></circle>

        <circle class="donut-segment-in" cx="21" cy="21" r="10.82253613" fill="transparent" stroke="#9CD3D0"
          stroke-width="3" stroke-dasharray="17 51" stroke-dashoffset="17"></circle>

        <circle class="donut-segment-in" cx="21" cy="21" r="10.82253613" fill="transparent" stroke="#2D8781"
          stroke-width="3" stroke-dasharray="17 51" stroke-dashoffset="34"></circle>

        <circle class="donut-segment-in" cx="21" cy="21" r="10.82253613" fill="transparent" stroke="#93EDE8"
          stroke-width="3" stroke-dasharray="17 51" stroke-dashoffset="51"></circle>
      </svg>
    </div>

  </main>
</template>

<script>
import { ref } from 'vue'

export default {
  setup() {
    return {
      value1: ref(5),
    }
  },
  methods: {

  }
}
</script>
