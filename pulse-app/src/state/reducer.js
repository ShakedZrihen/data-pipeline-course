import { ON_CHANGE_BY_FILTER, ON_SELECT_CHART, ON_SELECT_DATE, ON_SELECT_YEAR, ON_UPDATE_WORLD_MAP_DATA } from "./actions";

const reducer = (state, action) => {
  switch (action.type) {
    case ON_SELECT_YEAR:
      return { ...state, selectedYear: action.payload };
    case ON_SELECT_CHART:
      return { ...state, selectedChart: action.payload };
    case ON_UPDATE_WORLD_MAP_DATA:
      return { ...state, worldMapData: action.payload };
    case ON_CHANGE_BY_FILTER:
      return { ...state, byFilter: action.payload };
    case ON_SELECT_DATE:
      return { ...state, selectedDate: action.payload };
    default:
      return state;
  }
};

export default reducer;
