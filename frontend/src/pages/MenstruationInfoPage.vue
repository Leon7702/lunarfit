<template>
  <div>
    <BackButtonText />
    <q-card flat bordered class="my-card">
      <q-card-section>
        <div class="text-h6">Menstruation</div>
      </q-card-section>

      <q-card-section>
        Der Zyklus beginnt mit dem ersten Tag der Blutung, die durch den Abfall con Progesteron und Östrogen ausgelöst
        wird.
        Das steigende Östrogen hebt die Launer, macht selbstbewusst und kreativ.
      </q-card-section>
    </q-card>

    <PhaseInformation textErnaehrung="Probeotische Lebensmittel: Frische Sprossen, Sauerkraut"
      textSport="Die Sauerstoffaufnahme ist erhöht und die Erholungsfähigkeit verbessert sich. Kraftaufbau.
      Intervalltraining, Schnelligkeitstraining, neue Belastungsreite, hohe Intensität."
      textGesundheit="Text für Gesundheit" />
  </div>
</template>

<script>
import BackButtonText from 'components/BackButtonText.vue';
import PhaseInformation from 'src/components/PhaseInformation.vue';

export default {
  components: {
    BackButtonText,
    PhaseInformation,
  },
}
</script>

<style scoped>
/* Add your styles here */
</style>
