<template>
  <main>
    <!-- <h5>Zyklus</h5> -->
    <div class="q-pa-md flex flex-center">
      <svg width="250" height="250" viewBox="0 0 42 42" class="donut">
        <!-- <circle class="donut-hole" cx="21" cy="21" r="10" fill="#000"></circle> -->
        <!-- <circle class="donut-ring" cx="10" cy="10" r="12" fill="transparent" stroke="#50C1BA" stroke-width="3"></circle> -->

        <circle class="donut-segment" cx="21" cy="21" r="15.91549430918954" fill="transparent" stroke="#ce4b99"
          stroke-width="5" stroke-dasharray="20 80" stroke-dashoffset="25" @click="navigateToMenstruationPage"></circle>
        <!-- <text x="20" y="5.5" text-anchor="middle" fill="#fff" dy=".3em" font-size="2"
          transform="rotate(40 21 21)">Menstruation</text> -->
        <circle class="donut-segment" cx="21" cy="21" r="15.91549430918954" fill="transparent" stroke="#000"
          stroke-width="5" stroke-dasharray="30 70" stroke-dashoffset="105"></circle>
        <text x="21" y="21" text-anchor="middle" fill="#000" dy=".3em" font-size="3">Zyklustag 5</text>

        <circle class="donut-segment" cx="21" cy="21" r="15.91549430918954" fill="transparent" stroke="#377bbc"
          stroke-width="5" stroke-dasharray="10 90" stroke-dashoffset="75"></circle>

        <text x="20" y="37" text-anchor="middle" fill="#fff" dy=".3em" font-size="2"
          transform="rotate(15 21 21)">Ovulation</text>

        <circle class="donut-segment" cx="21" cy="21" r="15.91549430918954" fill="transparent" stroke="#50C1BA"
          stroke-width="5" stroke-dasharray="40 60" stroke-dashoffset="65"></circle>

        <text x="21" y="5.5" text-anchor="middle" fill="#fff" dy=".3em" font-size="2"
          transform="rotate(-62 21 21)">Luthealphase</text>

        <path id="myPath" d="M25 6 A15.91549430918954 15 0 0 1 35 15" fill="transparent"></path>

        <text fill="#fff" font-size="2" @click="navigateToMenstruationPage">
          <textPath href="#myPath">
            Menstruation
          </textPath>
        </text>

        <path id="myPath" d="M25 6 A15.91549430918954 15 0 0 1 35 15" fill="transparent"></path>

        <text fill="#fff" font-size="2" transform="rotate(90 21 21)">
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
export default {
  components: {
    PhaseInformation,
  },
  setup() {
    return {
      value: 20
    }
  },
  methods: {
    navigateToMenstruationPage() {
      this.$router.push({ name: 'MenstruationInfo' });
    }
  }
}
</script>
