<template>
  <div class="q-px-md">
    <div class="row justify-center">
      <q-btn-toggle v-model="slide" :options="[
        { label: '1', value: 'training' },
        { label: '2', value: 'mood' },
        { label: '3', value: 'strain' },
        { label: '4', value: 'free' },
        { label: '5', value: 'rest' }
      ]" />
    </div>
    <div class="carousel-container">
      <div class="q-gutter-md">
        <q-carousel v-model="slide" transition-prev="slide-right" transition-next="slide-left" swipeable animated
          control-color="black" navigation-icon="radio_button_unchecked" navigation padding
          :style="{ height: '80vh', width: '45vh' }" class="shadow-1 rounded-borders border-black">

          <q-carousel-slide name="training" class="column no-wrap flex-center">
            <q-scroll-area class="fit">
              <div class="column no-wrap flex-center">
                <div class="text-h6">Training</div>
                <TrsSunburst />
                <div class="text-p"><strong>Training Readiness Score: 76%</strong></div>
                <p></p>
                <q-card flat bordered class="my-card">
                  <q-card-section>
                    {{ trainingtext }}
                  </q-card-section>
                </q-card>
              </div>
            </q-scroll-area>
          </q-carousel-slide>

          <q-carousel-slide name="mood" class="column no-wrap flex-center">
            <q-scroll-area class="fit">
              <div class="column no-wrap flex-center">
                <div class="text-h6">Stimmung</div>
                <div class="q-mt-md text-center">
                  <q-card flat bordered class="my-card">
                    <q-card-section>
                      <div class="info-text">
                        <strong>{{ $t(`moodInfo.${moodScore}.description`) }}</strong>
                        <div>{{ $t(`moodInfo.${moodScore}.advice`) }}</div>
                      </div>
                    </q-card-section>
                  </q-card>
                  <div class="q-pa-md">
                    <p>Stimmung Score heute:</p>
                    <div class="q-gutter-y-md column justify-center items-center">
                      <q-rating v-model="moodScore" size="2em" :max="6" color="grey" :color-selected="ratingColors"
                        icon="rectangle" readonly />
                    </div>
                  </div>

                  <!-- <p>Verlauf</p>
                  <q-card class="my-card border-black">
                    <q-card-section>
                      <p>Diagram</p>
                    </q-card-section>
                  </q-card> -->
                </div>
              </div>
            </q-scroll-area>
          </q-carousel-slide>

          <q-carousel-slide name="strain" class="column no-wrap flex-center">
            <q-scroll-area class="fit">
              <div class="column no-wrap flex-center">
                <div class="text-h6">Belastung</div>
                <div class="q-mt-md text-center">
                  <q-card flat bordered class="my-card">
                    <q-card-section>
                      <div class="info-text">
                        <strong>{{ $t(`acwrInfo`)}} {{ acwr }}</strong>
                        <div>{{ $t(`strainInfo.${acwrScore}.description`) }}</div>
                        <p></p>
                        <div>{{ $t(`strainInfo.${acwrScore}.recommendations[0]`) }}</div>
                        <div>{{ $t(`strainInfo.${acwrScore}.recommendations[1]`) }}</div>
                        <div>{{ $t(`strainInfo.${acwrScore}.recommendations[2]`) }}</div>
                        <div>{{ $t(`strainInfo.${acwrScore}.recommendations[3]`) }}</div>
                      </div>
                    </q-card-section>
                  </q-card>
                  <div class="q-pa-md">
                    <p>Belastung Score heute:</p>
                    <q-linear-progress size="25px" :value="acwrProgress" color="primary">
                      <div class="absolute-full flex flex-center">
                        <q-badge color="white" text-color="primary" :label="acwrProgressLabel" />
                      </div>
                    </q-linear-progress>
                  </div>
                </div>
              </div>
            </q-scroll-area>
          </q-carousel-slide>

          <q-carousel-slide name="free" class="column no-wrap flex-center">
            <q-scroll-area class="fit">
              <div class="column no-wrap flex-center">
                <div class="text-h6">Beschwerdefreiheit</div>
                <div class="q-mt-md text-center">
                  <q-card flat bordered class="my-card">
                    <q-card-section>
                      <div class="info-text">
                        <div>{{ $t(`freeInfo.${freeScore}.description`) }}</div>
                        <p></p>
                        <div>{{ $t(`freeInfo.${freeScore}.recommendations[0]`) }}</div>
                        <div>{{ $t(`freeInfo.${freeScore}.recommendations[1]`) }}</div>
                        <div>{{ $t(`freeInfo.${freeScore}.recommendations[2]`) }}</div>
                        <div>{{ $t(`freeInfo.${freeScore}.recommendations[3]`) }}</div>
                        <div>{{ $t(`freeInfo.${freeScore}.recommendations[4]`) }}</div>
                      </div>
                    </q-card-section>
                  </q-card>
                  <div class="q-pa-md">
                    <p>Beschwerdefreiheit Score heute:</p>
                    <div class="q-gutter-y-md column justify-center items-center">
                      <q-rating v-model="freeScore" size="2em" :max="6" color="grey" :color-selected="ratingColors"
                        icon="rectangle" readonly />
                    </div>
                  </div>
                </div>
              </div>
            </q-scroll-area>
          </q-carousel-slide>

          <q-carousel-slide name="rest" class="column no-wrap flex-center">
            <q-scroll-area class="fit">
              <div class="column no-wrap flex-center">
                <div class="text-h6">Erholung</div>
                <div class="q-mt-md text-center">
                  <q-card flat bordered class="my-card">
                    <q-card-section>
                      {{ $t(`restInfo.${restScore}`) }}
                    </q-card-section>
                  </q-card>
                  <div class="q-pa-md">
                    <p>Erholung Score heute:</p>
                    <div class="q-gutter-y-md column justify-center items-center">
                      <q-rating v-model="restScore" size="2em" :max="6" color="grey" :color-selected="ratingColors"
                        icon="rectangle" readonly />
                    </div>
                  </div>
                </div>
              </div>
            </q-scroll-area>
          </q-carousel-slide>
        </q-carousel>
      </div>
    </div>
  </div>
</template>


<script>
import { ref, computed } from 'vue';
import axios from 'axios';
import TrsSunburst from 'components/TrsSunburst.vue';

export default {
  setup() {
    const slide = ref('training');
    const moodScore = ref(0);
    const strainScore = ref(0);
    const freeScore = ref(0);
    const restScore = ref(0);
    const acwr = ref(1.2);

    const fetchData = async () => {
      try {
        const response = await axios.get('http://localhost:3000/trsdata');
        const trsdata = response.data;
        moodScore.value = trsdata.mood;
        strainScore.value = trsdata.strain;
        freeScore.value = trsdata.free;
        restScore.value = trsdata.rest;
        acwr.value = trsdata.acwr;
      } catch (error) {
        console.error('Failed to fetch data:', error);
      }
    };

    fetchData();

    const acwrProgress = computed(() => Math.min(acwr.value / 2, 1));
    const acwrProgressLabel = computed(() => (acwr.value).toFixed(2));

    const acwrScore = computed(() => {
      if (acwr.value < 0.8) return 1;
      if (acwr.value < 1.5) return 2;
      if (acwr.value < 1.8) return 3;
      return 4;
    });

    return {
      // TODO: change names to be consistent to TrsSunburst and database
      lorem: 'Lorem ipsum dolor, sit amet consectetur adipisicing elit. Itaque voluptatem totam, architecto cupiditate officia rerum, error dignissimos praesentium libero ab nemo.',
      trainingtext: 'Trainingsempfehlung basierend auf Zyklusphase und TRS. Lorem ipsum dolor sit amet, consectetur adipiscing elit',
      moodtext: 'Deine Stimmung ist... Durch das...Kann sich deine Stimmung...',
      burdentext: 'Dein ACWR liegt bei... Im Verlauf der letzen Tage is er...Da du dich in der... befindest, solltest du darauf achten das Trainingspensum...',
      resttext: 'Dein Erholungszustand ist... Durch solltest das Training gerade im Hinblick auf die hormonellen Veränderungen in den nächsten Tagen...',

      slide,
      moodScore,
      strainScore,
      freeScore,
      restScore,
      acwr,
      acwrScore,
      acwrProgress,
      acwrProgressLabel,
      ratingColors: ['teal-2', 'teal-3', 'teal-4', 'teal-5', 'teal-6', 'teal-7']
    }
  },
  components: {
    // TODO: respective TrsSunburst components for each slide should be changed accordingly
    // Training gets original TrsSunburst component, the others get a modified version:
    // Mood: TrsSunburstMood
    // Strain: TrsSunburstStrain
    // Rest: TrsSunburstRest
    // Free: TrsSunburstFree
    TrsSunburst,
  },
}
</script>

<style scoped>
.border-black {
  border: 1px solid black;
}

.my-card {
  width: 100%;
  /* max-width: 250%; */
  max-width: 100vw;
}

.carousel-container {
  display: flex;
  justify-content: center;
  align-items: center;
}

.info-text {
  text-align: left;
}
</style>
