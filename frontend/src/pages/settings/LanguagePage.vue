<template>
  <div class="welcome-container">
    <div class="header">
      <q-btn flat dense round icon="arrow_back" @click="goBack" />
      <div class="title">{{ $t('language.title') }}</div>
    </div>
    <div class="linie"></div>
    <div class="q-pa-md">
    <q-option-group
      :options="options"
      type="radio"
      v-model="group"
    />
  </div>
  </div>
</template>

<script>
import { ref } from 'vue';
  export default {
    setup () {
      return {
      group: ref(null),

      options: [
        { label: 'Deutsch', value: 'de', color: 'primary'},
        { label: 'Englisch', value: 'en', color: 'primary' },
      ]
    }
  },
    components: {

    },
    data() {
      return {

      }
    },
    methods: {
      goBack() {
        window.history.back();
      }
    }
  };
  </script>

<style scoped>
  .welcome-container {
    display: flex;
    flex-direction: column;
    margin: auto;
  }

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
    margin-top: 60px;
  }

  .title {
    font: 600 20px 'Inter', sans-serif;
    color: #000;
    text-align: center;
    flex-grow: 1;
    padding-right: 30px;
  }

  </style>
