<template>
  <div class="welcome-container">
    <div class="header">
      <q-btn flat dense round icon="arrow_back" @click="goBack" />
      <div class="title">Profil</div>
    </div>
    <div class="linie"></div>

    <q-list>
      <!-- TODO: change prefix (v-slot: prepend?) -->
      <q-input filled v-model="first" type="text" input-class="text-right" class="q-pt-xl q-mb-sm">
        <template v-slot:prepend>
          <div class="text-color">Vorname</div>
        </template>
      </q-input>
      <q-input filled v-model="last" type="text" input-class="text-right" class="q-mb-sm">
        <template v-slot:prepend>
          <div class="text-color">Nachname</div>
        </template>
      </q-input>
      <q-input filled v-model="date" type="text" input-class="text-right" class="q-mb-sm">
        <template v-slot:prepend>
          <div class="text-color">Geburtsdatum</div>
        </template>
      </q-input>
      <q-input filled v-model="height" type="number" input-class="text-right" class="q-mb-sm">
        <template v-slot:prepend>
          <div class="text-color">Größe in cm</div>
        </template>
      </q-input>
      <q-input filled v-model="weigth" type="number" input-class="text-right" class="q-mb-sm">
        <template v-slot:prepend>
          <div class="text-color">Gewicht in kg</div>
        </template>
      </q-input>
      <q-select filled v-model="contraceptives" :options="options" input-class="text-right"
        class="q-mb-sm">
        <template v-slot:prepend>
          <div class="text-color">Verhütungsmittel</div>
        </template>
      </q-select>
    </q-list>
  </div>
</template>

<script>
import { ref } from 'vue';

export default {
  setup() {
    return {
      //TODO: get data from backend
      first: ref('Ina'),
      last: ref('Müller'),
      date: ref('12.08.1999'),
      height: ref(180),
      weigth: ref(77),
      contraceptives: ref(null),

      options: [
        'Pille', 'Hormonenspirale', 'Kupferspirale', 'Hormonimplantat', 'Dreimonatsspritze', 'Vaginalring', 'Sonstiges',
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

.text-color {
  color: #50C1BA;
  font-size: 14px;
}
</style>
