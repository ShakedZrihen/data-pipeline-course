import { useContext } from "react";
import ChartsContext from "../../state/context";
import { normalizeCounts } from "../../common/utils/stats";
import { GraphContainer, Label, LineBox, LineContainer, StyledStatsBox } from "./StatsBox.style";

// TODO: change content to fit all genres
const SongGenreStats = () => {
  const {
    state: {
      worldMapData: { topSongFeaturesByCountry }
    }
  } = useContext(ChartsContext);

  if (!topSongFeaturesByCountry) {
    return null;
  }

  const byArtistCounter = Object.values(topSongFeaturesByCountry ?? {}).reduce((acc, { artistType }) => {
    acc[artistType] = (acc[artistType] ?? 0) + 1;
    return acc;
  }, {});

  const normelizedCounts = normalizeCounts(byArtistCounter);

  const bandBoxes = Array.from({ length: normelizedCounts.Band ?? 0 }, (_, i) => <LineBox key={i} color="#ffba41" />);
  const maleBoxes = Array.from({ length: normelizedCounts.Male ?? 0 }, (_, i) => <LineBox key={i} color="#00c4d0" />);
  const femaleBoxes = Array.from({ length: normelizedCounts.Female ?? 0 }, (_, i) => (
    <LineBox key={i} color="#fd8db5" />
  ));

  return (
    <StyledStatsBox>
      <GraphContainer>
        <LineContainer>{bandBoxes}</LineContainer>
        <LineContainer>{maleBoxes}</LineContainer>
        <LineContainer>{femaleBoxes}</LineContainer>
      </GraphContainer>
      <Label>Artist Gender</Label>
    </StyledStatsBox>
  );
};

export default SongGenreStats;
