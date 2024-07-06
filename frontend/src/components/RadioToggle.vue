<template>
  <div class="q-pa-md">
    <q-list>
      <!-- Rendering a <label> tag (notice tag="label") so QRadios will respond to clicks on QItems to change Toggle state. -->
      <q-item tag="label" v-ripple class="styled-item">
        <q-item-section avatar>
          <q-radio v-model="value" val="ja" color="primary" />
        </q-item-section>
        <q-item-section>
          <q-item-label>{{ $t('yes') }}</q-item-label>
        </q-item-section>
      </q-item>

      <q-item tag="label" v-ripple class="styled-item">
        <q-item-section avatar>
          <q-radio v-model="value" val="nein" color="primary" />
        </q-item-section>
        <q-item-section>
          <q-item-label>{{ $t('no') }}</q-item-label>
        </q-item-section>
      </q-item>
    </q-list>
  </div>
</template>

<script>
import { ref, watch } from 'vue'
import { useI18n } from 'vue-i18n'

export default {
  props: {
    modelValue: {
      type: String,
      required: true
    }
  },
  setup(props, { emit }) {
    const value = ref(props.modelValue)

    watch(value, (newValue) => {
      emit('update:modelValue', newValue)
    })

    return {
      value
    }
  }
}
</script>

<style scoped>
.q-pa-md {
  padding-top: 5px;
  padding-left: 5px;
  padding-right: 5px;
  
  border-radius: 4px;
}

.styled-item {
  margin-bottom: 10px; /* Add space between items */
  background-color: #F2F2F2;
}
</style>
