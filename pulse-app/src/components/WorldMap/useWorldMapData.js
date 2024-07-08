import { useContext, useEffect, useState } from "react";
import ChartsContext from "../../state/context";
import { getChartByYear } from "../../services/chart.service";

const useWorldMapData = () => {
  const {
    state: { selectedYear }
  } = useContext(ChartsContext);

  const [worldMapData, setWorldMapData] = useState([]);

  const getTopSongFeaturesByCountry = (charts) => {
    const genreByCountry = Object.entries(charts).reduce((acc, [country, chart]) => {
      const genre = chart?.[0]?.songFeatures?.genre ?? "unknown";
      const artistType = chart?.[0]?.artistFeatures?.type ?? "unknown";
      const artistGender = chart?.[0]?.artistFeatures?.gender ?? "unknown";
      acc[country] = { genre, artistType: artistType === "Solo" ? artistGender : artistType, raw: chart[0] };

      return acc;
    }, {});

    return genreByCountry;
  };

  useEffect(() => {
    const fetchData = async () => {
      console.log('Fetching data...')
      const { data } = await getChartByYear(selectedYear);
      const { charts } = data ?? {};
      if (!charts) {
        setWorldMapData(data);
        return;
      }
      const topSongFeaturesByCountry = getTopSongFeaturesByCountry(charts);

      setWorldMapData({ topSongFeaturesByCountry, charts });
    };

    fetchData();
  }, [selectedYear]);

  return worldMapData;
};

export default useWorldMapData;
