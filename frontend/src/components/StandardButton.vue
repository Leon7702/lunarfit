<template>
    <div class="q-pa-md q-gutter-sm">
      <q-btn :label="label" style="background: #50C1BA; color: white" />
    </div>
  </template>
  
  <script>
  export default {
    name: 'StandardButton',
    props: {
      label: {
        type: String,
        required: true
      }
    }
  };
  </script>
  
  <style scoped>
  /* ggf. zusätzliche Stile hinzufügen */
  </style>
  