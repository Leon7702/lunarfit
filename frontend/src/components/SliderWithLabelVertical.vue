<template>
  <div class="slider-container">
    <div class="slider-labels">
      <div v-for="i in 7" :key="i" class="label">
        <span>{{ 6 - (i - 1) }}</span>
      </div>
    </div>
    <q-slider
      v-model="model"
      :min="0"
      :max="6"
      color="grey-4"
      track-size="40px"
      thumb-color="black"
      thumb-size="0px"
      markers
      vertical
      class="custom-slider"
    />
    <div class="slider-labels-right">
      <div v-for="i in 7" :key="i" class="label">
        <span v-if="i === 1">{{ textAtTop }}</span>
        <span v-if="i === 7">{{ textAtBottom }}</span>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, watch } from 'vue';

export default {
  props: {
    topText: String,
    bottomText: String,
    modelValue: Number
  },
  setup(props, { emit }) {
    const model = ref(props.modelValue || 0);

    watch(model, (newValue) => {
      emit('update:modelValue', newValue);
    });

    return {
      model,
      textAtTop: props.topText,
      textAtBottom: props.bottomText
    };
  }
};
</script>

<style scoped>
.slider-container {
    display: flex;
    align-items: center;
    position: relative;
    margin: auto;
    height: 300px;
    width: 70px;
}

.slider-labels {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    margin-right: 8px;
    height: 100%;
    justify-content: space-between;
}

.label {
    font-size: 14px;
}

.custom-slider {
    height: 100%;
}

::v-deep .custom-slider .q-slider__track {
    background: linear-gradient(to top, rgb(92, 205, 92), rgb(252, 252, 111), rgb(249, 81, 81));
}

.slider-labels-right {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    margin-left: 8px;
    height: 100%;
    justify-content: space-between;
}
</style>
