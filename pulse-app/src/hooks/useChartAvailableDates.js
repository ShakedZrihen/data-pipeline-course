import { useQuery } from "@tanstack/react-query";
import { getChartAvailableDates } from "../services/chart.service";

const useChartAvailableDates = () => {
  const { isLoading, isError, data } = useQuery({ queryKey: ["chartDates"], queryFn: getChartAvailableDates });

  return { isLoading, isError, data: data?.data ?? {} };
};

export default useChartAvailableDates;
