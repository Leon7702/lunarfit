<template>
  <div class="q-pa-md">
    <div class="row justify-center">
      <q-btn-toggle v-model="slide" :options="[
        { label: '1', value: 'menstruation' },
        { label: '2', value: 'follicular' },
        { label: '3', value: 'ovulation' },
        { label: '4', value: 'luteal' }
      ]" />
    </div>
    <div class="q-gutter-md">
      <q-carousel v-model="slide" transition-prev="slide-right" transition-next="slide-left" swipeable animated
        control-color="black" navigation-icon="radio_button_unchecked" navigation padding height="100%"
        class="shadow-1 rounded-borders border-black">

        <q-carousel-slide name="menstruation" class="column no-wrap flex-center">
          <PhaseInfoCard title="Menstruation"
            text="Der Zyklus beginnt mit dem ersten Tag der Blutung, die durch den Abfall con Progesteron und Östrogen ausgelöst wird. Das steigende Östrogen hebt die Launer, macht selbstbewusst und kreativ." />
          <img class="cycle-image" src="../assets/CyclePhaseGraph.jpg" alt="Graph" />
          <PhaseInformation :textNutrition="textNutrition" :textTraining="textTraining" :textHealth="textHealth" />
        </q-carousel-slide>

        <q-carousel-slide name="follicular" class="column no-wrap flex-center">
          <p>Follikelphase</p>
        </q-carousel-slide>

        <q-carousel-slide name="ovulation" class="column no-wrap flex-center">
          <p>Ovulation</p>
        </q-carousel-slide>

        <q-carousel-slide name="luteal" class="column no-wrap flex-center">
          <p>Luthealphase</p>
        </q-carousel-slide>
      </q-carousel>
    </div>
  </div>
</template>


<script>
import { ref } from 'vue';
import PhaseInformation from 'src/components/PhaseInformation.vue';
import PhaseInfoCard from 'src/components/PhaseInfoCard.vue';

export default {
  setup() {
    return {
      slide: ref('menstruation'),
      lorem: 'Lorem ipsum dolor, sit amet consectetur adipisicing elit. Itaque voluptatem totam, architecto cupiditate officia rerum, error dignissimos praesentium libero ab nemo.',

    }
  },
  components: {
    PhaseInfoCard,
    PhaseInformation,
  },
  data() {
    return {
      textNutrition: "Probeotische Lebensmittel: Frische Sprossen, Sauerkraut",
      textTraining: "Die Sauerstoffaufnahme ist erhöht und die Erholungsfähigkeit verbessert sich. Kraftaufbau. Intervalltraining, Schnelligkeitstraining, neue Belastungsreite, hohe Intensität.",
      textHealth: "Text für Gesundheit"
    }
  },
}
</script>

<style scoped>
.border-black {
  border: 1px solid black;
}

.my-card {
  width: 100%;
  max-width: 250px;
}

.cycle-image {
  max-width: 100%;
}
</style>
