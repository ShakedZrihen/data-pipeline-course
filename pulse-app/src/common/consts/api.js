const API_PATH = {
  CHARTS: "/charts",
  AVAILABLE_CHART_DATES: "/charts/available-dates"
};

export const MOCK_URL = "http://localhost:5000";
export const REAL_URL = "";
export const SERVER_BASE_URL = import.meta.env.VITE_RUN_IN_MOCK ? MOCK_URL : REAL_URL;

export default API_PATH;
