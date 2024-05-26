<template>
  <main>
    <!-- <h5>Zyklus</h5> -->
    <CycleCircle />
    <PhaseInformation />

  </main>
</template>

<script>
import CycleCircle from 'components/CycleCircle.vue';
import PhaseInformation from 'components/PhaseInformation.vue';

export default {
  components: {
    CycleCircle,
    PhaseInformation,
  },
  setup() {
    return {

    }
  },
}
</script>
