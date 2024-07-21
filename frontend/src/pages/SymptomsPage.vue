<template>
  <div class="size-container">
    <div class="header">
      <q-btn flat dense round icon="arrow_back" @click="goBack" />
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
import { QBtn } from 'quasar';

export default {
  components: {
    IconSlider,
    QBtn
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
    goBack() {
      this.$router.go(-1);
    },
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
  padding-bottom: 65px;
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
  padding-top: 10px;
  background-color: white;
  z-index: 1000;
  height: 110px;
}

.save-button {
  background-color: #50c1ba;
  color: white;
  border: none;
  padding: 10px 10px;
  font-size: 16px;
  cursor: pointer;
  border-radius: 5px;
}

.save-button:hover {
  background-color: #3b9991;
}
</style>
