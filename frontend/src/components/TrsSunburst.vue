<template>
  <main>
    <div class="q-px-md flex flex-center">
      <svg width="250" height="250" viewBox="0 0 42 42" class="donut">
        <!-- <circle class="donut-hole" cx="21" cy="21" r="10" fill="transparent"></circle> -->
        <!-- <circle class="donut-ring" cx="10" cy="10" r="6" fill="000" stroke="#50C1BA" stroke-width="3"></circle> -->
        <!-- 54/ pi = 17,18873385-->
        <circle class="donut-segment-6" cx="21" cy="21" r="17.18873385" fill="transparent" stroke="#9CD3D0"
          stroke-width="3.5" stroke-dasharray="27 81" stroke-dashoffset="0"></circle>

        <circle class="donut-segment-6" cx="21" cy="21" r="17.18873385" fill="transparent" stroke="#50C1BA"
          stroke-width="3.5" stroke-dasharray="27 81" stroke-dashoffset="27"></circle>

        <circle class="donut-segment-6" cx="21" cy="21" r="17.18873385" fill="transparent" stroke="#93EDE8"
          stroke-width="3.5" stroke-dasharray="27 81" stroke-dashoffset="54"></circle>

        <circle class="donut-segment-6" cx="21" cy="21" r="17.18873385" fill="transparent" stroke="#2D8781"
          stroke-width="3.5" stroke-dasharray="27 81" stroke-dashoffset="81"></circle>

        <!-- 43/pi = 13,68732511 -->
        <circle class="donut-segment-5" cx="21" cy="21" r="13.68732511" fill="transparent" stroke="#9CD3D0"
          stroke-width="3" stroke-dasharray="21.5 64.5" stroke-dashoffset="0"></circle>

        <circle class="donut-segment-5" cx="21" cy="21" r="13.68732511" fill="transparent" stroke="#50C1BA"
          stroke-width="3" stroke-dasharray="21.5 64.5" stroke-dashoffset="21.5"></circle>

        <circle class="donut-segment-5" cx="21" cy="21" r="13.68732511" fill="transparent" stroke="#93EDE8"
          stroke-width="3" stroke-dasharray="21.5 64.5" stroke-dashoffset="43"></circle>

        <circle class="donut-segment-5" cx="21" cy="21" r="13.68732511" fill="transparent" stroke="#2D8781"
          stroke-width="3" stroke-dasharray="21.5 64.5" stroke-dashoffset="64.5"></circle>

        <!-- 33,5/pi = 10,66338119 -->
        <circle class="donut-segment-4" cx="21" cy="21" r="10.66338119" fill="transparent" stroke="#9CD3D0"
          stroke-width="2.5" stroke-dasharray="16.75 50.25" stroke-dashoffset="0"></circle>

        <circle class="donut-segment-4" cx="21" cy="21" r="10.66338119" fill="transparent" stroke="#50C1BA"
          stroke-width="2.5" stroke-dasharray="16.75 50.25" stroke-dashoffset="16.75"></circle>

        <circle class="donut-segment-4" cx="21" cy="21" r="10.66338119" fill="transparent" stroke="#93EDE8"
          stroke-width="2.5" stroke-dasharray="16.75 50.25" stroke-dashoffset="33.5"></circle>

        <circle class="donut-segment-4" cx="21" cy="21" r="10.66338119" fill="transparent" stroke="#2D8781"
          stroke-width="2.5" stroke-dasharray="16.75 50.25" stroke-dashoffset="50.25"></circle>

        <!-- 25,5/pi = 8,116902098 -->
        <circle class="donut-segment-3" cx="21" cy="21" r="8.116902098" fill="transparent" stroke="#9CD3D0"
          stroke-width="2" stroke-dasharray="12.75 38.25" stroke-dashoffset="0"></circle>

        <circle class="donut-segment-3" cx="21" cy="21" r="8.116902098" fill="transparent" stroke="#50C1BA"
          stroke-width="2" stroke-dasharray="12.75 38.25" stroke-dashoffset="12.75"></circle>

        <circle class="donut-segment-3" cx="21" cy="21" r="8.116902098" fill="transparent" stroke="#93EDE8"
          stroke-width="2" stroke-dasharray="12.75 38.25" stroke-dashoffset="25.5"></circle>

        <circle class="donut-segment-3" cx="21" cy="21" r="8.116902098" fill="transparent" stroke="#2D8781"
          stroke-width="2" stroke-dasharray="12.75 38.25" stroke-dashoffset="38.25"></circle>

        <!-- 19/pi = 6,047887837 -->
        <circle class="donut-segment-2" cx="21" cy="21" r="6.047887837" fill="transparent" stroke="#9CD3D0"
          stroke-width="1.5" stroke-dasharray="9.5 28.5" stroke-dashoffset="0"></circle>

        <circle class="donut-segment-2" cx="21" cy="21" r="6.047887837" fill="transparent" stroke="#50C1BA"
          stroke-width="1.5" stroke-dasharray="9.5 28.5" stroke-dashoffset="9.5"></circle>

        <circle class="donut-segment-2" cx="21" cy="21" r="6.047887837" fill="transparent" stroke="#93EDE8"
          stroke-width="1.5" stroke-dasharray="9.5 28.5" stroke-dashoffset="19"></circle>

        <circle class="donut-segment-2" cx="21" cy="21" r="6.047887837" fill="transparent" stroke="#2D8781"
          stroke-width="1.5" stroke-dasharray="9.5 28.5" stroke-dashoffset="28.5"></circle>

        <!-- 14/pi = 4,456338407 -->
        <circle class="donut-segment-1" cx="21" cy="21" r="4.456338407" fill="transparent" stroke="#9CD3D0"
          stroke-width="1" stroke-dasharray="7 21" stroke-dashoffset="0"></circle>

        <circle class="donut-segment-1" cx="21" cy="21" r="4.456338407" fill="transparent" stroke="#50C1BA"
          stroke-width="1" stroke-dasharray="7 21" stroke-dashoffset="7"></circle>

        <circle class="donut-segment-1" cx="21" cy="21" r="4.456338407" fill="transparent" stroke="#93EDE8"
          stroke-width="1" stroke-dasharray="7 21" stroke-dashoffset="14"></circle>

        <circle class="donut-segment-1" cx="21" cy="21" r="4.456338407" fill="transparent" stroke="#2D8781"
          stroke-width="1" stroke-dasharray="7 21" stroke-dashoffset="21"></circle>

        <text x="21" y="21" text-anchor="middle" dominant-baseline="middle" font-size="2.5">
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
    return {

    }
  },
  methods: {

  },
  props: {
    score: {
      type: Number,
      default: 0,
      // required: true,
    },
  },
}
</script>
