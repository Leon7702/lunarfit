<template>
  <q-card flat bordered class="my-card">
    <q-card-section>
      <div class="pText">{{ $t("assessmentRequired") }}</div>
      <q-btn
        no-caps
        rounded
        style="background: #50C1BA; color: white"
        :label="$t('toAssessment')"
        padding="xs md"
        size="12px"
        to="log-training-strain"
      />
    </q-card-section>
  </q-card>
</template>

<script>
export default {
  name: "AssessmentRequiredCard",
};
</script>

<style scoped>
.my-card {
  width: 100%;
  max-width: 100vw;
}

.pText {
  padding-bottom: 8px;
}
</style>
