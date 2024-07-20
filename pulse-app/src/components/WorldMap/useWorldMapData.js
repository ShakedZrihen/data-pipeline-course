import { useContext, useEffect, useRef, useState } from "react";
import ChartsContext from "../../state/context";
import { getChartByYear } from "../../services/chart.service";

const useWorldMapData = () => {
  const {
    state: { selectedYear }
  } = useContext(ChartsContext);

  const [worldMapData, setWorldMapData] = useState(null);
  const debounceTimeoutRef = useRef(null);

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
      console.log("fetching new data for year", selectedYear);
      const { data } = await getChartByYear(selectedYear);
      const { charts } = data ?? {};

      if (!charts) {
        setWorldMapData(data);
        return;
      }
      const topSongFeaturesByCountry = getTopSongFeaturesByCountry(charts);

      setWorldMapData({ topSongFeaturesByCountry, charts });
    };

    if (worldMapData === null) {
      fetchData();
    } else {
      debounceTimeoutRef.current = setTimeout(() => {
        fetchData();
      }, 500);
    }

    return () => {
      if (debounceTimeoutRef.current) {
        clearTimeout(debounceTimeoutRef.current);
      }
    };
  }, [selectedYear]);

  return worldMapData == null ? [] : worldMapData;
};

export default useWorldMapData;
