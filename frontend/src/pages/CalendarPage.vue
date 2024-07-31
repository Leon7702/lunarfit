<template>
  <div class="size-container">
    <q-page class="q-pa-md">
      <div class="header q-mb-md q-gutter-sm flex justify-between items-center">
        <q-btn flat dense round icon="arrow_back" @click="prevMonth" />
        <div class="month-year text-h5">{{ currentMonth }} {{ currentYear }}</div>
        <q-btn flat dense round icon="arrow_forward" @click="nextMonth" />
      </div>

      <div v-if="loadingCalendar" class="q-mt-md flex flex-center">
        <q-spinner color="primary" size="2em" />
      </div>

      <div v-else class="custom-table-container">
        <q-table :rows="weeksInMonth" :columns="columns" row-key="weekIndex" flat dense :rows-per-page-options="[]"
          hide-bottom class="custom-table">
          <template v-slot:header="props">
            <q-tr :props="props">
              <q-th v-for="col in props.cols" :key="col.name" :props="props" class="custom-header">
                {{ col.label }}
              </q-th>
            </q-tr>
          </template>
          <template v-slot:body="props">
            <q-tr :props="props" class="custom-row">
              <q-td v-for="(day, dayIndex) in props.row.days" :key="dayIndex" class="custom-cell">
                <div :class="['day-circle', day.colorClass, { 'non-clickable': !day.date }]"
                  @click="day.date && selectDay(day)">
                  {{ day.date }}
                </div>
              </q-td>
            </q-tr>
          </template>
        </q-table>
      </div>

      <div class="legend q-mt-md">
        <div class="legend-item q-gutter-sm flex flex-center">
          <div class="legend-circle period"></div>
          <span class="legend-label">{{ $t('calendarLegend[0]') }}</span>
        </div>
        <div class="legend-item q-gutter-sm flex flex-center">
          <div class="legend-circle prediction"></div>
          <span class="legend-label">{{ $t('calendarLegend[1]') }}</span>
        </div>
        <div class="legend-item q-gutter-sm flex flex-center">
          <div class="legend-circle follicle"></div>
          <span class="legend-label">{{ $t('calendarLegend[2]') }}</span>
        </div>
      </div>

      <div class="day-log-container q-mt-md">
        <div class="day-log-header q-gutter-sm flex justify-between items-center">
          <div class="current-day">{{ currentDayFormatted }}</div>
          <q-btn class="log-button" no-caps rounded color="primary" label="+ Log" @click="log" />
        </div>
        <q-separator spaced />
      </div>

      <q-card class="cycle-phase-container subtle-card q-mt-md">
        <q-card-section>
          <div class="cycle-phase-header">{{ $t('training-recommendation.title') }}</div>
          <div v-if="loadingCyclePhase" class="q-mt-md flex flex-center">
            <q-spinner color="primary" size="2em" />
          </div>
          <div v-else>
            <div v-if="showFutureRecommendation" class="cycle-phase-text">{{ $t(phaseTextKey) }}</div>
            <div v-else-if="trainingReadinessScore > 0" class="training-recommendation-text">{{ $t(trainingTextKey +
              '.description') }}</div>
            <div v-else class="training-recommendation-text">{{ $t('training-recommendation.no-data') }}</div>
            <ul v-if="!showFutureRecommendation && trainingReadinessScore > 0" class="training-recommendation-list">
              <li>{{ $t(trainingTextKey + '.recommendations[0]') }}</li>
              <li>{{ $t(trainingTextKey + '.recommendations[1]') }}</li>
              <li>{{ $t(trainingTextKey + '.recommendations[2]') }}</li>
              <li>{{ $t(trainingTextKey + '.recommendations[3]') }}</li>
            </ul>
          </div>
        </q-card-section>
      </q-card>

      <q-separator spaced />
      <SectionContainer :title="$t('symptoms')" link="/symptoms" :linkText="$t('add')" :emojis="symptomsEmojis"
        :loading="loadingSymptoms" />
      <q-separator spaced />

      <q-card class="notes-container q-mt-md">
        <q-card-section>
          <div class="notes-header">{{ $t('logNotes.title') }}</div>
          <div v-if="loadingNotes" class="q-mt-md flex flex-center">
            <q-spinner color="primary" size="2em" />
          </div>
          <div v-else class="notes-text">{{ noteContent || $t('logNotes.no_entry') }}</div>
        </q-card-section>
      </q-card>
    </q-page>
  </div>
</template>


<script>
import { QBtn, QSeparator, QPage, QTable, QTr, QTd, QCard, QCardSection } from 'quasar';
import SectionContainer from 'components/SectionContainer.vue';
import { api } from 'src/boot/axios';
import { calculateScore } from 'src/utils/scoreCalculator';
import {
  calculateCycleAndPhases,
  calculateCurrentDay,
  getCurrentCycle,
} from "src/utils/cyclePhaseCalculator.js";

export default {
  components: {
    SectionContainer,
    QBtn,
    QSeparator,
    QPage,
    QTable,
    QTr,
    QTd,
    QCard,
    QCardSection,
  },
  data() {
    const date = new Date();
    return {
      date: {
        year: date.getFullYear(),
        month: date.getMonth(),
        day: date.getDate(),
      },
      dayColors: {},
      selectedDay: date.getDate(),
      trainingRecommendation: '',
      trainingReadinessScore: 0,
      loadingTraining: true,
      symptomsEmojis: [],
      moodEmojis: [],
      loadingMood: true,
      loadingSymptoms: false,
      loadingNotes: true,
      loadingCyclePhase: true,
      columns: [
        { name: 'mon', label: this.$t('weekdays_short[1]'), align: 'center' },
        { name: 'tue', label: this.$t('weekdays_short[2]'), align: 'center' },
        { name: 'wed', label: this.$t('weekdays_short[3]'), align: 'center' },
        { name: 'thu', label: this.$t('weekdays_short[4]'), align: 'center' },
        { name: 'fri', label: this.$t('weekdays_short[5]'), align: 'center' },
        { name: 'sat', label: this.$t('weekdays_short[6]'), align: 'center' },
        { name: 'sun', label: this.$t('weekdays_short[0]'), align: 'center' },
      ],
      symptomList: [
        { icon: '💨', text: 'symptomsList.bloating' },
        { icon: '🍒', text: 'symptomsList.breastPain' },
        { icon: '🚽', text: 'symptomsList.diarrhea' },
        { icon: '😓', text: 'symptomsList.exhaustion' },
        { icon: '🥶', text: 'symptomsList.cold' },
        { icon: '🍫', text: 'symptomsList.cravings' },
        { icon: '😡', text: 'symptomsList.irritability' },
        { icon: '🤕', text: 'symptomsList.aches' },
        { icon: '🥵', text: 'symptomsList.hotFlashes' },
        { icon: '🤯', text: 'symptomsList.headaches' },
        { icon: '💢', text: 'symptomsList.cramps' },
        { icon: '😴', text: 'symptomsList.fatigue' },
        { icon: '🛏️', text: 'symptomsList.sleepIssues' },
        { icon: '😵‍💫', text: 'symptomsList.dizziness' },
        { icon: '📉', text: 'symptomsList.moodSwings' },
        { icon: '😵', text: 'symptomsList.weakness' },
        { icon: '🤢', text: 'symptomsList.nausea' },
        { icon: '🍪', text: 'symptomsList.acne' },
        { icon: '🔴', text: 'symptomsList.pelvicPain' },
        { icon: '🪨', text: 'symptomsList.constipation' },
      ],
      mensLengthPortion: null,
      follicularLengthPortion: null,
      ovulationLengthPortion: null,
      earlyLutealLengthPortion: null,
      lateLutealLengthPortion: null,
      phaseTextKey: '',
      currentDay: 16,
      cycleLength: null,
      currentDayData: null,
      noteContent: '',
      showFutureRecommendation: false,
    };
  },
  computed: {
    currentYear() {
      return this.date.year;
    },
    currentMonth() {
      const locale = this.$i18n.locale;
      return new Date(this.date.year, this.date.month, 1).toLocaleString(locale, { month: 'long' });
    },
    daysInMonth() {
      const date = new Date(this.date.year, this.date.month + 1, 0);
      return [...Array(date.getDate()).keys()].map(i => i + 1);
    },
    weeksInMonth() {
      const days = this.daysInMonth;
      const firstDay = (new Date(this.date.year, this.date.month, 1).getDay() + 6) % 7; // Adjust for Monday start
      const weeks = [];
      let week = [];

      if (firstDay > 0) {
        const prevMonthDays = this.getDaysInPreviousMonth().slice(-firstDay);
        week.push(...prevMonthDays.map(day => ({ date: day, colorClass: this.dayColorClass(day, -1) })));
      }

      days.forEach(day => {
        if (week.length === 7) {
          weeks.push({ weekIndex: weeks.length, days: week });
          week = [];
        }
        week.push({ date: day, colorClass: this.dayColorClass(day) });
      });

      if (week.length > 0 && week.length < 7) {
        const nextMonthDays = 7 - week.length;
        week.push(...Array(nextMonthDays).fill({ date: '', colorClass: this.dayColorClass('', 1) }));
      }
      if (week.length > 0) {
        weeks.push({ weekIndex: weeks.length, days: week });
      }

      return weeks;
    },
    currentDayFormatted() {
      const locale = this.$i18n.locale;
      const date = this.selectedDay !== null
        ? new Date(this.date.year, this.date.month, this.selectedDay)
        : new Date(this.date.year, this.date.month, this.date.day);
      return date.toLocaleDateString(locale, { weekday: 'long', day: '2-digit', month: 'long' });
    },
    trainingTextKey() {
      if (this.trainingReadinessScore <= 25) return "scores.1";
      if (this.trainingReadinessScore <= 50) return "scores.2";
      if (this.trainingReadinessScore <= 75) return "scores.3";
      return "scores.4";
    },
  },
  methods: {
    async fetchData() {
      try {
        const cyclesResponse = await api.get('/cycles');
        const cycles = cyclesResponse.data.results;

        if (cycles.length === 0) {
          return;
        }

        this.dayColors = this.processCycles(cycles);
        this.addFutureCycles(cycles);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    },
    async fetchSymptoms() {
      this.loadingSymptoms = true;
      const selectedDateString = this.formatSelectedDate();
      try {
        const response = await api.get('/symptoms', {
          params: { date: selectedDateString }
        });
        this.symptomsEmojis = response.data.results
          .filter(symptom => symptom.date === selectedDateString)
          .sort((a, b) => b.strength - a.strength) // Sort by strength, descending
          .slice(0, 6)
          .map(symptom => {
            const symptomData = this.symptomList[symptom.symptom_category - 1];
            return {
              emoji: symptomData.icon,
              label: this.$t(symptomData.text),
            };
          });
        this.loadingSymptoms = false;
      } catch (error) {
        console.error('Error fetching symptoms:', error);
        this.loadingSymptoms = false;
      }
    },
    async fetchTrainingRecommendation() {
      this.loadingTraining = true;
      try {
        const response = await api.get('/training/trs/', {
          params: { date: this.formatSelectedDate() }
        });
        const selectedDateData = response.data.results.find((entry) => entry.date === this.formatSelectedDate());

        if (selectedDateData) {
          // Adjust complaints value for calculation
          const adjustedDateData = {
            ...selectedDateData,
            complaints: 6 - selectedDateData.complaints
          };
          this.trainingReadinessScore = calculateScore(adjustedDateData);
        } else {
          this.trainingReadinessScore = 0;
        }
        this.loadingTraining = false;
      } catch (error) {
        console.error('Error fetching training recommendation:', error);
        this.loadingTraining = false;
      }
    },
    async fetchNote() {
      this.loadingNotes = true;
      try {
        const response = await api.get('/notes', {
          params: { date: this.formatSelectedDate() }
        });
        const noteData = response.data.results.find((entry) => entry.date === this.formatSelectedDate());
        this.noteContent = noteData ? noteData.content : '';
        this.loadingNotes = false;
      } catch (error) {
        console.error('Error fetching note:', error);
        this.loadingNotes = false;
      }
    },
    async fetchDataAndCalculatePhases() {
      this.loadingCyclePhase = true;
      try {
        const cycleResponse = await api.get('/cycles/');
        const cycleData = cycleResponse.data;

        const cycles = cycleData.results;
        if (Array.isArray(cycles)) {
          const currentCycle = getCurrentCycle(cycles, this.formatSelectedDate());
          if (currentCycle) {
            const calculatedLengths = calculateCycleAndPhases(currentCycle);

            this.cycleLength = calculatedLengths.cycleLength;
            this.mensLengthPortion = (calculatedLengths.phaseLengths[0].length / this.cycleLength) * 100;
            this.follicularLengthPortion = (calculatedLengths.phaseLengths[1].length / this.cycleLength) * 100;
            this.ovulationLengthPortion = (calculatedLengths.phaseLengths[2].length / this.cycleLength) * 100;
            this.earlyLutealLengthPortion = (calculatedLengths.phaseLengths[3].length / this.cycleLength) * 100;
            this.lateLutealLengthPortion = (calculatedLengths.phaseLengths[4].length / this.cycleLength) * 100;

            this.currentDay = calculateCurrentDay(currentCycle.start, this.formatSelectedDate());
            const currentPhase = (this.currentDay / this.cycleLength) * 100;

            if (currentPhase <= this.mensLengthPortion) {
              this.phaseTextKey = "menstruationPhaseText";
            } else if (currentPhase <= this.mensLengthPortion + this.follicularLengthPortion) {
              this.phaseTextKey = "follicularPhaseText";
            } else if (currentPhase <= this.mensLengthPortion + this.follicularLengthPortion + this.ovulationLengthPortion) {
              this.phaseTextKey = "ovulationPhaseText";
            } else if (currentPhase <= this.mensLengthPortion + this.follicularLengthPortion + this.ovulationLengthPortion + this.earlyLutealLengthPortion) {
              this.phaseTextKey = "earlyLutealPhaseText";
            } else {
              this.phaseTextKey = "lateLutealPhaseText";
            }
          }
        }
        this.loadingCyclePhase = false;
      } catch (error) {
        console.error('Error calculating phases:', error);
        this.loadingCyclePhase = false;
      }
    },
    processCycles(cycles) {
      const dayColors = {};

      cycles.forEach(cycle => {
        cycle.phases.forEach(phase => {
          const start = new Date(phase.start);
          const end = new Date(phase.end);
          const phaseColorClass = this.getPhaseColorClass(phase.phase_number);

          for (let d = new Date(start); d <= end; d.setDate(d.getDate() + 1)) {
            const date = new Date(d);
            const day = date.getDate();
            const month = date.getMonth();
            const year = date.getFullYear();

            if (year === this.date.year && month === this.date.month) {
              dayColors[day] = phaseColorClass;
            } else if (year === this.date.year && month === this.date.month - 1) {
              dayColors[`prev_${day}`] = phaseColorClass;
            } else if (year === this.date.year && month === this.date.month + 1) {
              dayColors[`next_${day}`] = phaseColorClass;
            }
          }
        });
      });

      return dayColors;
    },
    addFutureCycles(cycles) {
      const lastCycle = cycles[cycles.length - 1];
      const avgCycleLength = this.calculateAverageCycleLength(cycles);
      const futureCycles = this.calculateFutureCycles(lastCycle, avgCycleLength, 3);

      futureCycles.forEach(cycle => {
        cycle.phases.forEach(phase => {
          if (phase.phase_number == 0) { // Only add future phases that are not follicular
            const start = new Date(phase.start);
            const end = new Date(phase.end);
            const phaseColorClass = this.getPhaseColorClass(phase.phase_number, true);

            for (let d = new Date(start); d <= end; d.setDate(d.getDate() + 1)) {
              const date = new Date(d);
              const day = date.getDate();
              const month = date.getMonth();
              const year = date.getFullYear();

              if (year === this.date.year && month === this.date.month) {
                this.dayColors[day] = phaseColorClass;
              } else if (year === this.date.year && month === this.date.month - 1) {
                this.dayColors[`prev_${day}`] = phaseColorClass;
              } else if (year === this.date.year && month === this.date.month + 1) {
                this.dayColors[`next_${day}`] = phaseColorClass;
              }
            }
          }
        });
      });
    },
    calculateAverageCycleLength(cycles) {
      const totalLength = cycles.reduce((acc, cycle) => {
        return acc + (new Date(cycle.end) - new Date(cycle.start)) / (1000 * 60 * 60 * 24) + 1;
      }, 0);
      return Math.round(totalLength / cycles.length);
    },
    calculateFutureCycles(lastCycle, avgCycleLength, months) {
      const futureCycles = [];
      let startDate = new Date(lastCycle.end);
      startDate.setDate(startDate.getDate() + 1);

      for (let i = 0; i < months; i++) {
        const phases = lastCycle.phases.map(phase => {
          const start = new Date(startDate);
          startDate.setDate(startDate.getDate() + phase.avg_duration - 1);
          const end = new Date(startDate);
          startDate.setDate(startDate.getDate() + 1);
          return {
            ...phase,
            start: start.toISOString().split('T')[0],
            end: end.toISOString().split('T')[0],
          };
        });

        futureCycles.push({
          ...lastCycle,
          phases,
          start: phases[0].start,
          end: phases[phases.length - 1].end,
        });

        startDate = new Date(phases[phases.length - 1].end);
        startDate.setDate(startDate.getDate() + 1);
      }

      return futureCycles;
    },
    getPhaseColorClass(phaseNumber, isFuture = false) {
      if (isFuture) {
        if (phaseNumber === 0) return 'prediction';
        return '';
      }
      switch (phaseNumber) {
        case 0:
          return 'period';
        case 1:
          return 'follicle';
        default:
          return '';
      }
    },
    nextMonth() {
      if (this.date.month === 11) {
        this.date.year++;
        this.date.month = 0;
      } else {
        this.date.month++;
      }
      this.fetchData(); // Fetch data when changing month
    },
    prevMonth() {
      if (this.date.month === 0) {
        this.date.year--;
        this.date.month = 11;
      } else {
        this.date.month--;
      }
      this.fetchData(); // Fetch data when changing month
    },
    dayColorClass(day, offset = 0) {
      const monthKey = offset === -1 ? `prev_${day}` : offset === 1 ? `next_${day}` : day;
      if (this.selectedDay === day && offset === 0) {
        return 'currentDate';
      }
      return this.dayColors[monthKey] || (offset !== 0 ? 'previous-month' : '');
    },
    async selectDay(day) {
      if (day.colorClass === 'previous-month') {
        const selectedDate = new Date(this.date.year, this.date.month - 1, day.date);
        this.selectedDay = selectedDate.getDate();
        this.date.year = selectedDate.getFullYear();
        this.date.month = selectedDate.getMonth();
      } else if (day.colorClass === 'next-month') {
        const selectedDate = new Date(this.date.year, this.date.month + 1, day.date);
        this.selectedDay = selectedDate.getDate();
        this.date.year = selectedDate.getFullYear();
        this.date.month = selectedDate.getMonth();
      } else if (day.date !== '') {
        this.selectedDay = day.date;
      } else {
        this.selectedDay = null;
      }
      await this.fetchSymptoms();
      await this.fetchTrainingRecommendation(); // Fetch training recommendation when a day is selected
      await this.fetchNote(); // Fetch note when a day is selected
      await this.fetchDataAndCalculatePhases(); // Fetch and calculate phases when a day is selected
    },
    getDaysInPreviousMonth() {
      const date = new Date(this.date.year, this.date.month, 0);
      return [...Array(date.getDate()).keys()].map(i => i + 1);
    },
    formatSelectedDate() {
      const year = this.date.year;
      const month = String(this.date.month + 1).padStart(2, '0');
      const day = String(this.selectedDay).padStart(2, '0');
      return `${year}-${month}-${day}`;
    },
    log() {
      this.$router.push({
        path: '/symptoms',
        query: { selectedDate: this.formatSelectedDate() }
      });
    }
  },
  watch: {
    async selectedDay() {
      await this.fetchTrainingRecommendation();
      await this.fetchNote(); // Fetch note when the selected day changes
      await this.fetchDataAndCalculatePhases(); // Fetch and calculate phases when the selected day changes
    },
    async date() {
      await this.fetchTrainingRecommendation();
      await this.fetchNote(); // Fetch note when the date changes
      await this.fetchDataAndCalculatePhases(); // Fetch and calculate phases when the date changes
    }
  },
  mounted() {
    this.fetchData();
    this.fetchSymptoms();
    this.fetchTrainingRecommendation();
    this.fetchNote(); // Fetch note when the component is mounted
    this.fetchDataAndCalculatePhases(); // Fetch and calculate phases when the component is mounted
  }
};
</script>



<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');

* {
  font-family: 'Inter', sans-serif;
}

.q-page {
  padding: 16px;
  padding: 0;
  margin: 0;
}

.header .month-year {
  font-weight: 600;
}

.custom-table-container {
  display: flex;
  justify-content: center;
}

.custom-table {
  width: 100%;
  table-layout: fixed;
}

.custom-header {
  font-weight: 600;
}

.q-tr,
.q-td {
  text-align: center;
  cursor: pointer;
}

.q-th {
  font-weight: 600;
  text-align: center;
}

.q-td {
  padding: 0;
}

.q-td .q-td-inner {
  padding: 8px;
}

.q-td:first-child .q-td-inner,
.q-td:last-child .q-td-inner {
  padding-left: 8px;
  padding-right: 8px;
}

.q-td:not(:last-child) {
  border-right: 1px solid #e0e0e0;
}

.q-td:hover .day-circle {
  background-color: #ebfffc;
}

.q-td .day-circle {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 2rem;
  height: 2rem;
  border-radius: 50%;
  text-align: center;
  margin: auto;
}

.q-td .day-circle.non-clickable {
  cursor: default;
  background-color: transparent;
}

.period {
  background-color: #ffd8df;
  color: #ff2d55;
}

.follicle {
  background-color: #e7e7ff;
  color: black;
}

.prediction {
  border: 2px dotted #ff2d55;
  color: #000;
}

.currentDate {
  border: 2px solid #50c1ba;
  color: #000;
}

.previous-month {
  color: #b0b0b0;
}

.legend {
  display: flex;
  justify-content: space-evenly;
}

.legend-item {
  display: flex;
  align-items: center;
}

.legend-item .legend-circle {
  width: 1rem;
  height: 1rem;
  border-radius: 50%;
}

.legend-label {
  margin-left: 0.25rem;
  font-size: 0.75rem;
  color: #72777a;
}

a {
  color: #50c1ba;
  text-decoration: none;
}

a:visited {
  color: #50c1ba;
}

a:hover {
  text-decoration: none;
}

.day-log-container {
  width: 100%;
  margin: 20px auto;
}

.day-log-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.current-day {
  color: #090a0a;
  font-size: 1.125rem;
  font-weight: 600;
  margin-top: 5px;
}

.log-button {
  font-size: 0.875rem;
}

.training-recommendation-header {
  display: flex;
  justify-content: center;
  color: #000;
  font-size: 1rem;
  font-weight: 600;
  line-height: 1.5;
}

.training-recommendation-text {
  font-size: 0.875rem;
  font-weight: 400;
  line-height: 1.5;
  padding-top: 10px;
  text-align: center;
}

.training-recommendation-list {
  font-size: 0.875rem;
  font-weight: 400;
  line-height: 1.5;
  padding-top: 10px;
  text-align: left;
  list-style-type: disc;
  padding-left: 20px;
}

.loading-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
}

.subtle-card {
  background-color: #bce5e258;
  border: 2px solid #50c1ba;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  padding: 0px;
  margin-bottom: 20px;
}

.notes-container {
  background-color: #ffffff58;
  border: 2px solid #ffffff;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  padding: 0px;
  margin-top: 20px;
  margin-bottom: 20px;
}

.notes-header {
  display: flex;
  justify-content: left;
  color: #000;
  font-size: 1rem;
  font-weight: 600;
  line-height: 1.5;
}

.notes-text {
  font-size: 0.875rem;
  font-weight: 400;
  line-height: 1.5;
  padding-top: 10px;
  text-align: left;
}

.cycle-phase-container {
  background-color: #bce5e258;
  border: 2px solid #50c1ba;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  padding: 0px;
  margin-top: 20px;
  margin-bottom: 20px;
}

.cycle-phase-header {
  display: flex;
  justify-content: center;
  color: #000;
  font-size: 1rem;
  font-weight: 600;
  line-height: 1.5;
}

.cycle-phase-text {
  font-size: 0.875rem;
  font-weight: 400;
  line-height: 1.5;
  padding-top: 10px;
  text-align: center;
}
</style>
