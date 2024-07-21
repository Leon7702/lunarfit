<template>
  <q-card class="q-pa-none q-mb-xs q-mt-xs" style="height: 60px; display: flex; align-items: center;">
    <q-card-section class="row no-wrap q-gutter-sm q-px-none items-center" style="width: 100%;">
      <q-avatar size="40px" class="q-mr-sm">
        <span class="icon">{{ icon }}</span>
      </q-avatar>

      <q-item-section class="text-container" v-if="!showSlider">
        <q-item-label class="text">{{ truncatedText }}</q-item-label>
      </q-item-section>

      <q-item-section class="slider-container" v-if="showSlider">
        <q-slider v-model="localValue" :min="1" :max="6" markers marker-labels class="slider q-mr-sm" />
      </q-item-section>

      <q-item-section class="button-container">
        <q-btn v-if="!showSlider" color="primary" size="sm" :label="$t('track')" @click="toggleSlider"
          class="track-button" />
        <q-btn v-if="showSlider" color="negative" size="sm" :label="$t('cancel')" @click="cancelTracking"
          class="cancel-button" />
      </q-item-section>
    </q-card-section>
  </q-card>
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
  computed: {
    truncatedText() {
      const maxLength = 20; // Set your desired max length here
      return this.text.length > maxLength ? this.text.substring(0, maxLength) + '...' : this.text;
    }
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
.text-container {
  flex: 1;
  font-family: 'Inter', sans-serif;
  padding-left: 0.9375rem;
}

.text {
  font-size: 1rem;
  color: #000;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.button-container {
  display: flex;
  justify-content: center;
  flex: 0 0 5rem;
}

.track-button {
  background-color: #50c1ba;
  color: white;
  border-radius: 0.25rem;
}

.track-button:hover {
  background-color: #3b9991;
}

.slider-container {
  display: flex;
  align-items: center;
  flex: 1;
  padding-left: 0.9375rem;
  height: 100%;
}

.icon {
  font-size: 1.875rem;
}

.slider {
  flex: 1;
  margin-right: 0.9375rem;
  max-height: 2.5rem;
}

.cancel-button {
  background-color: #f44336;
  color: white;
  border-radius: 0.25rem;
}

.cancel-button:hover {
  background-color: #d32f2f;
}
</style>
