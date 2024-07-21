<template>
  <div class="size-container">
    <div class="header">
      <router-link to="/calendar" class="navButton">
        <img src="/src/assets/arrow-left.svg" alt="Left" class="navButtonImage">
      </router-link>
      <div class="head">{{ $t('symptoms') }}</div>
    </div>

    <div class="container">
      <IconSlider v-for="(item, index) in symptomItems" :key="index" :icon="item.icon" :text="item.text" />
    </div>

    <div class="button-container">
      <button class="save-button" @click="redirectToCalendarPage">{{ $t('save') }}</button>
    </div>
  </div>
</template>

<script>
import { useRouter } from 'vue-router';
import IconSlider from 'components/IconSlider.vue';

export default {
  components: {
    IconSlider
  },
  data() {
    return {
      symptomItems: [
        { icon: '💨', text: this.$t('symptomsList.bloating') },
        { icon: '🍒', text: this.$t('symptomsList.breastPain') },
        { icon: '🚽', text: this.$t('symptomsList.diarrhea') },
        { icon: '😓', text: this.$t('symptomsList.exhaustion') },
        { icon: '🥶', text: this.$t('symptomsList.cold') },
        { icon: '🍫', text: this.$t('symptomsList.cravings') },
        { icon: '😡', text: this.$t('symptomsList.irritability') },
        { icon: '🤕', text: this.$t('symptomsList.aches') },
        { icon: '🥵', text: this.$t('symptomsList.hotFlashes') },
        { icon: '🤯', text: this.$t('symptomsList.headaches') },
        { icon: '💢', text: this.$t('symptomsList.cramps') },
        { icon: '😴', text: this.$t('symptomsList.fatigue') },
        { icon: '🛏️', text: this.$t('symptomsList.sleepIssues') },
        { icon: '😵‍💫', text: this.$t('symptomsList.dizziness') },
        { icon: '📉', text: this.$t('symptomsList.moodSwings') },
        { icon: '😵', text: this.$t('symptomsList.weakness') },
        { icon: '🤢', text: this.$t('symptomsList.nausea') },
        { icon: '🍪', text: this.$t('symptomsList.acne') },
        { icon: '🔴', text: this.$t('symptomsList.pelvicPain') },
        { icon: '🪨', text: this.$t('symptomsList.constipation') },
      ],
    };
  },
  methods: {
    redirectToCalendarPage() {
      const router = useRouter();
      router.push('/calendar');
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
  background-color: #0056b3;
}
</style>
