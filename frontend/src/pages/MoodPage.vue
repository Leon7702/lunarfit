<template>
  <div class="size-container">
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
.header {
  display: flex;
  align-items: center;
  position: relative;
  padding-bottom: 20px;
}

.navButton {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 40px;
  height: 40px;
  cursor: pointer;
  position: absolute;
  left: 10px;
}

.navButtonImage {
  width: 20px;
  height: 20px;
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
  flex: 1;
  padding-bottom: 0px;
  /* Adjust this if necessary to avoid overlap with the sticky button */
}

.button-container {
  position: fixed;
  bottom: 20px;
  /* Adjust this value if necessary to ensure it's above the toolbar */
  left: 0;
  width: 100%;
  display: flex;
  justify-content: center;
  padding-bottom: 60px;
  padding-top: 16px;

  background-color: white;
  z-index: 1000;
}

.save-button {
  background-color: #50c1ba;
  color: white;
  border: none;
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
  border-radius: 5px;
}

.save-button:hover {
  background-color: #3b9991;
}
</style>
