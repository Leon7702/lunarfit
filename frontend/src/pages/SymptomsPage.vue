<template>
  <div class="root">
    <div class="header">
      <router-link to="/calendar" class="navButton">
        <img src="/src/assets/arrow-left.svg" alt="Left" class="navButtonImage">
      </router-link>
      <div class="head">Symptome</div>
    </div>

    <div class="container">
      <IconSlider
        v-for="(item, index) in symptomItems"
        :key="index"
        :icon="item.icon"
        :text="item.text"
      />
    </div>
    
    <div class="button-container">
      <button class="save-button" @click="redirectToCalendarPage">Speichern</button>
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
        { icon: '/src/assets/LunaFit.svg', text: 'Blähungen' },
        { icon: '/src/assets/icon2.svg', text: 'Brustschmerzen' },
        { icon: '/src/assets/icon3.svg', text: 'Durchfall' },
        { icon: '/src/assets/icon2.svg', text: 'Erschöpfung' },
        { icon: '/src/assets/icon2.svg', text: 'Frieren' },
        { icon: '/src/assets/icon2.svg', text: 'Gelüste' },
        { icon: '/src/assets/icon2.svg', text: 'Gereiztheit' },
        { icon: '/src/assets/icon2.svg', text: 'Gliederschmerzen' },
        { icon: '/src/assets/icon2.svg', text: 'Hitzewallungen' },
        { icon: '/src/assets/icon2.svg', text: 'Kopfschmerzen' },
        { icon: '/src/assets/icon2.svg', text: 'Krämpfe' },
        { icon: '/src/assets/icon2.svg', text: 'Müdigkeit' },
        { icon: '/src/assets/icon2.svg', text: 'Schlafstörungen' },
        { icon: '/src/assets/icon2.svg', text: 'Schwindelgefühl' },
        { icon: '/src/assets/icon2.svg', text: 'Stimmungsschwankungen' },
        { icon: '/src/assets/icon2.svg', text: 'Schwächegefühl' },
        { icon: '/src/assets/icon2.svg', text: 'Übelkeit' },
        { icon: '/src/assets/icon2.svg', text: 'Unreine Haut' },
        { icon: '/src/assets/icon2.svg', text: 'Unterleibsschmerzen' },
        { icon: '/src/assets/icon2.svg', text: 'Verstopfung' },
      ]
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
.root {
  width: 90%;
  margin: 0 auto; /* Centers the content horizontally */
  display: flex;
  flex-direction: column;
  min-height: 100vh; /* Ensure the root takes full viewport height */
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
  flex: 1; /* This will make the container take the available space */
}

.button-container {
  display: flex;
  justify-content: center;
  padding: 20px 0; /* Add some padding for spacing */
}

.save-button {
  background-color: #50c1ba; /* Change this to your preferred color */
  color: white;
  border: none;
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
  border-radius: 5px;
}

.save-button:hover {
  background-color: #0056b3; /* Change this to your preferred hover color */
}
</style>
