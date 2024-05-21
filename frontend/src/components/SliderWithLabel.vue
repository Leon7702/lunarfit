<template>
  <div class="q-px-lg q-pt-md q-pb-xl">
    <q-slider
      v-model="model"
      marker-labels
      :min="1"
      :max="6"
    />
  </div>
</template>

<script>
import { ref } from 'vue'

export default {
  setup () {
    const model = ref(1)

    return {
      model
    }
  }
}
</script>