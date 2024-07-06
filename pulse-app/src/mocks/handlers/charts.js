import { http, HttpResponse } from "msw";
import { SERVER_BASE_URL } from "../../common/consts/api";

function mockUrl(url) {
  return new URL(url, SERVER_BASE_URL).toString();
}

// Function to generate days for a given month and year
const generateDays = (year, month) => {
  const daysInMonth = new Date(year, month, 0).getDate(); // Get days in the month
  return Array.from({ length: daysInMonth }, (_, i) => String(i + 1).padStart(2, "0")); // Create array of days
};

const generateAvailableDatesData = () => {
  const yearsData = {};
  for (let year = 2010; year <= 2024; year++) {
    yearsData[year] = {
      "01": generateDays(year, 1),
      "02": generateDays(year, 2),
      "03": generateDays(year, 3),
      "04": generateDays(year, 4),
      "05": generateDays(year, 5),
      "06": generateDays(year, 6),
      "07": generateDays(year, 7),
      "08": generateDays(year, 8),
      "09": generateDays(year, 9),
      10: generateDays(year, 10),
      11: generateDays(year, 11),
      12: generateDays(year, 12)
    };
  }

  return yearsData;
};

export const handlers = [
  http.get(mockUrl("/charts/available-dates"), () => {
    return HttpResponse.json(generateAvailableDatesData());
  })
];
