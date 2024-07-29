<template>
  <div class="size-container">
    <div class="header">
      <q-btn flat dense round icon="arrow_back" @click="goBack" />
      <div class="head">{{ $t('symptoms') }}</div>
    </div>

    <q-input v-model="selectedDate" label="Select Date" type="date" @input="fetchSymptoms" />

    <div class=" container">
      <IconSlider v-for="(item, index) in symptomItems" :key="index" :icon="item.icon" :text="item.text"
        :value="item.strength" :showSlider="item.tracked" @update:value="updateStrength(index, $event)"
        @update:tracked="updateTracked(index, $event)" />
    </div>

    <div class="button-container">
      <StandardButton :label="$t('save')" @click="saveSymptoms" />
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import IconSlider from 'components/IconSlider.vue';
import { QBtn, QInput } from 'quasar';
import { api } from 'src/boot/axios';
import StandardButton from 'components/StandardButton.vue';


export default {
  components: {
    IconSlider,
    QBtn,
    QInput,
    StandardButton
  },
  setup() {
    const selectedDate = ref(new Date().toISOString().substr(0, 10));
    const symptomItems = ref(getInitialSymptomItems());
    const initialSymptoms = ref([]);
    const router = useRouter();

    function getInitialSymptomItems() {
      return [
        { icon: '💨', text: 'Bloating', strength: 1, tracked: false },
        { icon: '🍒', text: 'Breast Pain', strength: 1, tracked: false },
        { icon: '🚽', text: 'Diarrhea', strength: 1, tracked: false },
        { icon: '😓', text: 'Exhaustion', strength: 1, tracked: false },
        { icon: '🥶', text: 'Cold', strength: 1, tracked: false },
        { icon: '🍫', text: 'Cravings', strength: 1, tracked: false },
        { icon: '😡', text: 'Irritability', strength: 1, tracked: false },
        { icon: '🤕', text: 'Aches', strength: 1, tracked: false },
        { icon: '🥵', text: 'Hot Flashes', strength: 1, tracked: false },
        { icon: '🤯', text: 'Headaches', strength: 1, tracked: false },
        { icon: '💢', text: 'Cramps', strength: 1, tracked: false },
        { icon: '😴', text: 'Fatigue', strength: 1, tracked: false },
        { icon: '🛏️', text: 'Sleep Issues', strength: 1, tracked: false },
        { icon: '😵‍💫', text: 'Dizziness', strength: 1, tracked: false },
        { icon: '📉', text: 'Mood Swings', strength: 1, tracked: false },
        { icon: '😵', text: 'Weakness', strength: 1, tracked: false },
        { icon: '🤢', text: 'Nausea', strength: 1, tracked: false },
        { icon: '🍪', text: 'Acne', strength: 1, tracked: false },
        { icon: '🔴', text: 'Pelvic Pain', strength: 1, tracked: false },
        { icon: '🪨', text: 'Constipation', strength: 1, tracked: false },
      ];
    }

    function updateStrength(index, value) {
      symptomItems.value[index].strength = value;
      if (value > 0) {
        symptomItems.value[index].tracked = true;
      } else {
        symptomItems.value[index].tracked = false;
      }
    }

    function updateTracked(index, tracked) {
      symptomItems.value[index].tracked = tracked;
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
            strength: symptom.strength,
            tracked: true
          };
        });

        // Store the initial state of the symptoms
        initialSymptoms.value = fetchedSymptoms.map(symptom => ({
          symptom_category: symptom.symptom_category,
          strength: symptom.strength
        }));
      } catch (error) {
        console.error('Error fetching symptoms:', error);
      }
    }

    async function saveSymptoms() {
      const trackedSymptoms = symptomItems.value.filter(item => item.tracked);
      console.log('Saving tracked symptoms:', trackedSymptoms);

      try {
        for (const symptom of trackedSymptoms) {
          const symptomIndex = symptomItems.value.findIndex(item => item.icon === symptom.icon);
          const initialSymptom = initialSymptoms.value.find(item => item.symptom_category === symptomIndex + 1);

          // Only send the symptom if it is new or has changed
          if (!initialSymptom || initialSymptom.strength !== symptom.strength) {
            const requestBody = {
              date: selectedDate.value,
              strength: symptom.strength,
              symptom_category: symptomIndex + 1,
            };
            console.log('Sending request body:', requestBody);
            await api.post('/symptoms/', requestBody);
          }
        }
        router.push('/calendar');
      } catch (error) {
        console.error('Error saving symptoms:', error);
      }
    }

    function goBack() {
      router.go(-1);
    }

    fetchSymptoms();

    return {
      selectedDate,
      symptomItems,
      initialSymptoms,
      updateStrength,
      updateTracked,
      fetchSymptoms,
      saveSymptoms,
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
  padding-bottom: 80px;
}

.button-container {
  position: fixed;
  bottom: 20px;
  /* Adjust this value if necessary to ensure it's above the toolbar */
  left: 0;
  width: 100%;
  display: flex;
  justify-content: center;
  padding-bottom: 40px;
  padding-top: 10px;
  background-color: white;
  z-index: 1000;
  height: 13%;
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
