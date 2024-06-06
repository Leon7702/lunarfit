<template>
  <div class="q-pt-md q-pb-md" style="width: 100%">
    <q-list bordered class="rounded-borders">
      <q-expansion-item>
        <template v-slot:header>
          <q-item-section avatar>
            <q-avatar>
              <img src="../assets/Food.svg" alt="Food" />
            </q-avatar>
          </q-item-section>
          <q-item-section>
            Ernährung
          </q-item-section>
        </template>
        <q-card>
          <q-card-section>
            {{ textNutrition }}
          </q-card-section>
        </q-card>
      </q-expansion-item>

    <q-separator />

      <q-expansion-item>
        <template v-slot:header>
          <q-item-section avatar>
            <q-avatar>
              <img src="../assets/Training.svg" alt="Training" />
            </q-avatar>
          </q-item-section>
          <q-item-section>
            Training
          </q-item-section>
        </template>
        <q-card>
          <q-card-section>
            {{ textTraining }}
          </q-card-section>
        </q-card>
      </q-expansion-item>

    <q-separator />

      <q-expansion-item>
        <template v-slot:header>
          <q-item-section avatar>
            <q-avatar>
              <img src="../assets/Health.svg" alt="Food" />
            </q-avatar>
          </q-item-section>
          <q-item-section>
            Gesundheit/ Fruchtbarkeit
          </q-item-section>
        </template>
        <q-card>
          <q-card-section>
            {{ textHealth }}
          </q-card-section>
        </q-card>
      </q-expansion-item>
    </q-list>
  </div>
</template>


<script>
export default {
  props: ['textNutrition', 'textTraining', 'textHealth'],
}
</script>
