<template>
    <div class="q-pa-md">
      <div class="q-gutter-sm">
        <q-checkbox
          v-model="customModel"
          color="secondary"
          label="Es gab Störfaktoren, welche die Temperatur beeinflussen könnten."
          true-value="yes"
          false-value="no"
          class="custom-checkbox"
        />
      </div>
    </div>
  </template>
  
  <script>
  import { ref } from 'vue'
  
  export default {
    setup () {
      return {
        customModel: ref('no')
      }
    }
  }
  </script>
  
  <style scoped>
  .q-pa-md {
    padding: 0;
    padding-bottom: 5px;
  }
  
  ::v-deep .q-checkbox__label {
    margin-left: 5px; 
  }
  </style>
  