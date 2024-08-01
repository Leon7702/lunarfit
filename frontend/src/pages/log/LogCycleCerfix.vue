<template>
  <div class="size-container">
    <div class="welcome-container">
      <div class="header">
        <q-btn flat dense round icon="arrow_back" @click="goBack" />
        <div class="title">{{ $t('logCycle.cervix.title') }}</div>
      </div>
      <div class="linie"></div>
      <p class="description">
        {{ $t('logCycle.cervix.description') }}
      </p>
      <div class="icon-grid">
        <div
          class="icon-item"
          v-for="(item, index) in iconItems"
          :key="index"
          @click="handleIconClick(index)"
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
import { ref, watch, computed, onMounted } from 'vue';
import { useRouter } from 'vue-router'; 
import { useAuthStore } from 'src/stores/auth';
import { useI18n } from 'vue-i18n';
import { api } from 'src/boot/axios';
import StandardButton from 'components/StandardButton.vue';

export default {
  components: {
    StandardButton
  },
  setup() {
    const { t, locale } = useI18n();
    const router = useRouter();  
    const authStore = useAuthStore();
    const iconItems = ref([]);
    const selectedIndex = ref(null);
    const currentEntryId = ref(null);

    const localizedIcons = computed(() => ({
      none: t('logCycle.cervix.icons.none'),
      dry: t('logCycle.cervix.icons.dry'),
      creamy: t('logCycle.cervix.icons.creamy'),
      sticky: t('logCycle.cervix.icons.sticky'),
      protein: t('logCycle.cervix.icons.protein')
    }));

    const updateIconItems = () => {
      iconItems.value = [
        { icon: localizedIcons.value.none },
        { icon: localizedIcons.value.dry},
        { icon: localizedIcons.value.creamy },
        { icon: localizedIcons.value.sticky },
        { icon: localizedIcons.value.protein }
      ];
    };

    const goBack = () => {
      window.history.back();
    };

    const handleIconClick = async (index) => {
      if (selectedIndex.value === index) {
        await deleteCurrentEntry();
        selectedIndex.value = null;
        currentEntryId.value = null;
      } else {
        selectedIndex.value = index;
      }
    };

    const deleteCurrentEntry = async () => {
      if (currentEntryId.value === null) {
        return;
      }

      try {
        await authStore.refreshAccessToken();
        await api.delete(`/cycles/log/${currentEntryId.value}/`, {
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${authStore.accessToken}`
          }
        });
      } catch (error) {
        console.error('Fehler beim Löschen des Zyklusdatensatzes', error);
        alert('Fehler beim Löschen des Zyklusdatensatzes.');
      }
    };

    const fetchCurrentEntry = async () => {
      const today = new Date().toISOString().split('T')[0];
      try {
        await authStore.refreshAccessToken();
        const response = await api.get('/cycles/log/', {
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${authStore.accessToken}`
          },
          params: {
            type: 4,
            date: today
          }
        });

        if (response.data.results.length > 0) {
          const entry = response.data.results[0];
          currentEntryId.value = entry.id;

          const entryResponse = await api.get(`/cycles/log/${currentEntryId.value}/`, {
            headers: {
              'Content-Type': 'application/json',
              'Authorization': `Bearer ${authStore.accessToken}`
            }
          });

          selectedIndex.value = parseInt(entryResponse.data.value);
        } else {
          currentEntryId.value = null;
          selectedIndex.value = null;
        }
      } catch (error) {
        console.error('Fehler beim Abrufen der Zyklusdaten', error);
      }
    };

    const saveCycleData = async () => {
      if (selectedIndex.value === null) {
        return;
      }

      const valueMapping = {
        none: 0,
        dry: 1,
        creamy: 2,
        sticky: 3,
        protein: 4
      };

      const requestBody = {
        date: new Date().toISOString().split('T')[0],
        type: 4,
        value: valueMapping[Object.keys(localizedIcons.value)[selectedIndex.value]]
      };

      try {
        await authStore.refreshAccessToken();

        if (currentEntryId.value) {
          await api.patch(`/cycles/log/${currentEntryId.value}/`, requestBody, {
            headers: {
              'Content-Type': 'application/json',
              'Authorization': `Bearer ${authStore.accessToken}`
            }
          });
        } else {
          const response = await api.post('/cycles/log/', requestBody, {
            headers: {
              'Content-Type': 'application/json',
              'Authorization': `Bearer ${authStore.accessToken}`
            }
          });
          currentEntryId.value = response.data.id;
        }

        router.push('/log-cycle');

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
    };

    onMounted(() => {
      updateIconItems();
      fetchCurrentEntry();
    });

    watch(locale, updateIconItems);

    return {
      iconItems,
      selectedIndex,
      goBack,
      handleIconClick,
      saveCycleData
    };
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
  width: 180px; /* 60px * 3 */
  height: 180px; /* 60px * 3 */
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
