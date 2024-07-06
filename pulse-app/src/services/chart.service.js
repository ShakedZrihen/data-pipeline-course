import axios from "axios";
import { SERVER_BASE_URL } from "../common/consts/api";

export const getChartAvailableDates = async () => {
  const response = await axios.get(new URL("/charts/available-dates", SERVER_BASE_URL).toString());
  
  return response;
};
