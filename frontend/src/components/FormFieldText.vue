<template>
    <div class="q-pa-md">
      <div class="q-gutter-y-md column" style="max-width: 300px">
        <q-input color="teal" filled v-model="text" :label="label">
          <template v-slot:prepend>
            <q-icon :name="iconName" />
          </template>
        </q-input>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'FormFieldText',
    props: {
      label: {
        type: String,
        default: 'Label'
      },
      iconName: {
        type: String,
        default: 'event'
      },
      value: {
        type: String,
        default: ''
      }
    },
    data() {
      return {
        text: this.value
      };
    }
  };
  </script>
  
  <style scoped>
  /* ggf. zusätzliche Styles */
  </style>
  