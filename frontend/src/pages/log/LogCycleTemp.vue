<template>
  <div class="size-container">
  <div class="welcome-container">
    <div class="header">
      <q-btn flat dense round icon="arrow_back" @click="goBack" />
      <div class="title">{{ $t('logCycle.temperature.title') }}</div>
    </div>
    <div class="linie"></div>
    <div class="description">
      {{ $t('logCycle.temperature.description') }}
    </div>
    <div class="form-group">
      <FormFieldText
        id="temperature"
        label=""
        iconName=""
        inputType="number"
        v-model="temperature"
      />
    </div>
    <div class="description-two">
      {{ $t('logCycle.temperature.descriptionTwo') }}
    </div>
    <div class="form-group">
      <CheckboxInput v-model="storfaktoren" />
    </div>
    <div class="small-description">
      {{ $t('logCycle.temperature.smallDescription') }}
    </div>
  </div>
  </div>
</template>

<script>
import CheckboxInput from 'components/CheckboxInput.vue';
import FormFieldText from 'components/FormFieldText.vue';

export default {
  components: {
    CheckboxInput,
    FormFieldText
  },
  data() {
    return {
      storfaktoren: false 
    };
  },
  methods: {
    goBack() {
      window.history.back();
    }
  }
};
</script>

<style scoped>

.linie {
  height: 1px;
  background-color: rgba(0, 0, 0, 0.1);
  width: 120%;
  margin-top: 10px;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  padding: 10px 0;
  margin-top: 20px;
}

.title {
  font: 600 20px 'Inter', sans-serif;
  color: #000;
  text-align: center;
  flex-grow: 1;
  padding-right: 30px;
}

.description {
  margin-top: 30px;
  text-align: left;
  width: 100%;
  font-size: 16px;
  font-weight: 500;
  margin-bottom: 10px;
}

.description-two {
  text-align: left;
  width: 100%;
  margin-top: 5px;
  font-size: 16px;
  font-weight: 500;
  margin-bottom: 10px;
}

.form-group {
  width: 100%;
}

.small-description {
  font: 12px/16px 'Inter', sans-serif;
  margin-top: 15px;
}

</style>
