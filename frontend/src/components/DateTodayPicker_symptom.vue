<template>
  <div class="date-picker-container">
    <q-btn flat dense @click="openPicker" class="date-display">
      {{ formattedDate }} <q-icon name="arrow_drop_down" />
    </q-btn>
    <q-popup-proxy ref="qDateProxy" transition-show="scale" transition-hide="scale">
      <q-date v-model="selectedDate" @input="updateDate" />
    </q-popup-proxy>
  </div>
</template>

<script>
import { ref, watch } from 'vue';
import { date } from 'quasar';

export default {
  name: 'DateTodayPicker',
  props: {
    modelValue: {
      type: String,
      required: true,
    },
  },
  setup(props, { emit }) {
    const selectedDate = ref(new Date(props.modelValue));
    const formattedDate = ref(date.formatDate(selectedDate.value, 'MMMM D'));

    const openPicker = () => {
      if (this.$refs.qDateProxy) {
        this.$refs.qDateProxy.show();
      }
    };

    const updateDate = (newDate) => {
      selectedDate.value = newDate;
      emit('update:modelValue', newDate);
    };

    watch(selectedDate, (newValue) => {
      formattedDate.value = date.formatDate(newValue, 'MMMM D');
    });

    return {
      selectedDate,
      formattedDate,
      openPicker,
      updateDate
    };
  },
};
</script>

<style scoped>
.date-picker-container {
  display: flex;
  align-items: center;
  justify-content: center;
}

.date-display {
  font-size: 1.2em;
  font: 'Inter', sans-serif;
  font-weight: 400;
  color: #000;
}

.q-icon {
  margin-left: 5px;
}
</style>
