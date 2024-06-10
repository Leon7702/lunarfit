<template>
    <div class="q-pa-md" style="max-width: 500px" >
      <q-input
        v-model="text"
        filled
        type="textarea"
      />
    </div>
  </template>
  
  <script>
  import { ref } from 'vue'
  
  export default {
    setup () {
      return {
        text: ref('')
      }
    }
  }
  </script>
  <style scoped>
  .q-pa-md {
    padding: 0;
    padding-bottom: 5px;
  }
  
  ::v-deep .custom-textarea .q-field {
    width: 100%;
  }
  </style>
