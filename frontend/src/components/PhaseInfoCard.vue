<template>
  <q-card flat bordered class="my-card">
    <q-card-section>
      <div class="text-p text-center">{{ title }}</div>
    </q-card-section>

    <q-card-section>
      {{ text }}
    </q-card-section>
  </q-card>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
      required: true
    },
    text: {
      type: String,
      required: true
    }
  }
}
</script>

<style scoped>
/* Add your styles here */
</style>
