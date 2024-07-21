<template>
  <div class="size-container">
    <q-btn flat dense round icon="arrow_back" to="/" />
    <CycleCarousel />
  </div>
</template>

<script>
import CycleCarousel from 'components/CycleCarousel.vue';

export default {
  components: {
    CycleCarousel,
  },

}
</script>
