export const ON_SELECT_YEAR = "ON_SELECT_YEAR";
export const ON_SELECT_CHART = "ON_SELECT_CHART";
export const ON_UPDATE_WORLD_MAP_DATA = "ON_UPDATE_WORLD_MAP_DATA";
export const ON_CHANGE_BY_FILTER = "ON_CHANGE_BY_FILTER";

export const onSelectYear = (year) => ({
  type: ON_SELECT_YEAR,
  payload: year
});

export const onSelectChart = (chart) => ({
  type: ON_SELECT_CHART,
  payload: chart
});

export const onUpdateWorldMapData = ({ topSongFeaturesByCountry, charts }) => ({
  type: ON_UPDATE_WORLD_MAP_DATA,
  payload: { topSongFeaturesByCountry, charts }
});

export const onChangeByFilter = (filter) => ({ type: ON_CHANGE_BY_FILTER, payload: filter });
