<script setup>
// import TheWelcome from '../components/TheWelcome.vue'
import ZyklusOverview from '../components/ZyklusOverview.vue'
import TrainingOverview from '../components/TrainingOverview.vue'
import Toolbar from '../components/Toolbar.vue'

</script>

<template>
  <main>
    <h1>Das wird das zukünftige Dashboard werden.</h1>
    <ZyklusOverview />
    <TrainingOverview />
  </main>
  <footer>
    <Toolbar />
  </footer>
</template>

<style scoped>
body {
  background-color: #f5f5f5;
}

footer {
  position: fixed;
  bottom: 0;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
