export function calculateScore(trsdata) {
  // Each score contributes 25/6 to the total score
  const weight = 25 / 6;
  const totalScore = (trsdata.strain + trsdata.mood + trsdata.rest + trsdata.free) * weight;
  return Math.round(totalScore);
}
