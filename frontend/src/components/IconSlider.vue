<template>
  <q-card class="q-pa-none q-mb-xs q-mt-xs" style="height: 60px; display: flex; align-items: center;">
    <q-card-section class="row no-wrap q-gutter-sm q-px-none items-center" style="width: 100%;">
      <q-avatar size="40px" class="q-mr-sm">
        <span class="icon">{{ icon }}</span>
      </q-avatar>

      <q-item-section class="text-container" v-if="!localShowSlider">
        <q-item-label class="text">{{ truncatedText }}</q-item-label>
      </q-item-section>

      <q-item-section class="slider-container" v-if="localShowSlider">
        <q-slider v-model="localValue" :min="1" :max="6" markers marker-labels class="slider q-mr-sm"
          @change="emitValue" />
      </q-item-section>

      <q-item-section class="button-container">
        <q-btn v-if="!localShowSlider" color="primary" size="md" label="➕" @click="toggleSlider" class="track-button" />
        <q-btn v-if="localShowSlider" color="negative" size="md" label="✘" @click="cancelTracking"
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
      default: 0
    },
    showSlider: {
      type: Boolean,
      default: false
    }
  },
  data() {
    return {
      localValue: this.value,
      localShowSlider: this.showSlider
    };
  },
  watch: {
    value(newVal) {
      this.localValue = newVal;
    },
    showSlider(newVal) {
      this.localShowSlider = newVal;
    }
  },
  computed: {
    truncatedText() {
      const maxLength = 20; // Set your desired max length here
      return this.text.length > maxLength ? this.text.substring(0, maxLength) + '...' : this.text;
    }
  },
  methods: {
    emitValue() {
      this.$emit('update:value', this.localValue);
    },
    toggleSlider() {
      this.localShowSlider = !this.localShowSlider;
      this.$emit('update:tracked', this.localShowSlider);
      if (!this.localShowSlider) {
        this.localValue = 0;
        this.emitValue();
      }
    },
    cancelTracking() {
      this.localShowSlider = false;
      this.localValue = 0;
      this.emitValue();
      this.$emit('update:tracked', false);
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
  flex: 0 0 3rem;
}

.track-button {
  background-color: #50c1ba;
  color: white;
  border-radius: 0.25rem;
  font-size: 1.25rem;
  padding: 0.25rem 0.5rem;
}

.track-button:hover {
  background-color: #3b9991;
}

.slider-container {
  display: flex;
  align-items: center;
  flex: 1;
  padding-left: 0.9375rem;
  padding-right: 1rem;
  height: 100%;
}

.icon {
  font-size: 1.875rem;
  padding-left: 0.8rem;

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
  font-size: 1.25rem;
  /* Increased font size */
  padding: 0.25rem 0.5rem;
  /* Adjusted padding */
}

.cancel-button:hover {
  background-color: #d32f2f;
}
</style>
