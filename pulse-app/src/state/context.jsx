/* eslint-disable react/prop-types */
import { createContext, useMemo, useReducer } from "react";
import reducer from "./reducer";

const initialProps = {
  selectedYear: -1,
  selectedChart: null
};

const ChartsContext = createContext(initialProps);
export const ChartsContextProvider = ({ children, selectedYear }) => {
  const [state, dispatch] = useReducer(reducer, {
    ...initialProps,
    selectedYear: selectedYear ?? initialProps.selectedYear
  });

  const contextValue = useMemo(() => ({ state, dispatch }), [state, dispatch]);

  return <ChartsContext.Provider value={contextValue}>{children}</ChartsContext.Provider>;
};

export default ChartsContext;
