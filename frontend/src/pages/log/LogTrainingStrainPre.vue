<template>
    <div class="welcome-container">
        <div class="header">
            <q-btn flat dense round icon="arrow_back" @click="goBack" />
            <div class="title">Trainingsbelastung</div>
        </div>
        <div class="linie"></div>
        <div class="form-group">
            <p>Hast du heute oder gestern trainiert?</p>
            <RadioToggle v-model="trainingStatus" />
        </div>
        <div class="form-group" v-if="trainingStatus === 'ja'">
            <p>Welche Sportart/Aktivität hast du durchgeführt?</p>
            <DropDownSingleSelect :options="trainingOptions" v-model="selectedActivity"/>
        </div>
        <div class="form-group spacer" v-if="trainingStatus === 'ja'"></div> <!-- Spacer div hinzugefügt -->
        <div class="form-group" v-if="trainingStatus === 'ja'">
            <p>Wie viele Minuten hast du trainiert?</p>
            <DropDownSingleSelect :options="trainingDurationOptions" v-model="selectedDuration"/>
        </div>
        <div class="button-container">
            <StandardButton label="Weiter" @click="navigateToNextStep" />
        </div>
    </div>
</template>

<script>
import StandardButton from 'components/StandardButton.vue';
import RadioToggle from 'components/RadioToggle.vue';
import DropDownSingleSelect from 'components/DropDownSingleSelect.vue';

export default {
    components: {
        StandardButton,
        RadioToggle,
        DropDownSingleSelect
    },
    data() {
        return {
            trainingStatus: null,
            trainingOptions: ['Krafttraining', 'Ausdauer', 'x', 'y', 'z'],
            trainingDurationOptions: ['60 Minuten oder weniger', '60 bis 120 Minuten', '120 Minuten oder mehr'],
            selectedActivity: null,
            selectedDuration: null
        };
    },
    methods: {
        goBack() {
            window.history.back();
        },
        navigateToNextStep() {
            if (this.trainingStatus === 'ja') {
                this.$router.push({ name: 'LogTrainingStrain' });
            } else {
                this.$router.push({ name: 'LogTrainingComplaints' });
            }
        }
    }
};
</script>

<style scoped>
.welcome-container {
    display: flex;
    flex-direction: column;
    align-items: center; /* Ausrichtung links */
    width: 90%;
    height: 100vh;
    overflow: auto;
    margin: auto;
}

.linie {
    height: 1px;
    background-color: rgba(0, 0, 0, 0.1);
    width: 120%;
    margin-top: 10px;
    margin-bottom: 30px;
}

.header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    padding: 10px 0;
    margin-top: 60px;
}

.title {
    font: 600 20px 'Inter', sans-serif;
    color: #000;
    text-align: center;
    flex-grow: 1;
    padding-right: 30px;
}

.form-group {
    width: 100%;
}

.form-group p {
    text-align: left;
    width: 100%;
    font-size: 16px;
    font-weight: 500;
}

.form-group.spacer {
    margin-bottom: 20px; /* Abstandsgröße anpassen nach Bedarf */
}

.button-container {
    position: fixed;
    bottom: 40px; 
    width: 100%;
    display: flex;
    justify-content: center;
    left: 0;
}
</style>
