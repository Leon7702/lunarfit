export function calculateScore(trsdata) {
  // Each score contributes 25/6 to the total score
  const weight = 25 / 6;
  const totalScore = (trsdata.trs_acwr + trsdata.mood + trsdata.recovery + trsdata.complaints) * weight;
  return Math.round(totalScore);
}
