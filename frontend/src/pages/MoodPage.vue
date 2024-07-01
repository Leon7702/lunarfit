<template>
  <div class="root">
    <div class="header">
      <router-link to="/calendar" class="navButton">
        <img src="/src/assets/arrow-left.svg" alt="Left" class="navButtonImage">
      </router-link>
      <div class="head">Stimmung</div>
    </div>

    <div class="container">
      <IconSlider v-for="(item, index) in moodItems" :key="index" :icon="item.icon" :text="item.text"
        :value="item.value" @update:value="updateMoodValue(index, $event)" />
    </div>

    <div class="button-container">
      <button class="save-button">Speichern</button>
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
        { icon: '😰', text: this.$t('moods.anxious'), value: 1 },
        { icon: '🤩', text: this.$t('moods.excited'), value: 1 },
        { icon: '🤩', text: this.$t('moods.relaxed'), value: 1 },
        { icon: '💆', text: this.$t('moods.fit'), value: 1 },
        { icon: '🫤', text: this.$t('moods.frustrated'), value: 1 },
        { icon: '😄', text: this.$t('moods.happy'), value: 1 },
        { icon: '🤯', text: this.$t('moods.stressed'), value: 1 },
        { icon: '😴', text: this.$t('moods.tired'), value: 1 },
        { icon: '🫨', text: this.$t('moods.nervous'), value: 1 },
        { icon: '😵', text: this.$t('moods.weak'), value: 1 },
        { icon: '😎', text: this.$t('moods.confident'), value: 1 },
        { icon: '😔', text: this.$t('moods.sad'), value: 1 },
        { icon: '🙁', text: this.$t('moods.unhappy'), value: 1 },
        { icon: '😶‍🌫️', text: this.$t('moods.insecure'), value: 1 },
        { icon: '😠', text: this.$t('moods.angry'), value: 1 },
        { icon: '😳', text: this.$t('moods.embarrassed'), value: 1 },
        { icon: '❓', text: this.$t('moods.confused'), value: 1 },
        { icon: '😤', text: this.$t('moods.furious'), value: 1 },
        { icon: '😊', text: this.$t('moods.satisfied'), value: 1 },
        { icon: '😉', text: this.$t('moods.optimistic'), value: 1 },
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
  margin: 0 auto;
  /* Centers the content horizontally */
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  /* Ensure the root takes full viewport height */
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
  width: 40px;
  /* Increase this value to make the clickable area larger */
  height: 40px;
  /* Increase this value to make the clickable area larger */
  cursor: pointer;
  position: absolute;
  /* Position relative to header */
  left: 10px;
  /* Align to the left side */
}

.navButtonImage {
  width: 20px;
  /* Adjust the size of the actual image */
  height: 20px;
  /* Adjust the size of the actual image */
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
  flex: 1;
  /* This will make the container take the available space */
}

.button-container {
  display: flex;
  justify-content: center;
  padding: 20px 0;
  /* Add some padding for spacing */
}

.save-button {
  background-color: #50c1ba;
  /* Change this to your preferred color */
  color: white;
  border: none;
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
  border-radius: 5px;
}

.save-button:hover {
  background-color: #0056b3;
  /* Change this to your preferred hover color */
}
</style>
