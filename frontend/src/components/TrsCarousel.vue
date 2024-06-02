<template>
  <div class="q-pa-md">
    <div class="row justify-center">
      <q-btn-toggle v-model="slide" :options="[
        { label: 1, value: 'mood' },
        { label: 2, value: 'tv' },
        { label: 3, value: 'layers' },
        { label: 4, value: 'map' }
      ]" />
    </div>
    <div class="q-gutter-md">
      <q-carousel v-model="slide" transition-prev="slide-right" transition-next="slide-left" swipeable animated
        control-color="black" prev-icon="arrow_left" next-icon="arrow_right" navigation-icon="radio_button_unchecked"
        navigation padding arrows height="100%" class="shadow-1 rounded-borders border-black">

        <q-carousel-slide name="mood" class="column no-wrap flex-center">
          <p>Stimmung</p>
          <TrsSunburst />
          <div class="q-mt-md text-center">
            <q-card class="my-card bg-primary text-white">
              <q-card-section>
                <div v-html="mood"></div>
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
          </div>
        </q-carousel-slide>
        <q-carousel-slide name="tv" class="column no-wrap flex-center">
          <q-icon name="live_tv" size="56px" />
          <div class="q-mt-md text-center">
            <q-card class="my-card bg-primary text-white">
              <q-card-section flat bordered class="border-black">
                <div v-html="lorem"></div>
              </q-card-section>
            </q-card>
          </div>
        </q-carousel-slide>
        <q-carousel-slide name="layers" class="column no-wrap flex-center">
          <q-icon name="layers" size="56px" />
          <div class="q-mt-md text-center">
            {{ lorem }}
          </div>
        </q-carousel-slide>
        <q-carousel-slide name="map" class="column no-wrap flex-center">
          <q-icon name="terrain" size="56px" />
          <div class="q-mt-md text-center">
            {{ lorem }}
          </div>
        </q-carousel-slide>
      </q-carousel>
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
      slide: ref('mood'),
      lorem: 'Lorem ipsum dolor, sit amet consectetur adipisicing elit. Itaque voluptatem totam, architecto cupiditate officia rerum, error dignissimos praesentium libero ab nemo.',
      mood: 'Deine Stimmung ist... <br> Durch das...<br>Kann sich deine Stimmung...',

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
  max-width: 250px;
}
</style>
