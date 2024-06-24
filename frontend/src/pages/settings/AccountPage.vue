<template>
  <div class="welcome-container">
    <div class="header">
      <q-btn flat dense round icon="arrow_back" @click="goBack" />
      <div class="title">{{ $t('account.title') }}</div>
    </div>
    <div class="linie"></div>

    <q-list>
      <q-item-label header class="q-pt-xl q-pb-xs text-color">{{ $t('account.email') }}</q-item-label>
      <q-item class="q-mb-xs grey-background">
        <q-item-section>
          <!-- TODO: get email name from database -->
          <q-item-label>ina.mueller@outlook.de</q-item-label>
        </q-item-section>
      </q-item>
      <q-item-label header class="q-pt-md q-pb-xs text-color">{{ $t('account.password') }}</q-item-label>
      <q-item clickable v-ripple class="q-mb-xs grey-background">
        <q-item-section>
          <q-item-label>{{ $t('account.change-password') }}</q-item-label>
        </q-item-section>
        <q-item-section side>
            <img src="../../assets/arrow-right.svg">
        </q-item-section>
      </q-item>
    </q-list>
  </div>
</template>

<script>

  export default {
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

  .grey-background {
  background-color: #F8F8F8;
  padding: 12px;
}

.text-color {
  color: #50C1BA;
}

  </style>
