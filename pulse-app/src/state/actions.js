export const ON_SELECT_YEAR = "ON_SELECT_YEAR";
export const ON_SELECT_CHART = "ON_SELECT_CHART";
export const ON_UPDATE_WORLD_MAP_DATA = "ON_UPDATE_WORLD_MAP_DATA";

export const onSelectYear = (year) => ({
  type: ON_SELECT_YEAR,
  payload: year
});

export const onSelectChart = (chart) => ({
  type: ON_SELECT_CHART,
  payload: chart
});
