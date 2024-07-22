<template>
  <div style="height: 30vh">
    <TrsLine :data="chartData" :options="chartOptions" />
  </div>
</template>

<script>
import { Line as TrsLine } from "vue-chartjs";
import { Chart, registerables } from "chart.js";
import 'chartjs-adapter-date-fns';
Chart.register(...registerables);

function roundUpToNextHalf(num) {
  return Math.ceil(num * 2) / 2 + 0.5;
}

export default {
  name: "LineChart",
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
    yStepSize: {
      type: Number,
      default: 1,
    },
    chartType: {
      type: String,
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
            spanGaps: true, // This option will interpolate over gaps
          },
        ],
      };
    },
    chartOptions() {
      const maxValues = {
        mood: 6,
        complaints: 6,
        recovery: 6,
      };
      const maxACWR = roundUpToNextHalf(Math.max(...this.data));

      return {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          x: {
            type: 'time',
            time: {
              unit: 'day',
              tooltipFormat: 'yyyy-MM-dd',
            },
          },
          y: {
            beginAtZero: true,
            max: this.chartType === 'acwr' ? maxACWR : maxValues[this.chartType],
            ticks: {
              stepSize: this.yStepSize,
            },
          },
        },
        plugins: {
          legend: {
            onClick: (e, legendItem, legend) => {
              // This is a no-op function, preventing any action from occurring
              // when a legend item is clicked.
            }
          }
        },
      };
    },
  },
};
</script>

<style scoped></style>
