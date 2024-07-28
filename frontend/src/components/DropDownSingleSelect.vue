<template>
  <div class="dropdown-container">
    <q-select 
      filled 
      v-model="localModel" 
      :options="selectOptions" 
      @update:model-value="updateValue"
    />
  </div>
</template>

<script>
import { ref, watch } from 'vue'

export default {
  name: 'DropDownSingleSelect',
  props: {
    options: {
      type: Array,
      required: true
    },
    modelValue: {
      type: [String, Number, Object],
      default: null
    }
  },
  setup(props, { emit }) {
    const localModel = ref(props.modelValue)

    const updateValue = (value) => {
      localModel.value = value
      emit('update:modelValue', value)
    }

    watch(() => props.modelValue, (newValue) => {
      localModel.value = newValue
    })

    return {
      localModel,
      selectOptions: props.options,
      updateValue
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
