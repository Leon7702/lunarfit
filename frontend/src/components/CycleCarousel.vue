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
                  {{ data.menstruationtext }}
                </q-card-section>
              </q-card>
              <img class="cycle-image" src="../assets/cyclePhase/PeriodOvulation.png" alt="Graph" />
              <PhaseInformation :textNutrition="data.menstruationNutrition" :textTraining="data.menstruationTraining"
                :textHealth="data.menstruationHealth" />
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
                  {{ data.folliculartext }}
                </q-card-section>
              </q-card>
              <img class="cycle-image" src="../assets/cyclePhase/Follicular.png" alt="Graph" />
              <PhaseInformation :textNutrition="data.follicularNutrition" :textTraining="data.follicularTraining"
                :textHealth="data.follicularHealth" />
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
                  {{ data.ovulationtext }}
                </q-card-section>
              </q-card>
              <img class="cycle-image" src="../assets/cyclePhase/PeriodOvulation.png" alt="Graph" />
              <PhaseInformation :textNutrition="data.ovulationNutrition" :textTraining="data.ovulationTraining"
                :textHealth="data.ovulationHealth" />
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
                  {{ data.lutealtext }}
                </q-card-section>
              </q-card>
              <img class="cycle-image" src="../assets/cyclePhase/Lutheal.png" alt="Graph" />
              <PhaseInformation :textNutrition="data.lutealNutrition" :textTraining="data.lutealTraining"
                :textHealth="data.lutealHealth" />
            </div>
          </q-scroll-area>
        </q-carousel-slide>
      </q-carousel>
    </div>
  </div>
</template>


<script>
import axios from 'axios';
import { ref } from 'vue';
import PhaseInformation from 'src/components/PhaseInformation.vue';
import data from '../assets/cycleData.json'; // path to the JSON-file

export default {
  // TODO: Initial slide need to change depending on the current phase of the user
  // 1. Get the user's cycle length and current day from the database

  // 2. Calculate the current phase of the user depending on the current day and cycle length
  // cycleLength = 28; // replace this with the actual cycle length of the user --> get data from database
  // if 2/10 of cyclelength & state1 (in menstruation) then in phase1
  // if 3/10 (so 0.5) of cyclelength then in phase2
  // if 1/10 (so 0.6) of cyclelength then in phase3
  // if 4/10 of cyclelength then in phase4

  // 3. Set the initial slide depending on the current phase of the user
  setup() {
    const slide = ref('');
    const cycleLength = ref(null);
    const currentDay = ref(null);

    const fetchData = async () => {
      try {
        const response = await axios.get('http://localhost:3000/usersdata/');
        cycleLength.value = response.data.cycleLength;
        currentDay.value = response.data.currentDay;

        // FIXME: fix edge cases due to rounding errors --> see calculation
        const currentPhase = currentDay.value / cycleLength.value;
        if (currentPhase <= 0.2) {
          slide.value = 'menstruation';
        } else if (currentPhase <= 0.5) { // Adjusted to 0.5 for clarity in phases
          slide.value = 'follicular';
        } else if (currentPhase <= 0.6) {
          slide.value = 'ovulation';
        } else {
          slide.value = 'luteal';
        }
      } catch (error) {
        console.error('Failed to fetch data:', error);
      }
    };

    fetchData();

    return {
      slide,
      data
    };
  },
  components: {
    PhaseInformation,
  },
};
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
