/* eslint-disable react/prop-types */
import { createContext, useEffect, useMemo, useReducer, useRef } from "react";
import reducer from "./reducer";
import { getChartByDate } from "../services/chart.service";
import { onUpdateWorldMapData } from "./actions";
import { getTopSongFeaturesByCountry } from "../common/utils/charts";
import { FILTERS } from "../common/consts/filters";

const initialProps = {
  selectedYear: -1,
  selectedDate: -1,
  selectedChart: null,
  byFilter: FILTERS.GENDER
};

const ChartsContext = createContext(initialProps);

export const ChartsContextProvider = ({ children, selectedYear, selectedDate }) => {
  const debounceTimeoutRef = useRef(null);

  const [state, dispatch] = useReducer(reducer, {
    ...initialProps,
    selectedYear: selectedYear ?? initialProps.selectedYear,
    selectedDate: selectedDate ?? initialProps.selectedDate,
    worldMapData: {}
  });

  useEffect(() => {
    const fetchData = async () => {
      console.log("fetching new data for date", state.selectedDate);
      const { data } = await getChartByDate(state.selectedDate);
      const { charts } = data ?? {};

      if (!charts) {
        return;
      }
      const topSongFeaturesByCountry = getTopSongFeaturesByCountry(charts);

      dispatch(onUpdateWorldMapData({ topSongFeaturesByCountry, charts }));
    };

    if (!Object.keys(state.worldMapData)) {
      fetchData();
    } else {
      debounceTimeoutRef.current = setTimeout(() => {
        fetchData();
      }, 500);
    }
  }, [state.selectedDate]);

  const contextValue = useMemo(() => ({ state, dispatch }), [state, dispatch]);

  return <ChartsContext.Provider value={contextValue}>{children}</ChartsContext.Provider>;
};

export default ChartsContext;
