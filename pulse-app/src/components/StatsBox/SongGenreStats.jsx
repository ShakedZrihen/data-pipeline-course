import { useContext } from "react";
import ChartsContext from "../../state/context";
import { normalizeCounts } from "../../common/utils/stats";
import { GraphContainer, Label, LineBox, LineContainer, StyledStatsBox } from "./StatsBox.style";
import { COLOR_PALETTES } from "../WorldMap/featureColors";
import { hashGenreToIndex } from "../../common/utils/colors";
import { Tooltip } from "@mui/material";

// TODO: change content to fit all genres
const SongGenreStats = () => {
  const {
    state: {
      worldMapData: { topSongFeaturesByCountry }
    }
  } = useContext(ChartsContext);
  console.log({ topSongFeaturesByCountry });
  if (!topSongFeaturesByCountry) {
    return null;
  }

  const byGenreCounter = Object.values(topSongFeaturesByCountry ?? {}).reduce((acc, { genre }) => {
    acc[genre] = (acc[genre] ?? 0) + 1;
    return acc;
  }, {});

  const normelizedCounts = normalizeCounts(byGenreCounter);

  const graphLines = Object.entries(normelizedCounts).map(([genre, count]) => {
    return (
      <Tooltip key={genre} title={genre}>
        <LineContainer>
          {Array.from({ length: count ?? 0 }, (_, i) => (
            <LineBox key={i} color={COLOR_PALETTES[hashGenreToIndex(genre)]} />
          ))}
        </LineContainer>
      </Tooltip>
    );
  });

  return (
    <StyledStatsBox>
      <GraphContainer>{graphLines}</GraphContainer>
      <Label>Song Genre</Label>
    </StyledStatsBox>
  );
};

export default SongGenreStats;
