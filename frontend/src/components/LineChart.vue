<template>
  <div style="height: 30vh">
    <TrsLine :data="chartData" :options="chartOptions" />
  </div>
</template>

<script>
import { Line as TrsLine } from 'vue-chartjs';
import { Chart, registerables } from 'chart.js';
Chart.register(...registerables);

export default {
  name: 'LineChart',
  components: {
    TrsLine,
  },
  props: {
    data: {
      type: Array,
      required: true,
    },
    label: {
      type: String,
      required: true,
    },
    color: {
      type: String,
      required: true,
    },
    labels: {
      type: Array,
      required: true,
    },
  },
  computed: {
    chartData() {
      return {
        labels: this.labels,
        datasets: [
          {
            label: this.label,
            backgroundColor: `${this.color}33`, // Adding some transparency
            borderColor: this.color,
            data: this.data,
            fill: true,
          },
        ],
      };
    },
    chartOptions() {
      return {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          y: {
            beginAtZero: true,
            max: 6,
            ticks: {
              stepSize: 1, // Definiert die Schrittgröße zwischen den Werten auf der Y-Achse
            },
          },
          x: {
            max: 7,
          }
        },
      };
    },
  },
};
</script>

<style scoped></style>
