import axios from "axios";
import { SERVER_BASE_URL } from "../common/consts/api";

export const getChartAvailableDates = async () => {
  const response = await axios.get(new URL("/charts/available-dates", SERVER_BASE_URL).toString());

  return response;
};

export const getChartByYear = async (year) => {
  const response = await axios.get(new URL(`/charts?year=${year}`, SERVER_BASE_URL).toString());

  return response;
};
