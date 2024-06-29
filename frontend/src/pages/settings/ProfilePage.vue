<template>
  <div class="welcome-container">
    <div class="header">
      <q-btn flat dense round icon="arrow_back" @click="goBack" />
      <div class="title">{{ $t('profile.title') }}</div>
    </div>
    <div class="linie"></div>

    <q-list>
      <!-- TODO: change prefix (v-slot: prepend?) -->
      <q-input filled v-model="first" type="text" input-class="text-right" class="q-pt-xl q-mb-sm">
        <template v-slot:prepend>
          <div class="text-color">{{ $t('profile.firstName') }}</div>
        </template>
      </q-input>
      <q-input filled v-model="last" type="text" input-class="text-right" class="q-mb-sm">
        <template v-slot:prepend>
          <div class="text-color">{{ $t('profile.lastName') }}</div>
        </template>
      </q-input>
      <q-input filled v-model="date" type="text" input-class="text-right" class="q-mb-sm">
        <template v-slot:prepend>
          <div class="text-color">{{ $t('profile.birthdate') }}</div>
        </template>
      </q-input>
      <q-input filled v-model="height" type="number" input-class="text-right" class="q-mb-sm">
        <template v-slot:prepend>
          <div class="text-color">{{ $t('profile.height') }}</div>
        </template>
      </q-input>
      <q-input filled v-model="weight" type="number" input-class="text-right" class="q-mb-sm">
        <template v-slot:prepend>
          <div class="text-color">{{ $t('profile.weight') }}</div>
        </template>
      </q-input>
      <q-select filled v-model="hormonalContraception" :options="contraceptionOptions" input-class="text-right"
        class="q-mb-sm">
        <template v-slot:prepend>
          <div class="text-color">{{ $t('profile.contraception') }}</div>
        </template>
      </q-select>
    </q-list>
  </div>
</template>

<script>
import { ref } from 'vue';

export default {
  // i18n handling
  name: 'ProfilePage',
  // computed: {
  //   contraceptionOptions() {
  //     return [
  //       this.$t('profile.contraceptionOptions[0]'),
  //       this.$t('profile.contraceptionOptions[1]'),
  //       this.$t('profile.contraceptionOptions[2]'),
  //       this.$t('profile.contraceptionOptions[3]'),
  //       this.$t('profile.contraceptionOptions[4]'),
  //       this.$t('profile.contraceptionOptions[5]'),
  //     ];
  //   },
  // },

  // refactored:
  computed: {
    contraceptionOptions() {
      return Array.from({ length: 6 }, (_, i) =>
        this.$t(`profile.contraceptionOptions[${i}]`)
      );
    },
  },
  setup() {
    return {
      //TODO: get data from backend --> replace these with dynamic data fetching logic
      first: ref('Ina'),
      last: ref('Müller'),
      date: ref('12.08.1999'),
      height: ref(180),
      weight: ref(77),
      hormonalContraception: ref(null),

      // comment out because of i18n
      // contraceptionOptions: [
      //   'Pilleee', 'Hormonspirale', 'Kupferspirale', 'Hormonimplantat', 'Dreimonatsspritze', 'Vaginalring', 'Sonstiges',
      // ]
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

.text-color {
  color: #50C1BA;
  font-size: 14px;
}
</style>
