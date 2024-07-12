import { useContext, useRef } from "react";
import ChartsContext from "../../state/context";
import useChartAvailableDates from "../../hooks/useChartAvailableDates";
import { onSelectYear } from "../../state/actions";
import { handleYearChanged } from "./utils";

const useTimeline = () => {
  const {
    state: { selectedYear },
    dispatch
  } = useContext(ChartsContext);

  const { data } = useChartAvailableDates();

  const years = Object.keys(data)
    .map(Number)
    .sort((a, b) => b - a);
  const debounceTimeout = useRef(null);

  const handleWheel = (e) => {
    if (debounceTimeout.current) {
      clearTimeout(debounceTimeout.current);
    }
    debounceTimeout.current = setTimeout(() => {
      const payload = {
        delta: e.deltaY,
        selectedYear,
        onChange: (year) => dispatch(onSelectYear(year))
      };
      handleYearChanged(payload);
    }, 2);
  };

  return { years, handleWheel };
};

export default useTimeline;