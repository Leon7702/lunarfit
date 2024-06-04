<template>
  <div class="q-pa-md">
    <div class="row justify-center">
      <q-btn-toggle v-model="slide" :options="[
        { label: '1', value: 'training' },
        { label: '2', value: 'mood' },
        { label: '3', value: 'burden' },
        { label: '4', value: 'layers' },
        { label: '5', value: 'rest' }
      ]" />
    </div>
    <div class="carousel-container">
    <div class="q-gutter-md">
      <q-carousel v-model="slide" transition-prev="slide-right" transition-next="slide-left" swipeable animated
        control-color="black" navigation-icon="radio_button_unchecked" navigation padding :style="{ height: '80vh', width:'45vh' }"
        class="shadow-1 rounded-borders border-black">

        <q-carousel-slide name="training" class="column no-wrap flex-center">
          <q-scroll-area class="fit">
            <div class="column no-wrap flex-center">
              <div class="text-h6">Training</div>
              <TrsSunburst />
              <div class="text-p">Training Readiness Score: 76%</div>
              <div class="q-pa-md row items-start q-gutter-md text-center">
                <q-card flat bordered class="my-card">
                  <q-card-section>
                    {{ trainingtext }}
                  </q-card-section>
                </q-card>
              </div>
            </div>
          </q-scroll-area>
        </q-carousel-slide>

        <q-carousel-slide name="mood" class="column no-wrap flex-center">
          <q-scroll-area class="fit">
            <div class="column no-wrap flex-center">
              <div class="text-h6">Stimmung</div>
              <TrsSunburst />
              <div class="q-mt-md text-center">
                <q-card class="my-card bg-primary text-white">
                  <q-card-section>
                    <div v-html="moodtext"></div>
                  </q-card-section>
                </q-card>
                <div class="q-pa-md">
                  <p>Mood score today:</p>
                  <q-linear-progress size="25px" :value="progress1" color="primary">
                    <div class="absolute-full flex flex-center">
                      <q-badge color="white" text-color="primary" :label="progressLabel1" />
                    </div>
                  </q-linear-progress>
                </div>
                <p>Verlauf</p>
                <q-card class="my-card border-black">
                  <q-card-section>
                    <p>Diagram</p>
                  </q-card-section>
                </q-card>
              </div>
            </div>
          </q-scroll-area>
        </q-carousel-slide>

        <q-carousel-slide name="burden" class="column no-wrap flex-center">
          <q-scroll-area class="fit">
            <div class="column no-wrap flex-center">
              <div class="text-h6">Belastung</div>
              <TrsSunburst />
              <div class="q-mt-md text-center">
                <q-card class="my-card bg-primary text-white">
                  <q-card-section flat bordered class="border-black">
                    <div v-html="burdentext"></div>
                  </q-card-section>
                </q-card>
              </div>
            </div>
          </q-scroll-area>
        </q-carousel-slide>

        <q-carousel-slide name="layers" class="column no-wrap flex-center">
          <q-scroll-area class="fit">
            <div class="column no-wrap flex-center">
              <div class="text-h6">Beschwerden</div>
              <TrsSunburst />
              <div class="q-mt-md text-center">
                {{ lorem }}
              </div>
            </div>
          </q-scroll-area>
        </q-carousel-slide>

        <q-carousel-slide name="rest" class="column no-wrap flex-center">
          <q-scroll-area class="fit">
            <div class="column no-wrap flex-center">
              <div class="text-h6">Erholung</div>
              <TrsSunburst />
              <div class="q-mt-md text-center">
                {{ resttext }}
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
import TrsSunburst from 'components/TrsSunburst.vue';

export default {
  setup() {
    const progress1 = ref(0.3);
    return {
      slide: ref('training'),
      lorem: 'Lorem ipsum dolor, sit amet consectetur adipisicing elit. Itaque voluptatem totam, architecto cupiditate officia rerum, error dignissimos praesentium libero ab nemo.',
      trainingtext: 'Trainingsempfehlung basierend auf Zyklusphase und TRS. Lorem ipsum dolor sit amet, consectetur adipiscing elit',
      moodtext: 'Deine Stimmung ist... <br> Durch das...<br>Kann sich deine Stimmung...',
      burdentext: 'Dein ACWR liegt bei... <br> Im Verlauf der letzen Tage is er...<br>Da du dich in der... befindest, solltest du darauf achten das Trainingspensum...',
      resttext: 'Dein Erholungszustand ist... Durch solltest das Training gerade im Hinblick auf die hormonellen Veränderungen in den nächsten Tagen...',

      progress1,
      progressLabel1: computed(() => (progress1.value * 100).toFixed(2) + '%'),
    }
  },
  components: {
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
  max-width: 250%;
}

.carousel-container {
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
