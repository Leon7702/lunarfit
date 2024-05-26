<template>
  <div>
    <div class="header">
      <q-btn class="leftButton" @click="prevMonth">
        <template v-slot:default>
          <img src="" alt="Left">
        </template>
      </q-btn>
      <div class="month-year">{{ currentMonth }} {{ currentYear }}</div>
      <q-btn class="rightButton" @click="nextMonth">
        <template v-slot:default>
          <img src="" alt="Right">
        </template>
      </q-btn>
    </div>
    <table>
      <tr>
        <th>S</th>
        <th>M</th>
        <th>T</th>
        <th>W</th>
        <th>T</th>
        <th>F</th>
        <th>S</th>
      </tr>
      <tr v-for="(week, weekIndex) in weeksInMonth" :key="weekIndex">
        <td v-for="(day, dayIndex) in week" :key="`${weekIndex}-${dayIndex}`">
          <div :class="['day-circle', dayColorClass(day)]">{{ day }}</div>
        </td>
      </tr>
    </table>

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

  </div>
</template>


  
<script>
export default {
  data() {
    let date = new Date();
    return {
      date: {
        year: date.getFullYear(),
        month: date.getMonth(),
      },
      dayColors: {
        1: 'period',
        2: 'follicle',
        3: 'prediction',
      },
    };
  },
  computed: {
    currentYear() {
      return this.date.year;
    },
    currentMonth() {
      return new Date(this.date.year, this.date.month, 1).toLocaleString('default', { month: 'long' });
    },
    daysInMonth() {
      let date = new Date(this.date.year, this.date.month + 1, 0);
      return [...Array(date.getDate()).keys()].map(i => i + 1);
    },
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

/* Add more color classes as needed */
</style>
