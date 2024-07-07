// Function to calculate the number of days between two dates, inclusive of start and end dates
export function calculateDaysBetween(start, end) {
  const startDate = new Date(start);
  const endDate = new Date(end);
  const differenceInMilliseconds = endDate - startDate;
  const millisecondsInOneDay = 24 * 60 * 60 * 1000;
  return Math.floor(differenceInMilliseconds / millisecondsInOneDay) + 1;
}

// Function to calculate the current day in the cycle
export function calculateCurrentDay(cycleStartDate, currentDate) {
  const startDate = new Date(cycleStartDate);
  const current = new Date(currentDate);
  const differenceInMilliseconds = current - startDate;
  const millisecondsInOneDay = 24 * 60 * 60 * 1000;
  return Math.floor(differenceInMilliseconds / millisecondsInOneDay) + 1;
}

// Function to calculate the cycle length and the length of each phase
// calculates the mensLength, follicularLength, ovulationLength, earlyLutealLength, lateLutealLength
export function calculateCycleAndPhases(cycle) {
  const cycleLength = calculateDaysBetween(cycle.start, cycle.end);

  const phaseLengths = cycle.phases.map((phase) => {
    return {
      phase_number: phase.phase_number,
      length: calculateDaysBetween(phase.start, phase.end)
    };
  });

  return {
    cycleLength,
    phaseLengths
  };
}
