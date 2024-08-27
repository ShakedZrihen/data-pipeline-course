import { ALL_TIMES_YEAR, CURRENT_YEAR } from "./consts";

export const handleYearChanged = ({ delta, selectedYear, onChange }) => {
  if (delta > 0) {
    // down
    if (selectedYear < 0) {
      onChange(CURRENT_YEAR);
      return;
    }

    if (selectedYear - 1 < 2010) {
      return;
    }

    onChange(selectedYear - 1);
  } else if (delta < 0) {
    if (selectedYear < 0) {
      return;
    }
    // up
    if (selectedYear + 1 > CURRENT_YEAR) {
      onChange(ALL_TIMES_YEAR);
      return;
    }
    onChange(selectedYear + 1);
  }
};

export const getThursdayWeeks = (payload) => {
  const weeks = {};

  const data = payload?.availableDates ?? payload;
  // Iterate over each year
  Object.keys(data).forEach((year) => {
    // Iterate over each month in the year
    Object.keys(data[year]).forEach((month) => {
      // Iterate over each day in the month
      const days = data[year][month]?.map((day) => parseInt(day));

      for (let i = 0; i < days.length; i++) {
        const date = new Date(`${year}-${month.padStart(2, "0")}-${days[i].toString().padStart(2, "0")}`);

        // Check if the day is a Thursday
        if (date.getDay() === 4) {
          // 4 is Thursday
          const formattedDate = date.toISOString().split("T")[0];
          const displayMonth = date.toLocaleString("default", { month: "long" });
          const weekLabel = `week of ${displayMonth.toLowerCase()} ${date.getDate()}`;

          weeks[formattedDate] = weekLabel;
        }
      }
    });
  });

  return weeks;
};

export function getLatestDatesFromThursdays(thursdayWeeks, maxCount = 15) {
  const dates = Object.keys(thursdayWeeks).map((dateStr) => new Date(dateStr));

  // Sort dates in descending order
  dates.sort((a, b) => b - a);

  const result = [];

  for (let i = 0; i < Math.min(maxCount, dates.length); i++) {
    result.push(dates[i]);
  }

  // Convert dates to the desired format with year as a key
  const finalResult = {};
  result.forEach((date) => {
    const year = date.getFullYear();
    const dateStr = date.toISOString().split("T")[0];
    if (!finalResult[year]) {
      finalResult[year] = [];
    }
    finalResult[year].push({
      date: dateStr,
      label: thursdayWeeks[dateStr]
    });
  });

  return finalResult;
}
