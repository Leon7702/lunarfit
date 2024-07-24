<template>
  <div class="q-pa-none">
    <div class="row justify-center">
      <q-btn-toggle
        class="toggle-border"
        size="sm"
        v-model="slide"
        :options="[
          { label: '1', value: 'training' },
          { label: '2', value: 'mood' },
          { label: '3', value: 'strain' },
          { label: '4', value: 'free' },
          { label: '5', value: 'rest' },
        ]"
      />
    </div>
    <div class="q-gutter-md">
      <q-carousel
        v-model="slide"
        transition-prev="slide-right"
        transition-next="slide-left"
        swipeable
        animated
        control-color="black"
        padding
        :style="{ height: '80vh' }"
      >
        <q-carousel-slide name="training" class="column no-wrap flex-center">
          <q-scroll-area class="fit">
            <div class="column no-wrap flex-center">
              <div class="text-h6">{{ $t("training") }}</div>
              <TrsSunburst />
              <div class="text-p">
                <strong
                  >Training Readiness Score:
                  {{ trainingReadinessScore }}%</strong
                >
              </div>
              <p></p>
              <div v-if="currentDayData">
                <q-card flat bordered class="my-card">
                  <q-card-section>
                    {{ $t(`${trainingTextKey}.description`) }}
                    <ul>
                      <li>{{ $t(`${trainingTextKey}.recommendations[0]`) }}</li>
                      <li>{{ $t(`${trainingTextKey}.recommendations[1]`) }}</li>
                      <li>{{ $t(`${trainingTextKey}.recommendations[2]`) }}</li>
                      <li>{{ $t(`${trainingTextKey}.recommendations[3]`) }}</li>
                    </ul>
                  </q-card-section>
                </q-card>
              </div>
              <div v-else>
                <div class="q-mt-none text-center">
                  <AssessmentRequiredCard />
                </div>
              </div>
              <p></p>
              <q-card flat bordered class="my-card">
                <q-card-section>
                  <div v-if="phaseTextKey">{{ $t(phaseTextKey) }}</div>
                </q-card-section>
              </q-card>
            </div>
          </q-scroll-area>
        </q-carousel-slide>

        <q-carousel-slide name="mood" class="column no-wrap flex-center">
          <q-scroll-area class="fit">
            <div class="column no-wrap flex-center">
              <div class="text-h6">{{ $t("mood") }}</div>
              <div class="q-mt-none text-center">
                <div v-if="currentDayData">
                  <q-card flat bordered class="my-card">
                    <q-card-section>
                      <div class="info-text">
                        <strong>{{
                          $t(`moodInfo.${moodScore}.description`)
                        }}</strong>
                        <div>{{ $t(`moodInfo.${moodScore}.advice`) }}</div>
                      </div>
                    </q-card-section>
                  </q-card>
                </div>
                <div v-else>
                  <AssessmentRequiredCard />
                </div>
                <div class="q-pa-md">
                  <div class="scoreText">{{ $t("moodInfo.today") }}</div>
                  <div class="q-gutter-y-md column justify-center items-center">
                    <q-rating
                      v-model="moodScore"
                      size="2em"
                      :max="6"
                      color="grey"
                      :color-selected="ratingColors"
                      icon="rectangle"
                      readonly
                    />
                  </div>
                </div>
                <div class="q-px-sm q-pt-sm q-pb-none">
                  <!-- <div class="q-pb-sm">DateInput: {{ date }}</div> -->
                  <q-btn flat dense @click="openPicker" class="date-display">
                    {{ $t("selectDate") }} <q-icon name="arrow_drop_down" />
                    <q-popup-proxy ref="qDateProxy">
                      <q-date v-model="date" range />
                    </q-popup-proxy>
                  </q-btn>
                </div>
                <LineChart
                  :data="filteredData.moodData"
                  :labels="filteredData.dateLabels"
                  :label="$t('moodTrend')"
                  color="#93EDE8"
                  :yStepSize="1"
                  chartType="mood"
                />
                <div class="yText">{{ $t("yLegend.mood") }}</div>
              </div>
            </div>
          </q-scroll-area>
        </q-carousel-slide>

        <q-carousel-slide name="strain" class="column no-wrap flex-center">
          <q-scroll-area class="fit">
            <div class="column no-wrap flex-center">
              <div class="text-h6">{{ $t("strain") }}</div>
              <div class="q-mt-none text-center">
                <div v-if="currentDayData">
                  <q-card flat bordered class="my-card">
                    <q-card-section>
                      <div class="info-text">
                        <strong>{{ $t(`acwrInfo`) }} {{ acwr }}</strong>
                        <div>{{ $t(`strainInfo.${acwrScore}.description`) }}</div>
                        <p></p>
                        <div>
                          {{ $t(`strainInfo.${acwrScore}.recommendations[0]`) }}
                        </div>
                        <div>
                          {{ $t(`strainInfo.${acwrScore}.recommendations[1]`) }}
                        </div>
                        <div>
                          {{ $t(`strainInfo.${acwrScore}.recommendations[2]`) }}
                        </div>
                        <div>
                          {{ $t(`strainInfo.${acwrScore}.recommendations[3]`) }}
                        </div>
                      </div>
                    </q-card-section>
                  </q-card>
                </div>
                <div v-else>
                  <AssessmentRequiredCard />
                </div>
                <div class="q-px-sm q-pt-lg q-pb-none">
                  <q-btn flat dense @click="openPicker" class="date-display">
                    {{ $t("selectDate") }} <q-icon name="arrow_drop_down" />
                    <q-popup-proxy ref="qDateProxy">
                      <q-date v-model="date" range />
                    </q-popup-proxy>
                  </q-btn>
                </div>
                <LineChart
                  :data="filteredData.acwrData"
                  :labels="filteredData.dateLabels"
                  :label="$t('acwrTrend')"
                  color="#50C1BA"
                  :yStepSize="0.5"
                  chartType="acwr"
                />
                <div class="yText">{{ $t("yLegend.acwr") }}</div>
              </div>
            </div>
          </q-scroll-area>
        </q-carousel-slide>

        <q-carousel-slide name="free" class="column no-wrap flex-center">
          <q-scroll-area class="fit">
            <div class="column no-wrap flex-center">
              <div class="text-h6">{{ $t("free") }}</div>
              <div class="q-mt-none text-center">
                <div v-if="currentDayData">
                  <q-card flat bordered class="my-card">
                    <q-card-section>
                      <div class="info-text">
                        <div>{{ $t(`freeInfo.${freeScore}.description`) }}</div>
                        <p></p>
                        <div>
                          {{ $t(`freeInfo.${freeScore}.recommendations[0]`) }}
                        </div>
                        <div>
                          {{ $t(`freeInfo.${freeScore}.recommendations[1]`) }}
                        </div>
                        <div>
                          {{ $t(`freeInfo.${freeScore}.recommendations[2]`) }}
                        </div>
                        <div>
                          {{ $t(`freeInfo.${freeScore}.recommendations[3]`) }}
                        </div>
                        <div>
                          {{ $t(`freeInfo.${freeScore}.recommendations[4]`) }}
                        </div>
                      </div>
                    </q-card-section>
                  </q-card>
                </div>
                <div v-else>
                  <AssessmentRequiredCard />
                </div>
                <div class="q-pa-md">
                  <div class="scoreText">{{ $t("strainInfo.today") }}</div>
                  <div class="q-gutter-y-md column justify-center items-center">
                    <q-rating
                      v-model="freeScore"
                      size="2em"
                      :max="6"
                      color="grey"
                      :color-selected="ratingColors"
                      icon="rectangle"
                      readonly
                    />
                  </div>
                </div>
                <div class="q-px-sm q-pt-sm q-pb-none">
                  <q-btn flat dense @click="openPicker" class="date-display">
                    {{ $t("selectDate") }} <q-icon name="arrow_drop_down" />
                    <q-popup-proxy ref="qDateProxy">
                      <q-date v-model="date" range />
                    </q-popup-proxy>
                  </q-btn>
                </div>
                <LineChart
                  :data="filteredData.complaintsData"
                  :labels="filteredData.dateLabels"
                  :label="$t('complaintsTrend')"
                  color="#9CD3D0"
                  :yStepSize="1"
                  chartType="complaints"
                />
                <div class="yText">{{ $t("yLegend.complaints") }}</div>
              </div>
            </div>
          </q-scroll-area>
        </q-carousel-slide>

        <q-carousel-slide name="rest" class="column no-wrap flex-center">
          <q-scroll-area class="fit">
            <div class="column no-wrap flex-center">
              <div class="text-h6">{{ $t("rest") }}</div>
              <div class="q-mt-none text-center">
                <div v-if="currentDayData">
                  <q-card flat bordered class="my-card">
                    <q-card-section>
                      {{ $t(`restInfo.${restScore}`) }}
                    </q-card-section>
                  </q-card>
                </div>
                <div v-else>
                  <AssessmentRequiredCard />
                </div>
                <div class="q-pa-md">
                  <div class="scoreText">{{ $t("restInfo.today") }}</div>
                  <div class="q-gutter-y-md column justify-center items-center">
                    <q-rating
                      v-model="restScore"
                      size="2em"
                      :max="6"
                      color="grey"
                      :color-selected="ratingColors"
                      icon="rectangle"
                      readonly
                    />
                  </div>
                </div>
                <div class="q-px-sm q-pt-sm q-pb-none">
                  <q-btn flat dense @click="openPicker" class="date-display">
                    {{ $t("selectDate") }} <q-icon name="arrow_drop_down" />
                    <q-popup-proxy ref="qDateProxy">
                      <q-date v-model="date" range />
                    </q-popup-proxy>
                  </q-btn>
                </div>
                <LineChart
                  :data="filteredData.recoveryData"
                  :labels="filteredData.dateLabels"
                  :label="$t('recoveryTrend')"
                  color="#38A8A1"
                  :yStepSize="1"
                  chartType="recovery"
                />
                <div class="yText">{{ $t("yLegend.recovery") }}</div>
              </div>
            </div>
          </q-scroll-area>
        </q-carousel-slide>
      </q-carousel>
    </div>
  </div>
</template>

<script>
import { ref, computed } from "vue";
import axios from "axios";
import TrsSunburst from "components/TrsSunburst.vue";
import LineChart from "components/LineChart.vue";
import AssessmentRequiredCard from "components/AssessmentRequiredCard.vue";
import { calculateScore } from "src/utils/scoreCalculator";
import {
  calculateCycleAndPhases,
  calculateCurrentDay,
  getCurrentCycle,
} from "src/utils/cyclePhaseCalculator.js";

export default {
  setup() {
    const slide = ref("training");
    const moodScore = ref(0);
    const strainScore = ref(0);
    const freeScore = ref(0);
    const restScore = ref(0);
    const acwr = ref(1.2);
    const trainingReadinessScore = ref(0);

    const cycleLength = ref(null);
    const currentDay = ref(16);

    const phaseTextKey = ref("");
    const currentDayData = ref(null);

    const mensLengthPortion = ref(null);
    const follicularLengthPortion = ref(null);
    const ovulationLengthPortion = ref(null);
    const earlyLutealLengthPortion = ref(null);
    const lateLutealLengthPortion = ref(null);

    const trsScores = ref(null);

    const date2 = new Date();
    date2.setDate(date2.getDate() - 6);
    const date7DaysPrior = date2.toISOString().split("T")[0];
    const date = ref({
      from: date7DaysPrior.split("-").join("/"),
      to: new Date().toISOString().split("T")[0].split("-").join("/"),
    });

    const qDateProxyRef = ref(null);

    const openPicker = () => {
      if (qDateProxyRef.value) {
        qDateProxyRef.value.show();
      }
    };

    const roundToTwoDecimals = (num) => parseFloat(num.toFixed(2));

    const calculateLengthPortion = (calculatedLengths) => {
      mensLengthPortion.value =
        (calculatedLengths.phaseLengths[0].length / cycleLength.value) * 100;
      follicularLengthPortion.value =
        (calculatedLengths.phaseLengths[1].length / cycleLength.value) * 100;
      ovulationLengthPortion.value =
        (calculatedLengths.phaseLengths[2].length / cycleLength.value) * 100;
      earlyLutealLengthPortion.value =
        (calculatedLengths.phaseLengths[3].length / cycleLength.value) * 100;
      lateLutealLengthPortion.value =
        (calculatedLengths.phaseLengths[4].length / cycleLength.value) * 100;
    };

    const fetchData = async () => {
      try {
        const [cycleResponse, trsResponse] = await Promise.all([
          axios.get("http://localhost:3000/cycles/"),
          axios.get("http://localhost:3000/trs?user_id=1"),
        ]);

        // Handle cycle data
        const cycleData = cycleResponse.data;
        const today = new Date().toISOString().split("T")[0]; // Use the current date in production
        // const today = "2024-07-15"; // For testing, set a specific date instead of the current date
        // const today = "2024-05-05";  // for testing with a specific date - cycle 0
        // const today = "2024-06-09";  // for testing with a specific date - cycle 1
        // const today = "2024-11-11";  // for testing with a specific date - no cycle found

        const currentCycle = getCurrentCycle(cycleData, today);

        if (currentCycle) {
          const calculatedLengths = calculateCycleAndPhases(currentCycle);

          cycleLength.value = calculatedLengths.cycleLength;
          calculateLengthPortion(calculatedLengths);

          currentDay.value = calculateCurrentDay(currentCycle.start, today);

          const currentPhase = roundToTwoDecimals(
          (currentDay.value / cycleLength.value) * 100
        );
        if (currentPhase <= roundToTwoDecimals(mensLengthPortion.value)) {
          phaseTextKey.value = "menstruationPhaseText";
        } else if (
          currentPhase <=
          roundToTwoDecimals(
            mensLengthPortion.value + follicularLengthPortion.value
          )
        ) {
          phaseTextKey.value = "follicularPhaseText";
        } else if (
          currentPhase <=
          roundToTwoDecimals(
            mensLengthPortion.value +
              follicularLengthPortion.value +
              ovulationLengthPortion.value
          )
        ) {
          phaseTextKey.value = "ovulationPhaseText";
        } else if (
          currentPhase <=
          roundToTwoDecimals(
            mensLengthPortion.value +
              follicularLengthPortion.value +
              ovulationLengthPortion.value +
              earlyLutealLengthPortion.value
          )
        ) {
          phaseTextKey.value = "earlyLutealPhaseText";
        } else {
          phaseTextKey.value = "lateLutealPhaseText";
        }

        // Log the phaseTextKey to ensure it's being set correctly
        console.log("phaseTextKey:", phaseTextKey.value);
        } else {
          console.error('No cycle found for today\'s date');
        }

        // Handle TRS data
        const trsdata = trsResponse.data;
        const todayData = trsdata.find((entry) => entry.day === today);
        if (todayData) {
          currentDayData.value = todayData;
          moodScore.value = todayData.mood;
          strainScore.value = todayData.trs_acwr;
          freeScore.value = todayData.complaints;
          restScore.value = todayData.recovery;
          acwr.value = todayData.acwr;
          trainingReadinessScore.value = calculateScore(todayData); // calculate the trs
        } else {
          currentDayData.value = null;
        }

        // Handle trs score data
        trsScores.value = trsdata;
      } catch (error) {
        console.error("Failed to fetch data:", error);
      }
    };

    fetchData();

    const acwrScore = computed(() => {
      if (acwr.value < 0.8) return 1;
      if (acwr.value < 1.5) return 2;
      if (acwr.value < 1.8) return 3;
      return 4;
    });

    // Computed property to get the correct training text key based on trainingReadinessScore
    const trainingTextKey = computed(() => {
      if (trainingReadinessScore.value <= 25) return "scores.1";
      if (trainingReadinessScore.value <= 50) return "scores.2";
      if (trainingReadinessScore.value <= 75) return "scores.3";
      return "scores.4";
    });

    const filteredData = computed(() => {
      // Check if trsScores or date range is null/undefined
      if (trsScores.value === null || date.value?.to === undefined || date.value?.from === undefined) {
        return {
          moodData: [],
          acwrData: [],
          complaintsData: [],
          recoveryData: [],
          dateLabels: [],
        };
      }

      // Convert date range strings to Date objects
      let [toYear, toMonth, toDay] = date.value?.to.split("/");
      let [fromYear, fromMonth, fromDay] = date.value?.from.split("/");
      let toDate = new Date(`${toYear}-${toMonth}-${toDay}`);
      let fromDate = new Date(`${fromYear}-${fromMonth}-${fromDay}`);

      // Filter data within the date range
      let filtered = trsScores.value
        .filter((d) => new Date(d.day) >= fromDate)
        .filter((d) => new Date(d.day) <= toDate);

      // Create an array of all dates within the range
      let allDates = [];
      let currentDate = new Date(fromDate);
      while (currentDate <= toDate) {
        allDates.push(new Date(currentDate));
        currentDate.setDate(currentDate.getDate() + 1);
      }

      // Initialize arrays for data and labels
      let moodData = [];
      let acwrData = [];
      let complaintsData = [];
      let recoveryData = [];
      let dateLabels = [];

      // Fill data arrays with values or null if no data for a date
      allDates.forEach(date => {
        let entry = filtered.find(e => new Date(e.day).getTime() === date.getTime());
        dateLabels.push(date.toISOString().split('T')[0]);
        moodData.push(entry ? entry.mood : null);
        acwrData.push(entry ? entry.acwr : null);
        complaintsData.push(entry ? entry.complaints : null);
        recoveryData.push(entry ? entry.recovery : null);
      });

      // Return the data for the charts
      return {
        moodData,
        acwrData,
        complaintsData,
        recoveryData,
        dateLabels,
      };
    });

    return {
      slide,
      moodScore,
      strainScore,
      freeScore,
      restScore,
      acwr,
      acwrScore,
      trainingReadinessScore,
      trainingTextKey,
      phaseTextKey,
      trsScores,
      currentDayData,
      filteredData,
      ratingColors: [
        "teal-2",
        "teal-3",
        "teal-4",
        "teal-5",
        "teal-6",
        "teal-7",
      ],
      date,
      qDateProxyRef,
      openPicker,
    };
  },
  components: {
    TrsSunburst,
    LineChart,
    AssessmentRequiredCard
  },
};
</script>

<style scoped>
ul {
  padding-left: 15px;
  margin: 0;
}

.border-black {
  border: 1px solid black;
}

.my-card {
  width: 100%;
  max-width: 100vw;
}

.toggle-border {
  border: 1px solid #d9d9d9;
}

.info-text {
  text-align: left;
}

.date-display {
  font-weight: 400;
}

.q-icon {
  margin-left: 5px;
}

.text-h6 {
  font-weight: bold;
}

.yText {
  font-size: x-small;
  color: grey;
  padding-top: 5px;
}

.scoreText {
  padding-bottom: 5px;
}
</style>
