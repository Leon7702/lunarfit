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
                <div :class="['day-circle', day.colorClass]" @click="selectDay(day)">
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

      <q-card class="training-recommendation-container subtle-card q-mt-md">
        <q-card-section>
          <div class="training-recommendation-header">{{ $t('training-recommendation.title') }}</div>
          <div v-if="loadingTraining" class="q-mt-md flex flex-center">
            <q-spinner color="primary" size="2em" />
          </div>
          <div v-else class="training-recommendation-text">{{ trainingRecommendation }}</div>
        </q-card-section>
      </q-card>

      <q-separator spaced />
      <SectionContainer :title="$t('symptoms')" link="/symptoms" :linkText="$t('add')" :emojis="symptomsEmojis"
        :loading="loadingSymptoms" />
      <q-separator spaced />
      <SectionContainer :title="$t('mood')" link="/mood" :linkText="$t('add')" :emojis="moodEmojis"
        :loading="loadingMood" />
      <q-separator spaced />
      <SectionContainer :title="$t('trs')" link="/trs" :linkText="$t('more-info')" :emojis="[]" :loading="false" />
    </q-page>
  </div>
</template>

<script>
import { QSpinner, QBtn, QSeparator, QPage, QTable, QTr, QTd, QCard, QCardSection } from 'quasar';
import SectionContainer from 'components/SectionContainer.vue';

export default {
  components: {
    SectionContainer,
    QSpinner,
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
      loadingCalendar: true,
      loadingTraining: true,
      loadingMood: true,
      loadingSymptoms: true,
      columns: [
        { name: 'mon', label: this.$t('weekdays_short[1]'), align: 'center' },
        { name: 'tue', label: this.$t('weekdays_short[2]'), align: 'center' },
        { name: 'wed', label: this.$t('weekdays_short[3]'), align: 'center' },
        { name: 'thu', label: this.$t('weekdays_short[4]'), align: 'center' },
        { name: 'fri', label: this.$t('weekdays_short[5]'), align: 'center' },
        { name: 'sat', label: this.$t('weekdays_short[6]'), align: 'center' },
        { name: 'sun', label: this.$t('weekdays_short[0]'), align: 'center' },
      ],
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
        week.push(...prevMonthDays.map(day => ({ date: day, colorClass: 'previous-month' })));
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
        week.push(...Array(nextMonthDays).fill({ date: '', colorClass: 'next-month' }));
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
  },
  methods: {
    async fetchData() {
      try {
        const response = await this.mockApiCall();
        this.dayColors = response.dayColors;
        this.trainingRecommendation = response.trainingRecommendation;
        this.loadingCalendar = false;
        this.loadingTraining = false;

        const emojisResponse = await this.fetchEmojis();
        this.moodEmojis = emojisResponse.mood;
        this.symptomsEmojis = emojisResponse.symptoms;
        this.loadingMood = false;
        this.loadingSymptoms = false;
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    },
    mockApiCall() {
      return new Promise(resolve => {
        setTimeout(() => {
          resolve({
            dayColors: {
              3: 'period',
              4: 'period',
              5: 'period',
              6: 'period',
              7: 'period',
              8: 'follicle',
              9: 'follicle',
              10: 'follicle',
              11: 'follicle',
              30: 'prediction',
              31: 'prediction',
            },
            trainingRecommendation: 'Recommended training: Cardio exercises',
          });
        }, 1000);
      });
    },
    fetchEmojis() {
      return new Promise(resolve => {
        setTimeout(() => {
          resolve({
            mood: [
              { emoji: '❓', label: 'Confused' },
              { emoji: '😶‍🌫️', label: 'Insecure' },
              { emoji: '🤩', label: 'Excited' },
              { emoji: '🫨', label: 'Nervous' },
            ],
            symptoms: [
              { emoji: '🍫', label: 'Cravings' },
              { emoji: '📉', label: 'Mood Swings' },
              { emoji: '💢', label: 'Cramps' },
              { emoji: '🥶', label: 'Cold' },
            ]
          });
        }, 1000);
      });
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
    dayColorClass(day) {
      if (this.selectedDay === day) {
        return 'currentDate';
      }
      return this.dayColors[day] || '';
    },
    selectDay(day) {
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
    },
    getDaysInPreviousMonth() {
      const date = new Date(this.date.year, this.date.month, 0);
      return [...Array(date.getDate()).keys()].map(i => i + 1);
    },
    log() {
      this.$router.push('/log');
    }
  },
  mounted() {
    this.fetchData();
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

.previous-month,
.next-month {
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
</style>
