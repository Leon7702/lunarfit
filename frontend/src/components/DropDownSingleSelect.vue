<template>
    <div class="dropdown-container">
      <q-select filled v-model="model" :options="selectOptions" />
    </div>
  </template>
  
  <script>
  import { ref } from 'vue'
  
  export default {
    name: 'DropDownSingleSelect',
    props: {
      options: {
        type: Array,
        required: true
      }
    },
    setup(props) {
      const model = ref(null)
      return {
        model,
        selectOptions: props.options
      }
    }
  }
  </script>
  
  <style scoped>
  .dropdown-container {
    width: 100%; 
  }
  .q-select {
    width: 100%;
  }
  .q-pa-md {
    padding-top: 5px;
    padding-left: 5px;
    padding-right: 5px;
  }
  </style>
