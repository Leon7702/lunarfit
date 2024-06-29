<template>
  <div class="container">
    <!-- Header with navigation buttons and current month/year display -->
    <div class="header">
      <!-- Button to navigate to the previous month -->
      <div class="navButton" @click="prevMonth">
        <img src="/src/assets/arrow-left.svg" alt="Left" class="navButtonImage">
      </div>

      <!-- Display current month and year -->
      <div class="month-year">{{ currentMonth }} {{ currentYear }}</div>

      <!-- Button to navigate to the next month -->
      <div class="navButton" @click="nextMonth">
        <img src="/src/assets/arrow-right.svg" alt="Right" class="navButtonImage">
      </div>
    </div>

    <!-- Calendar table with days of the week and dates -->
    <table>
      <!-- Header row with days of the week -->
      <tr>
        <th>{{ $t('weekdays_short[1]') }} </th>
        <th>{{ $t('weekdays_short[2]') }}</th>
        <th>{{ $t('weekdays_short[3]') }}</th>
        <th>{{ $t('weekdays_short[4]') }}</th>
        <th>{{ $t('weekdays_short[5]') }}</th>
        <th>{{ $t('weekdays_short[6]') }}</th>
        <th>{{ $t('weekdays_short[0]') }}</th>
      </tr>

      <!-- Rows for each week in the month -->
      <tr v-for="(week, weekIndex) in weeksInMonth" :key="weekIndex">
        <td v-for="(day, dayIndex) in week" :key="`${weekIndex}-${dayIndex}`">
          <div :class="['day-circle', day.colorClass]" @click="selectDay(day.date)">
            {{ day.date }}
          </div>
        </td>
      </tr>
    </table>

    <!-- Legend to explain color codes for different phases -->
    <div class="legend">
      <div class="legend-item">
        <div class="day-circle period"></div>
        <span class="legend-label">{{ $t('calendarLegend[0]') }}</span>
      </div>
      <div class="legend-item">
        <div class="day-circle prediction"></div>
        <span class="legend-label">{{ $t('calendarLegend[1]') }}</span>
      </div>
      <div class="legend-item">
        <div class="day-circle follicle"></div>
        <span class="legend-label">{{ $t('calendarLegend[2]') }}</span>
      </div>
    </div>

    <!-- Container for logging details of the selected day -->
    <div class="day-log-container">
      <div class="day-log-header">
        <div class="current-day">{{ currentDayFormatted }}</div>
        <q-btn class="log-button" no-caps rounded style="background: #50C1BA; color: white" label="+ Log"
          padding="xs lg" size="14px">
          <template v-slot:default></template>
        </q-btn>
      </div>
    </div>

    <hr class="separator">

    <!-- Display training recommendation -->
    <div class="training-recommendation-container">
      <div class="training-recommendation-header">
        {{ $t('training-recommendation.title') }}
        <router-link to="/r">{{ $t('more-info') }}</router-link>
      </div>
      <div class="training-recommendation-text">
        {{ $t('training-recommendation.description') }}
      </div>
      <div class="training-recommendation"></div>
    </div>

    <hr class="separator">

    <!-- Display Symptoms and Mood using the new reusable component -->
    <SectionContainer :title="$t('symptoms')" link="/symptoms" :linkText="$t('add')" />
    <hr class="separator">
    <SectionContainer :title="$t('mood')" link="/mood" :linkText="$t('add')" />
    <hr class="separator">
    <SectionContainer :title="$t('trs')" link="/" :linkText="$t('more-info')" />
  </div>
</template>

<script>
import SectionContainer from 'components/SectionContainer.vue';

export default {
  components: {
    SectionContainer,
  },
  data() {
    let date = new Date();
    return {
      date: {
        year: date.getFullYear(),
        month: date.getMonth(),
        day: date.getDate(),
      },
      dayColors: {
        1: 'period',
        2: 'follicle',
        3: 'prediction'
      },
      selectedDay: date.getDate(),
    };
  },
  computed: {
    currentYear() {
      return this.date.year;
    },
    currentMonth() {
      // Use the current i18n locale for formatting
      const locale = this.$i18n.locale;
      return new Date(this.date.year, this.date.month, 1).toLocaleString(locale, {
        month: 'long',
      });
    },
    daysInMonth() {
      let date = new Date(this.date.year, this.date.month + 1, 0);
      return [...Array(date.getDate()).keys()].map((i) => i + 1);
    },
    weeksInMonth() {
      let days = this.daysInMonth;
      let firstDay = (new Date(this.date.year, this.date.month, 1).getDay() + 6) % 7; // Adjust for Monday start
      let weeks = [];
      let week = [];

      if (firstDay > 0) {
        let prevMonthDays = this.getDaysInPreviousMonth().slice(-firstDay);
        week.push(
          ...prevMonthDays.map((day) => ({ date: day, colorClass: 'previous-month' }))
        );
      }

      days.forEach((day) => {
        if (week.length === 7) {
          weeks.push(week);
          week = [];
        }
        week.push({ date: day, colorClass: this.dayColorClass(day) });
      });

      if (week.length > 0 && week.length < 7) {
        let nextMonthDays = 7 - week.length;
        week.push(
          ...Array(nextMonthDays).fill({ date: '', colorClass: 'next-month' })
        );
      }
      if (week.length > 0) {
        weeks.push(week);
      }

      return weeks;
    },
    currentDayFormatted() {
      let date;
      if (this.selectedDay !== null) {
        date = new Date(this.date.year, this.date.month, this.selectedDay);
      } else {
        date = new Date(this.date.year, this.date.month, this.date.day);
      }
      return date.toLocaleDateString('de-DE', {
        weekday: 'long',
        day: '2-digit',
        month: 'long',
      });
    },
  },
  methods: {
    nextMonth() {
      if (this.date.month === 11) {
        this.date.year++;
        this.date.month = 0;
      } else {
        this.date.month++;
      }
    },
    prevMonth() {
      if (this.date.month === 0) {
        this.date.year--;
        this.date.month = 11;
      } else {
        this.date.month--;
      }
    },
    dayColorClass(day) {
      if (this.selectedDay === day) {
        return 'currentDate';
      }
      return this.dayColors[day] || '';
    },
    selectDay(day) {
      if (day !== '') {
        let selectedDate = new Date(this.date.year, this.date.month, day);
        this.selectedDay = selectedDate.getDate();
      } else {
        this.selectedDay = null;
      }
    },

    getDaysInPreviousMonth() {
      let date = new Date(this.date.year, this.date.month, 0);
      return [...Array(date.getDate()).keys()].map((i) => i + 1);
    },
  },
};
</script>

<style>
table {
  width: 100%;
  table-layout: fixed;
  margin: 0 auto;
  margin-top: 20px;
}

th,
td {
  text-align: center;
  padding: 0px;
  padding-bottom: 10px;
  margin: 0;
  box-sizing: border-box;
}

th {
  width: 350px/7px;
  color: #6C7072;
  ;
}

a {
  color: #50c1ba;
  font-weight: bold;
  font-size: 14px;
  text-decoration: none;
}

p {
  font-size: 14px;
  margin: 20px;
  padding-top: 10px;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  margin-top: 46px;
  width: 80%;
  margin: 0 auto;
}

.month-year {
  color: #000;
  text-align: center;
  font-size: 20px;
  font-style: normal;
  font-weight: 600;
  line-height: 31px;
}

.navButton {
  font-size: 8px;
  cursor: pointer;
}

.day-circle {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 30px;
  height: 30px;
  line-height: 30px;
  border-radius: 50%;
  text-align: center;
  margin: auto;
}

.period {
  background-color: #FFD8DF;
  color: #FF2D55;
}

.follicle {
  background-color: #E7E7FF;
  color: black;
}

.prediction {
  border: 2px dotted #FF2D55;
  color: #000;
}

.currentDate {
  border: 2px solid #FF2D55;
  color: #000;
}

.navButton {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 40px;
  height: 40px;
  cursor: pointer;
}

.navButtonImage {
  width: 20px;
  height: 20px;
}


.previous-month {
  color: #b0b0b0;
}

.next-month {
  color: #b0b0b0;
}

.legend {
  display: flex;
  justify-content: space-evenly;
  margin: 5px 0;
}

.legend-item {
  display: flex;
  align-items: center;
}

.legend-item .day-circle {
  width: 15px;
  height: 15px;
  line-height: 15px;
  border-radius: 50%;
}

.legend-label {
  margin-left: 5px;
  font-size: 12px;
  color: #72777A;
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
  color: #090A0A;
  font-size: 18px;
  font-style: normal;
  font-weight: 600;
  margin-top: 5px;
}

.log-button {
  font-size: 14px;
}

.separator {
  margin-top: 10px;
  border: 0;
  border-top: 1px solid #e0e0e0;
  width: 100%;
}

.training-recommendation-container {
  width: 100%;
  margin: 20px auto;
}

.training-recommendation-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: #000;
  font-size: 16px;
  font-style: normal;
  font-weight: 600;
  line-height: 21px;
}

.training-recommendation-text {
  font-size: 14px;
  font-style: normal;
  font-weight: 400;
  line-height: 18px;
  padding-top: 18px;
}

@media only screen and (min-width: 200px) {
  .container {
    max-width: 350px;
    margin: auto;
    margin-top: 20px;
  }
}
</style>
