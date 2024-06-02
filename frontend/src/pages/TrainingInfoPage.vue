<template>
  <BackButtonText />
  <div class="q-pa-md row items-start q-gutter-md text-center">
    <q-card flat bordered class="my-card" @click="navigateToTrsInfoPage">
      <q-card-section>
        <div class="text-h6">Training</div>
      </q-card-section>
      <TrsSunburst />
      <q-card-section class="q-pt-none">
        Training Readiness Score: 76%
      </q-card-section>

      <q-separator inset />

      <q-card-section>
        {{ trainingtext }}
      </q-card-section>
    </q-card>
  </div>
</template>

<script>
import BackButtonText from 'components/BackButtonText.vue';
import TrsSunburst from 'components/TrsSunburst.vue';

export default {
  components: {
    BackButtonText,
    TrsSunburst,
  },
  setup() {
    return {
      trainingtext: 'Trainingsempfehlung basierend auf Zyklusphase und TRS. Lorem ipsum dolor sit amet, consectetur adipiscing elit',
    }
  },
  methods: {
    navigateToTrsInfoPage() {
      this.$router.push({ name: 'TrsInfoPage' });
    }
  },
}
</script>
