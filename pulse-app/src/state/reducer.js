import { ON_SELECT_CHART, ON_SELECT_YEAR } from "./actions";

const reducer = (state, action) => {
  switch (action.type) {
    case ON_SELECT_YEAR:
      return { ...state, selectedYear: action.payload };
    case ON_SELECT_CHART:
      return { ...state, selectedChart: action.payload };
    default:
      return state;
  }
};

export default reducer;