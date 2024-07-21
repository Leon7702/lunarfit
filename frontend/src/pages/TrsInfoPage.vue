<template>
  <div class="size-container">
    <q-btn flat dense round icon="arrow_back" to="/" />
    <TrsCarousel />
  </div>
</template>

<script>
import TrsCarousel from 'components/TrsCarousel.vue';

export default {
  components: {
    TrsCarousel,

  },
}
</script>
