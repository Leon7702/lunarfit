<template>
  <div class="root">
    <div class="header">
      <router-link to="/calendar" class="navButton">
        <img src="/src/assets/arrow-left.svg" alt="Left" class="navButtonImage">
      </router-link>
      <div class="head">Stimmung</div>
    </div>

    <div class="container">
      <IconSlider
        v-for="(item, index) in moodItems"
        :key="index"
        :icon="item.icon"
        :text="item.text"
        :value="item.value"
        @update:value="updateMoodValue(index, $event)"
      />
    </div>
  </div>
</template>

<script>
import IconSlider from 'components/IconSlider.vue';

export default {
  components: {
    IconSlider
  },
  data() {
    return {
      moodItems: [
        { icon: '/src/assets/LunaFit.svg', text: 'Ängstlich', value: 1 },
        { icon: '/src/assets/icon2.svg', text: 'Begeistert', value: 1 },
        { icon: '/src/assets/icon3.svg', text: 'Entspannt', value: 1 },
        { icon: '/src/assets/icon2.svg', text: 'Fit', value: 1 },
        { icon: '/src/assets/icon2.svg', text: 'Frustriert', value: 1 },
        { icon: '/src/assets/icon2.svg', text: 'Glücklich', value: 1 },
        { icon: '/src/assets/icon2.svg', text: 'Gestresst', value: 1 },
        { icon: '/src/assets/icon2.svg', text: 'Müde', value: 1 },
        { icon: '/src/assets/icon2.svg', text: 'Nervös', value: 1 },
        { icon: '/src/assets/icon2.svg', text: 'Schwach', value: 1 },
        { icon: '/src/assets/icon2.svg', text: 'Selbstsicher', value: 1 },
        { icon: '/src/assets/icon2.svg', text: 'Traurig', value: 1 },
        { icon: '/src/assets/icon2.svg', text: 'Unglücklich', value: 1 },
        { icon: '/src/assets/icon2.svg', text: 'Unsicher', value: 1 },
        { icon: '/src/assets/icon2.svg', text: 'Verägert', value: 1 },
        { icon: '/src/assets/icon2.svg', text: 'Verlegen', value: 1 },
        { icon: '/src/assets/icon2.svg', text: 'Verwirrt', value: 1 },
        { icon: '/src/assets/icon2.svg', text: 'Wütend', value: 1 },
        { icon: '/src/assets/icon2.svg', text: 'Zufrieden', value: 1 },
        { icon: '/src/assets/icon2.svg', text: 'Zuversichtlich', value: 1 },
      ]
    };
  },
  methods: {
    updateMoodValue(index, newValue) {
      this.moodItems[index].value = newValue;
    }
  }
};
</script>

<style scoped>
.root {
  width: 90%;
  margin: 0 auto; /* Centers the content horizontally */
}

.header {
  display: flex;
  align-items: center;
  position: relative;
  padding: 10px;
  padding-top: 46px;
  padding-bottom: 20px;
}

.navButton {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 40px; /* Increase this value to make the clickable area larger */
  height: 40px; /* Increase this value to make the clickable area larger */
  cursor: pointer;
  position: absolute; /* Position relative to header */
  left: 10px; /* Align to the left side */
}

.navButtonImage {
  width: 20px; /* Adjust the size of the actual image */
  height: 20px; /* Adjust the size of the actual image */
}

.head {
  color: #000;
  text-align: center;
  font-size: 20px;
  font-style: normal;
  font-weight: 600;
  line-height: 31px;
  margin: 0 auto;
  flex: 1;
}

.container {
  border-top: 1px solid #ccc;
}
</style>
