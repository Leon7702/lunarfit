<template>
  <main>
    <!-- <h5>Zyklus</h5> -->
    <div class="q-pa-md flex flex-center">
      <svg width="250" height="250" viewBox="0 0 42 42" class="donut">
        <!-- <circle class="donut-hole" cx="21" cy="21" r="10" fill="transparent"></circle> -->
        <!-- <circle class="donut-ring" cx="10" cy="10" r="12" fill="transparent" stroke="#50C1BA" stroke-width="3"></circle> -->

        <circle class="donut-segment" cx="21" cy="21" r="15.91549430918954" fill="transparent" stroke="#50C1BA"
          stroke-width="5" stroke-dasharray="20 80" stroke-dashoffset="25" @click="navigateToMenstruationPage"></circle>
        <!-- <text x="20" y="5.5" text-anchor="middle" fill="#fff" dy=".3em" font-size="2"
          transform="rotate(40 21 21)">Menstruation</text> -->
        <circle class="donut-segment" cx="21" cy="21" r="15.91549430918954" fill="transparent" stroke="#9CD3D0"
          stroke-width="5" stroke-dasharray="30 70" stroke-dashoffset="105" @click="navigateToMenstruationPage"></circle>

        <text x="21" y="21" text-anchor="middle" fill="#000" dy=".3em" font-size="3">
        </text>


        <circle class="donut-segment" cx="21" cy="21" r="15.91549430918954" fill="transparent" stroke="#2D8781"
          stroke-width="5" stroke-dasharray="10 90" stroke-dashoffset="75"></circle>

        <text x="20" y="37" text-anchor="middle" fill="#fff" dy=".3em" font-size="2"
          transform="rotate(15 21 21)">Ovulation</text>

        <circle class="donut-segment" cx="21" cy="21" r="15.91549430918954" fill="transparent" stroke="#93EDE8"
          stroke-width="5" stroke-dasharray="40 60" stroke-dashoffset="65"></circle>

          <foreignObject x="-7" y="-7" width="42" height="42">
          <div style="box-shadow: none;">
            <q-knob :min="1" :max="28" v-model="value1" show-value size="24px" :thickness="0.05" color="teal"
              track-color="grey-3" class="q-ma-md" font-size="4px"/>
          </div>
        </foreignObject>

        <text x="21" y="5.5" text-anchor="middle" fill="#fff" dy=".3em" font-size="2"
          transform="rotate(-62 21 21)">Luthealphase</text>

        <path id="myPath" d="M25 6 A15.91549430918954 15 0 0 1 35 15" fill="transparent"></path>

        <text fill="#fff" font-size="2" @click="navigateToMenstruationPage">
          <textPath href="#myPath">
            Menstruation
          </textPath>
        </text>

        <path id="myPath" d="M25 6 A15.91549430918954 15 0 0 1 35 15" fill="transparent"></path>

        <text fill="#fff" font-size="2" transform="rotate(90 21 21)" @click="navigateToMenstruationPage">
          <textPath href="#myPath">
            Follikelphase
          </textPath>
        </text>


      </svg>
    </div>
    <PhaseInformation />

  </main>
</template>

<script>
import PhaseInformation from 'components/PhaseInformation.vue';
import { ref } from 'vue'

export default {
  components: {
    PhaseInformation,
  },
  setup() {
    return {
      value1: ref(5),
    }
  },
  methods: {
    navigateToMenstruationPage() {
      this.$router.push({ name: 'MenstruationInfo' });
    }
  }
}
</script>
