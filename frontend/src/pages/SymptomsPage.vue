<template>
  <div class="size-container">
    <div class="header">
      <q-btn flat dense round icon="arrow_back" @click="goBack" />
      <div class="head">{{ $t('symptoms') }}</div>
    </div>

    <q-input v-model="selectedDate" label="Select Date" type="date" @input="fetchSymptoms" />

    <div class="container">
      <IconSlider v-for="(item, index) in symptomItems" :key="index" :icon="item.icon" :text="item.text"
        :value="item.strength" :showSlider="item.tracked" @update:value="updateStrength(index, $event)"
        @update:tracked="updateTracked(index, $event)" />
    </div>
  </div>
</template>

<script>
import { ref, watch } from 'vue';
import { useRouter } from 'vue-router';
import IconSlider from 'components/IconSlider.vue';
import { QBtn, QInput } from 'quasar';
import { api } from 'src/boot/axios';

export default {
  components: {
    IconSlider,
    QBtn,
    QInput
  },
  setup() {
    const selectedDate = ref(new Date().toISOString().substr(0, 10));
    const symptomItems = ref(getInitialSymptomItems());
    const initialSymptoms = ref([]);
    const router = useRouter();

    function getInitialSymptomItems() {
      return [
        { icon: '💨', text: 'Bloating', strength: 0, tracked: false, id: null },
        { icon: '🍒', text: 'Breast Pain', strength: 0, tracked: false, id: null },
        { icon: '🚽', text: 'Diarrhea', strength: 0, tracked: false, id: null },
        { icon: '😓', text: 'Exhaustion', strength: 0, tracked: false, id: null },
        { icon: '🥶', text: 'Cold', strength: 0, tracked: false, id: null },
        { icon: '🍫', text: 'Cravings', strength: 0, tracked: false, id: null },
        { icon: '😡', text: 'Irritability', strength: 0, tracked: false, id: null },
        { icon: '🤕', text: 'Aches', strength: 0, tracked: false, id: null },
        { icon: '🥵', text: 'Hot Flashes', strength: 0, tracked: false, id: null },
        { icon: '🤯', text: 'Headaches', strength: 0, tracked: false, id: null },
        { icon: '💢', text: 'Cramps', strength: 0, tracked: false, id: null },
        { icon: '😴', text: 'Fatigue', strength: 0, tracked: false, id: null },
        { icon: '🛏️', text: 'Sleep Issues', strength: 0, tracked: false, id: null },
        { icon: '😵‍💫', text: 'Dizziness', strength: 0, tracked: false, id: null },
        { icon: '📉', text: 'Mood Swings', strength: 0, tracked: false, id: null },
        { icon: '😵', text: 'Weakness', strength: 0, tracked: false, id: null },
        { icon: '🤢', text: 'Nausea', strength: 0, tracked: false, id: null },
        { icon: '🍪', text: 'Acne', strength: 0, tracked: false, id: null },
        { icon: '🔴', text: 'Pelvic Pain', strength: 0, tracked: false, id: null },
        { icon: '🪨', text: 'Constipation', strength: 0, tracked: false, id: null },
      ];
    }

    function updateStrength(index, value) {
      console.log(`Updating strength of symptom at index ${index} to ${value}`);
      symptomItems.value[index].strength = value;
      symptomItems.value[index].tracked = value > 0;
      saveSymptom(index);
    }

    function updateTracked(index, tracked) {
      console.log(`Updating tracked status of symptom at index ${index} to ${tracked}`);
      symptomItems.value[index].tracked = tracked;
      if (!tracked) {
        deleteSymptom(index);
      } else {
        saveSymptom(index);
      }
    }

    async function fetchSymptoms() {
      console.log('Fetching symptoms for date:', selectedDate.value);
      symptomItems.value = getInitialSymptomItems(); // Reset symptom items
      try {
        const response = await api.get('/symptoms', {
          params: { date: selectedDate.value }
        });
        const fetchedSymptoms = response.data.results.filter(symptom => symptom.date === selectedDate.value);
        console.log('Fetched Symptoms:', fetchedSymptoms);

        fetchedSymptoms.forEach(symptom => {
          const symptomIndex = symptom.symptom_category - 1;
          symptomItems.value[symptomIndex] = {
            ...symptomItems.value[symptomIndex],
            id: symptom.id,
            strength: symptom.strength,
            tracked: true
          };
        });

        // Store the initial state of the symptoms
        initialSymptoms.value = fetchedSymptoms.map(symptom => ({
          id: symptom.id,
          symptom_category: symptom.symptom_category,
          strength: symptom.strength
        }));
      } catch (error) {
        console.error('Error fetching symptoms:', error);
      }
    }

    async function saveSymptom(index) {
      const symptom = symptomItems.value[index];
      const initialSymptom = initialSymptoms.value.find(item => item.symptom_category === index + 1);

      const requestBody = {
        date: selectedDate.value,
        strength: symptom.strength,
        symptom_category: index + 1,
      };

      try {
        if (!initialSymptom) {
          if (symptom.tracked) {
            console.log('Creating new symptom:', requestBody);
            const response = await api.post('/symptoms/', requestBody);
            symptomItems.value[index].id = response.data.id;
            initialSymptoms.value.push({ ...requestBody, id: response.data.id });
          }
        } else if (symptom.strength > 0 && symptom.strength !== initialSymptom.strength) {
          console.log('Deleting and re-creating symptom:', initialSymptom);
          await api.delete(`/symptoms/${initialSymptom.id}/`);
          const response = await api.post('/symptoms/', requestBody);
          symptomItems.value[index].id = response.data.id;
          initialSymptoms.value = initialSymptoms.value.map(item =>
            item.symptom_category === index + 1 ? { ...item, ...requestBody, id: response.data.id } : item
          );
        } else if (symptom.strength === 0) {
          console.log('Deleting symptom:', initialSymptom);
          await api.delete(`/symptoms/${initialSymptom.id}/`);
          symptomItems.value[index].id = null;
          initialSymptoms.value = initialSymptoms.value.filter(item => item.symptom_category !== index + 1);
        }
      } catch (error) {
        console.error('Error saving symptom:', error);
      }
    }

    async function deleteSymptom(index) {
      const symptom = symptomItems.value[index];
      if (symptom.id) {
        try {
          await api.delete(`/symptoms/${symptom.id}/`);
          console.log('Deleted symptom:', symptom);
        } catch (error) {
          console.error('Error deleting symptom:', error);
        }
      }
      symptomItems.value[index] = {
        ...symptomItems.value[index],
        strength: 0,
        tracked: false,
        id: null
      };
    }

    function goBack() {
      router.go(-1);
    }

    watch(selectedDate, fetchSymptoms);

    fetchSymptoms();

    return {
      selectedDate,
      symptomItems,
      initialSymptoms,
      updateStrength,
      updateTracked,
      fetchSymptoms,
      deleteSymptom,
      goBack,
    };
  },
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
  margin-bottom: 20px;
}
</style>
