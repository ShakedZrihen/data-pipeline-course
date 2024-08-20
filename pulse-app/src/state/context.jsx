/* eslint-disable react/prop-types */
import { createContext, useEffect, useMemo, useReducer, useRef } from "react";
import reducer from "./reducer";
import { getChartByYear } from "../services/chart.service";
import { onUpdateWorldMapData } from "./actions";
import { getTopSongFeaturesByCountry } from "../common/utils/charts";
import { FILTERS } from "../common/consts/filters";

const initialProps = {
  selectedYear: -1,
  selectedChart: null,
  byFilter: FILTERS.GENDER
};

const ChartsContext = createContext(initialProps);

export const ChartsContextProvider = ({ children, selectedYear }) => {
  const debounceTimeoutRef = useRef(null);

  const [state, dispatch] = useReducer(reducer, {
    ...initialProps,
    selectedYear: selectedYear ?? initialProps.selectedYear,
    worldMapData: {}
  });

  useEffect(() => {
    const fetchData = async () => {
      console.log("fetching new data for year", state.selectedYear);
      const { data } = await getChartByYear(state.selectedYear);
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
  }, [state.selectedYear]);

  const contextValue = useMemo(() => ({ state, dispatch }), [state, dispatch]);

  return <ChartsContext.Provider value={contextValue}>{children}</ChartsContext.Provider>;
};

export default ChartsContext;
