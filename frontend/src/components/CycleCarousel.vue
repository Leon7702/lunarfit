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
          <p>Menstruation</p>
          <div class="q-mt-md text-center">
            {{ menstruationtext }}
          </div>
          <img class="cycle-image" src="../assets/CyclePhaseGraph.jpg" alt="Graph" />
          <PhaseInformation :textNutrition="menstruationNutrition" :textTraining="menstruationTraining" :textHealth="menstruationHealth" />
        </q-carousel-slide>

        <q-carousel-slide name="follicular" class="column no-wrap flex-center">
          <p>Follikelphase</p>
          <div class="q-mt-md text-center">
            {{ folliculartext }}
          </div>
          <img class="cycle-image" src="../assets/CyclePhaseGraph.jpg" alt="Graph" />
          <PhaseInformation :textNutrition="follicularNutrition" :textTraining="follicularTraining" :textHealth="follicularHealth" />
        </q-carousel-slide>

        <q-carousel-slide name="ovulation" class="column no-wrap flex-center">
          <p>Ovulation</p>
          <div class="q-mt-md text-center">
            {{ ovulationtext }}
          </div>
          <img class="cycle-image" src="../assets/CyclePhaseGraph.jpg" alt="Graph" />
          <PhaseInformation :textNutrition="ovulationNutrition" :textTraining="ovulationTraining" :textHealth="ovulationHealth" />
        </q-carousel-slide>

        <q-carousel-slide name="luteal" class="column no-wrap flex-center">
          <p>Luthealphase</p>
          <div class="q-mt-md text-center">
            {{ lutealtext }}
          </div>
          <img class="cycle-image" src="../assets/CyclePhaseGraph.jpg" alt="Graph" />
          <PhaseInformation :textNutrition="lutealNutrition" :textTraining="lutealTraining" :textHealth="lutealHealth" />
        </q-carousel-slide>
      </q-carousel>
    </div>
  </div>
</template>


<script>
import { ref } from 'vue';
import PhaseInformation from 'src/components/PhaseInformation.vue';

export default {
  setup() {
    return {
      slide: ref('menstruation'),
      lorem: 'Lorem ipsum dolor, sit amet consectetur adipisicing elit. Itaque voluptatem totam, architecto cupiditate officia rerum, error dignissimos praesentium libero ab nemo.',
      menstruationtext: 'Der Zyklus beginnt mit dem ersten Tag der Blutung, die durch den Abfall von Progesteron und Östrogen ausgelöst wird. Das steigende Östrogen hebt die Launer, macht selbstbewusst und kreativ.',
      folliculartext: 'Phase nach der Menstruation, in der die Eibläschchen zu einem sprungbereiten Follikel reifen. Das steigende Östrogen hebt die Laune, machr selbstbewusst und kreativ.',
      ovulationtext: 'Nach dem Eisprung wird die Eizelle aus dem Follikel im Eierstock in den Eileiter ausgestoßen. Die Hülle der Eizelle bleibt als Gelbkörper zurück. Zum Eisprung maccht das Östrogen häufig gute Laune. Danach gibt es auch mal schlechte Laune.',
      lutealtext: 'Die Phase nach dem Eisprung bis zum Beginn der nächsten Menstruation. Der Gelbkörper produziert Progesteron, das die Gebärmutterschleimhaut auf die Einnistung einer befruchteten Eizelle vorbereitet. Das Progesteron kann die Laune verschlechtern.',
    }
  },
  components: {
    PhaseInformation,
  },
  data() {
    return {
      menstruationNutrition: "Probeotische Lebensmittel: Frische Sprossen, Sauerkraut",
      menstruationTraining: "Die Sauerstoffaufnahme ist erhöht und die Erholungsfähigkeit verbessert sich. Kraftaufbau. Intervalltraining, Schnelligkeitstraining, neue Belastungsreite, hohe Intensität.",
      menstruationHealth: "Text für Gesundheit",

      follicularNutrition: "Probeotische Lebensmittel: Frische Sprossen, Sauerkraut",
      follicularTraining: "Die Sauerstoffaufnahme ist erhöht und die Erholungsfähigkeit verbessert sich. Kraftaufbau. Intervalltraining, Schnelligkeitstraining, neue Belastungsreite, hohe Intensität.",
      follicularHealth: "Text für Gesundheit",

      ovulationNutrition: "Probeotische Lebensmittel: Frische Sprossen, Sauerkraut",
      ovulationTraining: "Die Sauerstoffaufnahme ist erhöht und die Erholungsfähigkeit verbessert sich. Kraftaufbau. Intervalltraining, Schnelligkeitstraining, neue Belastungsreite, hohe Intensität.",
      ovulationHealth: "Text für Gesundheit",

      lutealNutrition: "Magnesium, hochwertige Fette, Proteine, Ballaststoffe: Haferflocken, Vollkornprodukte, Bananen, Blattgemüse, Hülsenfrüchte. Weniger Koffein, Zucker und Alkohol.",
      lutealTraining: "Die Sauerstoffaufnahme ist erhöht und die Erholungsfähigkeit verbessert sich. Kraftaufbau. Intervalltraining, Schnelligkeitstraining, neue Belastungsreite, hohe Intensität.",
      lutealHealth: "Text für Gesundheit",
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
