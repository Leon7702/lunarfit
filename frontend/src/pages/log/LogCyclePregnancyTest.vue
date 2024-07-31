<template>
  <div class="size-container">
    <div class="welcome-container">
      <div class="header">
        <q-btn flat dense round icon="arrow_back" @click="goBack" />
        <div class="title">{{ $t('logCycle.pregnancyTest.title') }}</div>
      </div>
      <div class="linie"></div>
      <p class="description">
        {{ $t('logCycle.pregnancyTest.description') }}
      </p>
      <div class="icon-grid">
        <div
          class="icon-item"
          v-for="(item, index) in iconItems"
          :key="index"
          @click="selectItem(index)"
          :class="{ selected: selectedIndex === index }"
        >
          <div class="icon-wrapper">
            <img :src="item.icon" class="icon" />
            <div class="icon-circle" :class="{ active: selectedIndex === index }"></div>
          </div>
          <div class="icon-label">{{ item.label }}</div>
        </div>
      </div>
      <div class="button-container">
        <StandardButton :label="$t('buttons.save')" @click="saveCycleData" />
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useAuthStore } from 'src/stores/auth';
import { api } from 'src/boot/axios';
import StandardButton from 'components/StandardButton.vue';

export default {
  components: {
    StandardButton
  },
  data() {
    return {
      iconItems: [],
      selectedIndex: null
    };
  },
  computed: {
    localizedIcons() {
      return {
        positive: this.$t('logCycle.pregnancyTest.icons.positive'),
        negative: this.$t('logCycle.pregnancyTest.icons.negative'),
        invalid: this.$t('logCycle.pregnancyTest.icons.invalid')
      };
    }
  },
  watch: {
    '$i18n.locale': 'updateIconItems'
  },
  methods: {
    goBack() {
      window.history.back();
    },
    selectItem(index) {
      this.selectedIndex = index;
    },
    updateIconItems() {
      this.iconItems = [
        { icon: this.localizedIcons.positive},
        { icon: this.localizedIcons.negative },
        { icon: this.localizedIcons.invalid}
      ];
    },
    async saveCycleData() {
      if (this.selectedIndex === null) {
        return;
      }

      const valueMapping = {
        positive: 0,
        negative: 1,
        invalid: 2
      };

      const requestBody = {
        date: new Date().toISOString().split('T')[0], 
        type: 7,
        value: valueMapping[Object.keys(this.localizedIcons)[this.selectedIndex]]
      };

      const authStore = useAuthStore();

      try {
        await authStore.refreshAccessToken(); 

        await api.post('/cycles/log/', requestBody, {
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${authStore.accessToken}`
          }
        });

      } catch (error) {
        console.error('Fehler beim Speichern der Zyklusdaten', error);

        if (error.response) {
          if (error.response.status === 400) {
            alert('Fehlerhafte Anfrage. Bitte überprüfen Sie Ihre Eingaben.');
          } else if (error.response.status === 401) {
            alert('Nicht autorisiert. Bitte melden Sie sich erneut an.');
          } else {
            alert('Fehler beim Speichern der Zyklusdaten.');
          }
        } else if (error.request) {
          alert('Keine Antwort vom Server. Bitte überprüfen Sie Ihre Internetverbindung.');
        } else {
          alert('Ein unbekannter Fehler ist aufgetreten.');
        }
      }
    }
  },
  created() {
    this.updateIconItems();
  }
};
</script>


<style scoped>
.linie {
  height: 1px;
  background-color: rgba(0, 0, 0, 0.1);
  width: 120%;
  margin-top: 10px;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  padding: 10px 0;
  margin-top: 20px;
}

.title {
  font: 600 20px 'Inter', sans-serif;
  color: #000;
  text-align: center;
  flex-grow: 1;
  padding-right: 30px;
}

.description {
  text-align: left;
  width: 100%;
  margin-top: 30px;
  font-size: 16px;
  font-weight: 500;
}

.icon-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(100px, 1fr));
  width: 100%;
  max-width: 600px;
  justify-content: center;
}

.icon-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 12px;
  cursor: pointer;
}

.icon-wrapper {
  position: relative;
  width: 140px;
  height: 240px;
}

.icon {
  width: 100%;
  height: 100%;
}

.icon-circle {
  position: absolute;
  bottom: 15px;
  left: 50%;
  transform: translateX(-50%);
  width: 25px;
  height: 25px;
  border-radius: 50%;
  background-color: lightgray;
  transition: background-color 0.3s;
}

.icon-circle.active {
  background-color: var(--q-primary);
}

.button-container {
  position: fixed;
  bottom: 80px;  
  width: 100%;
  display: flex;
  justify-content: center;
  left: 0;
}
</style>
