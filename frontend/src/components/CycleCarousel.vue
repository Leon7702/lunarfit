<template>
  <div class="q-pa-md">
    <div class="row justify-center">
      <!-- Quasar button toggle component to switch between slides -->
      <q-btn-toggle v-model="slide" :options="[
        { label: '1', value: 'menstruation' },
        { label: '2', value: 'follicular' },
        { label: '3', value: 'ovulation' },
        { label: '4', value: 'luteal' }
      ]" />
    </div>
    <div class="q-gutter-md">
      <!-- Quasar carousel component to display in total 4 slides -->
      <q-carousel v-model="slide" transition-prev="slide-right" transition-next="slide-left" swipeable animated
        control-color="black" navigation-icon="radio_button_unchecked" navigation padding :style="{ height: '80vh' }"
        class="shadow-1 rounded-borders border-black">

        <!-- Carousel slide for menstruation -->
        <q-carousel-slide name="menstruation" class="column no-wrap flex-center">
          <q-scroll-area class="fit">
            <div class="column no-wrap flex-center">
              <div class="text-h6">Menstruation</div>
              <q-card flat bordered class="my-card">
                <q-card-section>
                  {{ menstruationtext }}
                </q-card-section>
              </q-card>
              <img class="cycle-image" src="../assets/cyclePhase/PeriodOvulation.png" alt="Graph" />
              <PhaseInformation :textNutrition="menstruationNutrition" :textTraining="menstruationTraining"
                :textHealth="menstruationHealth" />
            </div>
          </q-scroll-area>
        </q-carousel-slide>

        <!-- Carousel slide for follicular phase -->
        <q-carousel-slide name="follicular" class="column no-wrap flex-center">
          <q-scroll-area class="fit">
            <div class="column no-wrap flex-center">
              <div class="text-h6">Follikelphase</div>
              <q-card flat bordered class="my-card">
                <q-card-section>
                {{ folliculartext }}
              </q-card-section>
              </q-card>
              <img class="cycle-image" src="../assets/cyclePhase/Follicular.png" alt="Graph" />
              <PhaseInformation :textNutrition="follicularNutrition" :textTraining="follicularTraining"
                :textHealth="follicularHealth" />
            </div>
          </q-scroll-area>
        </q-carousel-slide>

        <!-- Carousel slide for ovulation phase -->
        <q-carousel-slide name="ovulation" class="column no-wrap flex-center">
          <q-scroll-area class="fit">
            <div class="column no-wrap flex-center">
              <div class="text-h6">Ovulation</div>
              <q-card flat bordered class="my-card">
                <q-card-section>
                {{ ovulationtext }}
              </q-card-section>
              </q-card>
              <img class="cycle-image" src="../assets/cyclePhase/PeriodOvulation.png" alt="Graph" />
              <PhaseInformation :textNutrition="ovulationNutrition" :textTraining="ovulationTraining"
                :textHealth="ovulationHealth" />
            </div>
          </q-scroll-area>
        </q-carousel-slide>

        <!-- Carousel slide for lutheal phase -->
        <q-carousel-slide name="luteal" class="column no-wrap flex-center">
          <q-scroll-area class="fit">
            <div class="column no-wrap flex-center">
              <div class="text-h6">Luthealphase</div>
              <q-card flat bordered class="my-card">
                <q-card-section>
                {{ lutealtext }}
              </q-card-section>
              </q-card>
              <img class="cycle-image" src="../assets/cyclePhase/Lutheal.png" alt="Graph" />
          <PhaseInformation :textNutrition="lutealNutrition" :textTraining="lutealTraining"
            :textHealth="lutealHealth" />
          </div>
          </q-scroll-area>
        </q-carousel-slide>
      </q-carousel>
    </div>
  </div>
</template>


<script>
import { ref } from 'vue';
import PhaseInformation from 'src/components/PhaseInformation.vue';

// TODO: Create a JSON-file for the data and import it here.
// TODO: Import the JSON-file and use the data in the setup function.

export default {
  setup() {
    return {
      // Defining reactive properties
      // TODO: Initial slide need to change depending on the current phase of the user
      slide: ref('menstruation'),
      lorem: 'Lorem ipsum dolor, sit amet consectetur adipisicing elit. Itaque voluptatem totam, architecto cupiditate officia rerum, error dignissimos praesentium libero ab nemo.',
    }
  },
  components: {
    PhaseInformation,
  },
  data() {
    // Defining non-reactive properties
    return {
      menstruationtext: 'Der Zyklus beginnt mit dem ersten Tag der Blutung, die durch den Abfall von Progesteron und Östrogen ausgelöst wird. Das steigende Östrogen hebt die Laune, macht selbstbewusst und kreativ.',
      folliculartext: 'Phase nach der Menstruation, in der die Eibläschchen zu einem sprungbereiten Follikel reifen. Das steigende Östrogen hebt die Laune, machr selbstbewusst und kreativ.',
      ovulationtext: 'Nach dem Eisprung wird die Eizelle aus dem Follikel im Eierstock in den Eileiter ausgestoßen. Die Hülle der Eizelle bleibt als Gelbkörper zurück. Zum Eisprung macht das Östrogen häufig gute Laune. Danach gibt es auch mal schlechte Laune.',
      lutealtext: 'Die Phase nach dem Eisprung bis zum Beginn der nächsten Menstruation. Der Gelbkörper produziert Progesteron, das die Gebärmutterschleimhaut auf die Einnistung einer befruchteten Eizelle vorbereitet. Das Progesteron kann die Laune verschlechtern.',

      menstruationNutrition: "Probeotische Lebensmittel: Frische Sprossen, Sauerkraut",
      menstruationTraining: "Die Sauerstoffaufnahme ist erhöht und die Erholungsfähigkeit verbessert sich. Kraftaufbau. Intervalltraining, Schnelligkeitstraining, neue Belastungsreite, hohe Intensität.",
      menstruationHealth: "Text für Gesundheit",

      follicularNutrition: "Probeotische Lebensmittel: Frische Sprossen, Sauerkraut",
      follicularTraining: "Die Sauerstoffaufnahme ist erhöht und die Erholungsfähigkeit verbessert sich. Kraftaufbau. Intervalltraining, Schnelligkeitstraining, neue Belastungsreite, hohe Intensität.",
      follicularHealth: "Text für Gesundheit",

      ovulationNutrition: "Probeotische Lebensmittel: Frische Sprossen, Sauerkraut",
      ovulationTraining: "Die Sauerstoffaufnahme ist erhöht und die Erholungsfähigkeit verbessert sich. Kraftaufbau. Intervalltraining, Schnelligkeitstraining, neue Belastungsreite, hohe Intensität.",
      ovulationHealth: "Text für Gesundheit",

      lutealNutrition: "Magnesium, hochwertige Fette, Proteine, Ballaststoffe: Haferflocken, Vollkornprodukte, Bananen, Blattgemüse, Hülsenfrüchte. Weniger Koffein, Zucker und Alkohol",
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
  max-width: 100vw;
}

.cycle-image {
  max-width: 100%;
  padding-top: 16px;
}
</style>
