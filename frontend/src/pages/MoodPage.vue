<template>
    <div class="root">
      <div class="header">
        <router-link to="/calendar" class="leftButton">
          <img src="/src/assets/arrow-left.svg" alt="Left">
        </router-link>
        <div class="head">Stimmung</div>
      </div>
  
      <div class="container">
        <IconCheckbox
          v-for="(item, index) in symptomItems"
          :key="index"
          :icon="item.icon"
          :text="item.text"
        />
      </div>
    </div>
  </template>
  
  <script>
  import { useRouter } from 'vue-router';
  import IconCheckbox from 'components/IconCheckbox.vue';
  
  export default {
    components: {
      IconCheckbox
    },
    data() {
      return {
        symptomItems: [
          { icon: '/src/assets/LunaFit.svg', text: 'Ängstlich' },
          { icon: '/src/assets/icon2.svg', text: 'Begeistert' },
          { icon: '/src/assets/icon3.svg', text: 'Entspannt' },
          { icon: '/src/assets/icon2.svg', text: 'Fit' },
          { icon: '/src/assets/icon2.svg', text: 'Frustriert' },
          { icon: '/src/assets/icon2.svg', text: 'Glücklich' },
          { icon: '/src/assets/icon2.svg', text: 'Gestresst' },
          { icon: '/src/assets/icon2.svg', text: 'Müde' },
          { icon: '/src/assets/icon2.svg', text: 'Nervös' },
          { icon: '/src/assets/icon2.svg', text: 'Schwach' },
          { icon: '/src/assets/icon2.svg', text: 'Selbstsicher' },
          { icon: '/src/assets/icon2.svg', text: 'Traurig' },
          { icon: '/src/assets/icon2.svg', text: 'Unglücklich' },
          { icon: '/src/assets/icon2.svg', text: 'Unsicher' },
          { icon: '/src/assets/icon2.svg', text: 'Verägert' },
          { icon: '/src/assets/icon2.svg', text: 'Verlegen' },
          { icon: '/src/assets/icon2.svg', text: 'Verwirrt' },
          { icon: '/src/assets/icon2.svg', text: 'Wütend' },
          { icon: '/src/assets/icon2.svg', text: 'Zufrieden' },
          { icon: '/src/assets/icon2.svg', text: 'Zuversichtlich' },
        ]
      };
    },
    methods: {
      redirectToCalendarPage() {
        const router = useRouter();
        router.push('/calendar'); // Assuming '/calendar' is the path to CalendarPage
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
    justify-content: center;
    align-items: center;
    position: relative;
    padding: 10px;
    padding-top: 46px;
    padding-bottom: 20px;
  }
  
  .leftButton {
    cursor: pointer; /* Makes it look like a button */
    position: absolute;
    left: 0;
  }
  
  .head {
    color: #000;
    text-align: center;
    font-size: 20px;
    font-style: normal;
    font-weight: 600;
    line-height: 31px;
  }
  
  .container {
    border-top: 1px solid #ccc;
  }
  </style>
