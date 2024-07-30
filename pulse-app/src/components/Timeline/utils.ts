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
