<template>
  <div class="row">
    <div class="item icon-container">
      <span class="icon">{{ icon }}</span>
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

<style>
.row {
  display: flex;
  align-items: center;
  border-bottom: 1px solid #ccc;
  padding: 0.625rem 0;
  height: 3.75rem;
}

.item {
  display: flex;
  align-items: center;
  height: 100%;
}

.icon-container {
  flex: 0 0 2.5rem;
  justify-content: center;
}

.text-container {
  flex: 1;
  justify-content: flex-start;
  color: #000;
  font-size: 1rem;
  font-weight: 400;
  line-height: 1.5rem;
  /* 24px */
  padding-left: 0.9375rem;
  /* 15px */
}

.button-container {
  flex: 0 0 5rem;
  /* 80px */
  justify-content: center;
}

.track-button {
  background-color: #50c1ba;
  color: white;
  border: none;
  padding: 0.3125rem 0.625rem;
  /* 5px 10px */
  cursor: pointer;
  border-radius: 0.25rem;
  /* 4px */
}

.track-button:hover {
  background-color: #3b9991;
}

.slider-container {
  display: flex;
  align-items: center;
  flex: 1;
  padding: 0 0.9375rem;
  /* 15px */
  height: 100%;
}

.icon {
  font-size: 1.875rem;
  /* 30px */
}

.text {
  font-size: 1rem;
  /* 16px */
}

.slider {
  flex: 1;
  margin-right: 0.9375rem;
  /* 15px */
  max-height: 2.5rem;
  /* 40px */
}

.cancel-button {
  background-color: #f44336;
  color: white;
  border: none;
  padding: 0.3125rem 0.625rem;
  /* 5px 10px */
  cursor: pointer;
  border-radius: 0.25rem;
  /* 4px */
}

.cancel-button:hover {
  background-color: #d32f2f;
}
</style>
