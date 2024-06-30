<template>
  <div class="q-pt-md q-pb-md" style="width: 100%">
    <q-list bordered class="rounded-borders">
      <q-expansion-item class="hover-effect">
        <template v-slot:header>
          <q-item-section avatar>
            <q-avatar>
              <img src="../assets/Food.svg" alt="Food" />
            </q-avatar>
          </q-item-section>
          <q-item-section>
            {{ $t('nutrition') }}
          </q-item-section>
        </template>
        <q-card>
          <q-card-section>
            <ul>
              <li v-for="(item, index) in textNutrition" :key="'nutrition-' + index">{{ item }}</li>
            </ul>
          </q-card-section>
        </q-card>
      </q-expansion-item>

      <q-separator />

      <q-expansion-item class="hover-effect">
        <template v-slot:header>
          <q-item-section avatar>
            <q-avatar>
              <img src="../assets/Training.svg" alt="Training" />
            </q-avatar>
          </q-item-section>
          <q-item-section>
            {{ $t('training') }}
          </q-item-section>
        </template>
        <q-card>
          <q-card-section>
            {{ textTraining }}
          </q-card-section>
        </q-card>
      </q-expansion-item>

      <q-separator />

      <q-expansion-item class="hover-effect">
        <template v-slot:header>
          <q-item-section avatar>
            <q-avatar>
              <img src="../assets/Health.svg" alt="Food" />
            </q-avatar>
          </q-item-section>
          <q-item-section>
            {{ $t('healthFertility') }}
          </q-item-section>
        </template>
        <q-card>
          <q-card-section>
            {{ textHealthString1 }}
            <ul>
              <li v-for="(item, index) in textHealthArray" :key="'health-' + index">{{ item }}</li>
            </ul>
            {{ textHealthString2 }}
          </q-card-section>
        </q-card>
      </q-expansion-item>
    </q-list>
  </div>
</template>


<script>
export default {
  props: {
    textNutrition: Array,
    textTraining: String,
    textHealthString1: String,
    textHealthString2: String,
    textHealthArray: Array,
  },
}
</script>

<style scoped>
ul {
  padding-left: 15px;
  margin: 0;
}

.hover-effect {
  transition: background-color 0.3s ease-in-out;
}

.hover-effect:hover {
  background-color: rgba(80, 193, 186, 0.2);
}
</style>
