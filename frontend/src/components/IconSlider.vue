<template>
  <div class="row">
    <div class="item icon-container">
      <img :src="icon" alt="Icon" class="icon">
    </div>
    <div class="item text-container" v-if="!showSlider">
      <span class="text">{{ text }}</span>
    </div>
    <div class="item button-container" v-if="!showSlider">
      <button @click="toggleSlider" class="track-button">{{ $t('track') }}</button>
    </div>
    <div class="item slider-container" v-if="showSlider">
      <q-slider v-model="localValue" :min="1" :max="6" markers marker-labels class="slider" />
      <button @click="cancelTracking" class="cancel-button">{{ $t('cancel') }}</button>
    </div>
  </div>
</template>



<script>
export default {
  name: 'IconSlider',
  props: {
    icon: {
      type: String,
      required: true
    },
    text: {
      type: String,
      required: true
    },
    value: {
      type: Number,
      default: 1
    }
  },
  data() {
    return {
      showSlider: false,
      localValue: this.value,
      originalValue: this.value
    };
  },
  watch: {
    value(newVal) {
      this.localValue = newVal;
      this.originalValue = newVal;
    },
    localValue(newVal) {
      this.$emit('update:value', newVal);
    }
  },
  methods: {
    toggleSlider() {
      this.showSlider = !this.showSlider;
    },
    cancelTracking() {
      this.showSlider = false;
      this.localValue = this.originalValue;
    }
  }
};
</script>

<style scoped>
.row {
  display: flex;
  align-items: center;
  border-bottom: 1px solid #ccc;
  padding: 10px 0;
  height: 60px;
  /* Fixed height for the row */
}

.item {
  display: flex;
  align-items: center;
  height: 100%;
  /* Ensure items fill the row height */
}

.icon-container {
  flex: 0 0 40px;
  /* Fixed width for the icon container */
  justify-content: center;
}

.text-container {
  flex: 1;
  /* Allow text to take the remaining space */
  justify-content: flex-start;
  color: #000;
  font-size: 16px;
  font-style: normal;
  font-weight: 400;
  line-height: 24px;
  /* 150% */
  padding-left: 15px;
  /* Adjust padding to ensure consistent space */
}

.button-container {
  flex: 0 0 80px;
  /* Fixed width for the button container */
  justify-content: center;
}

.track-button {
  background-color: #50c1ba;
  color: white;
  border: none;
  padding: 5px 10px;
  cursor: pointer;
  border-radius: 4px;
}

.track-button:hover {
  background-color: #3b9991;
}

.slider-container {
  display: flex;
  align-items: center;
  flex: 1;
  /* Allow slider to take the remaining space */
  padding: 0 15px;
  /* Add padding for better spacing */
  height: 100%;
  /* Ensure slider-container fills the row height */
}

.icon {
  width: 30px;
  height: 30px;
}

.text {
  font-size: 16px;
}

.slider {
  flex: 1;
  margin-right: 15px;
  /* Space between slider and button */
  max-height: 40px;
  /* Ensure slider does not exceed a certain height */
}

.cancel-button {
  background-color: #f44336;
  color: white;
  border: none;
  padding: 5px 10px;
  cursor: pointer;
  border-radius: 4px;
}

.cancel-button:hover {
  background-color: #d32f2f;
}
</style>
