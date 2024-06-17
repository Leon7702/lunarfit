<template>
  <div class="q-pa-md">
    <div class="q-gutter-y-md column" >
      <q-input
        :type="inputType"
        :pattern="pattern"
        color="teal"
        filled
        v-model="text"
        :label="label"
        :class="{ 'no-icon': !iconName }"
      >
        <template v-if="iconName" v-slot:prepend>
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
    },
    inputType: {
      type: String,
      default: 'text'
    },
    pattern: {
      type: String,
      default: ''
    }
  },
  data() {
    return {
      text: this.value
    };
  },
  watch: {
    value(newValue) {
      this.text = newValue;
    },
    text(newValue) {
      this.$emit('input', newValue);
    }
  }
};
</script>

<style scoped>
.q-input.no-icon .q-field__native {
  padding-left: 36px; /* Adjust this value if needed */
}

.q-pa-md {
  padding-top: 5px;
  padding-left: 5px;
  padding-right: 5px;
}
</style>
