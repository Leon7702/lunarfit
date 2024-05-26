<template>
  <div>
    <!-- Header with navigation buttons and current month/year display -->
    <div class="header">
      <!-- Button to navigate to the previous month -->
      <q-btn class="leftButton" @click="prevMonth">
        <template v-slot:default>
          <img src="" alt="Left">
        </template>
      </q-btn>

      <!-- Display current month and year -->
      <div class="month-year">{{ currentMonth }} {{ currentYear }}</div>

      <!-- Button to navigate to the next month -->
      <q-btn class="rightButton" @click="nextMonth">
        <template v-slot:default>
          <img src="" alt="Right">
        </template>
      </q-btn>
    </div>

    <!-- Calendar table with days of the week and dates -->
    <table>
      <!-- Header row with days of the week -->
      <tr>
        <th>S</th>
        <th>M</th>
        <th>T</th>
        <th>W</th>
        <th>T</th>
        <th>F</th>
        <th>S</th>
      </tr>

      <!-- Rows for each week in the month -->
      <tr v-for="(week, weekIndex) in weeksInMonth" :key="weekIndex">
        <td v-for="(day, dayIndex) in week" :key="`${weekIndex}-${dayIndex}`">
          <div :class="['day-circle', dayColorClass(day)]">{{ day }}</div>
        </td>
      </tr>
    </table>

    <!-- Legend to explain color codes for different phases -->
    <div class="legend">
      <div class="legend-item">
        <div class="day-circle period"></div>
        <span class="legend-label">Periode</span>
      </div>
      <div class="legend-item">
        <div class="day-circle prediction"></div>
        <span class="legend-label">Vorhergesagte Periode</span>
      </div>
      <div class="legend-item">
        <div class="day-circle follicle"></div>
        <span class="legend-label">Follikelphase</span>
      </div>
    </div>

    <!-- Container for logging details of the selected day -->
    <div class="day-log-container">
      <div class="day-log-header">
        <div class="current-day">{{ currentDayFormatted }}</div>
        <q-btn class="log-button" no-caps rounded style="background: #50C1BA; color: white" label="+ Log" padding="xs lg" size="14px">
          <template v-slot:default></template>
        </q-btn>
      </div>
    </div>
    
    <!-- Horizontal separator line -->
    <hr class="separator">
  </div>
</template>

<script>
export default {
  data() {
    let date = new Date();
    return {
      // Store the current date
      date: {
        year: date.getFullYear(),
        month: date.getMonth(),
        day: date.getDate()
      },
      // Define color classes for specific days
      dayColors: {
        1: 'period',
        2: 'follicle',
        3: 'prediction',
      },
    };
  },
  computed: {
    // Compute the current year
    currentYear() {
      return this.date.year;
    },
    // Compute the current month as a string
    currentMonth() {
      return new Date(this.date.year, this.date.month, 1).toLocaleString('default', { month: 'long' });
    },
    // Compute the number of days in the current month
    daysInMonth() {
      let date = new Date(this.date.year, this.date.month + 1, 0);
      return [...Array(date.getDate()).keys()].map(i => i + 1);
    },
    // Compute the weeks in the current month for the calendar view
    weeksInMonth() {
      let days = this.daysInMonth;
      let firstDay = new Date(this.date.year, this.date.month, 1).getDay();
      let weeks = [];
      let week = Array(firstDay).fill('');
      days.forEach((day, index) => {
        week.push(day);
        if (week.length == 7 || index == days.length - 1) {
          weeks.push(week);
          week = [];
        }
      });
      return weeks;
    },
    // Format the current day for display
    currentDayFormatted() {
      let date = new Date(this.date.year, this.date.month, this.date.day);
      return date.toLocaleDateString('de-DE', { weekday: 'long', day: '2-digit', month: 'long' });
    }
  },
  methods: {
    // Navigate to the next month
    nextMonth() {
      if (this.date.month === 11) {
        this.date.year++;
        this.date.month = 0;
      } else {
        this.date.month++;
      }
    },
    // Navigate to the previous month
    prevMonth() {
      if (this.date.month === 0) {
        this.date.year--;
        this.date.month = 11;
      } else {
        this.date.month--;
      }
    },
    // Get the color class for a given day
    dayColorClass(day) {
      return this.dayColors[day] || '';
    },
  },
};
</script>

<style>
/* Ensure consistent styling for both table headers and data cells */
table {
  width: 80%;
  table-layout: fixed;
  margin: 0 auto;
  margin-top: 20px;
  border-collapse: collapse; /* Remove gaps between cells */
}

th, td {
  width: 14.2857%; /* 100% / 7 days */
  text-align: center;
  padding-bottom: 10px;
  box-sizing: border-box; /* Ensure padding and border are included in the width */
}

th {
  color: #6C7072;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  padding-top: 46px;
}

.month-year {
  color: #000;
  text-align: center;
  font-size: 20px;
  font-style: normal;
  font-weight: 600;
  line-height: 31px; /* 155% */
}

.leftButton, .rightButton {
  font-size: 8px;
}

.day-circle {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 30px; /* Ensure this matches height */
  height: 30px; /* Ensure this matches width */
  line-height: 30px; /* Ensure this matches height */
  border-radius: 50%;
  text-align: center;
  margin: auto; /* Center the circle in the table cell */
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
  border: 2px dotted #FF2D55; /* You can change the color as needed */
  color: #000; /* Set the text color */
}

.legend {
  display: flex;
  justify-content: space-evenly; /* Evenly space legend items */
  margin: 5px 0;
}

.legend-item {
  display: flex;
  align-items: center;
}

.legend-item .day-circle {
  width: 15px; /* Smaller width for legend items */
  height: 15px; /* Smaller height for legend items */
  line-height: 15px; /* Smaller line-height for legend items */
  border-radius: 50%; /* Ensure circle shape */
}

.legend-label {
  margin-left: 5px;
  font-size: 12px; /* Smaller font size for legend labels */
  color: #72777A; /* Set text color */
}

.day-log-container {
  width: 80%;
  margin: 20px auto; /* Center container with top margin */
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
  border-top: 1px solid #e0e0e0; /* Light grey color for the line */
  width: 100%; /* Ensure the separator stretches the full width */
}

/* Add more color classes as needed */
</style>
