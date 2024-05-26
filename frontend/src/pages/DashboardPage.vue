<template>
  <main>
    <!-- <h5>Zyklus</h5> -->
    <CycleCircle />
    <PhaseInformation />
    <TrsSunburst />
    <p>hallo</p>
  </main>
</template>

<script>
import CycleCircle from 'components/CycleCircle.vue';
import PhaseInformation from 'components/PhaseInformation.vue';
import TrsSunburst from 'components/TrsSunburst.vue';

export default {
  components: {
    CycleCircle,
    PhaseInformation,
    TrsSunburst,
  },
  setup() {
    return {

    }
  },
}
</script>

