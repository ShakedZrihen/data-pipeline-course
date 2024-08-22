import { styled } from "@mui/material";
import { useContext } from "react";
import ChartsContext from "../../state/context";
import { normalizeCounts } from "../../common/utils/stats";

const StyledStatsBox = styled("div")`
  width: 100%;
  height: 15rem;
  margin-top: 3rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
`;

const LineBox = styled("div")`
  width: 1.7rem;
  height: 1rem;
  margin-bottom: 0.5rem;
  background-color: ${({ color }) => color ?? "red"};
`;

const LineContainer = styled("div")`
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  height: 100%;
  margin: 0 0.3rem;
  align-items: center;
`;

const GraphContainer = styled("div")`
  display: flex;
  align-items: flex-end;
  justify-content: center;
`;

const Label = styled("p")`
  margin: 0;
`;

const GenderStats = () => {
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

export default GenderStats;
