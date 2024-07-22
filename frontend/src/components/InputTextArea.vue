<template>
  <div class="q-pa-md" style="max-width: 500px">
    <q-input
      v-model="internalValue"
      filled
      type="textarea"
    />
  </div>
</template>

<script>
import { ref, watch } from 'vue';

export default {
  props: {
    modelValue: {
      type: String,
      required: true
    }
  },
  setup(props, { emit }) {
    const internalValue = ref(props.modelValue);

    watch(internalValue, (newValue) => {
      emit('update:modelValue', newValue);
    });

    watch(() => props.modelValue, (newValue) => {
      internalValue.value = newValue;
    });

    return {
      internalValue
    };
  }
};
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
