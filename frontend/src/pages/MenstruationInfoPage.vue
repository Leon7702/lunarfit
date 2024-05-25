<template>
  <div>
    <BackButtonText />
    <q-card flat bordered class="my-card">
      <q-card-section>
        <div class="text-h6">Menstruation</div>
      </q-card-section>

      <q-card-section>
        Der Zyklus beginnt mit dem ersten Tag der Blutung, die durch den Abfall con Progesteron und Östrogen ausgelöst wird.
        Das steigende Östrogen hebt die Launer, macht selbstbewusst und kreativ.
      </q-card-section>
    </q-card>
  </div>
</template>

<script>
import BackButtonText from 'components/BackButtonText.vue';

export default {
  components: {
    BackButtonText,
  },
}
</script>

<style scoped>
/* Add your styles here */
</style>
