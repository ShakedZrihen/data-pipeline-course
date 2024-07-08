import { styled } from "@mui/material";
import { ComposableMap, Geographies, Geography } from "react-simple-maps";
import useWorldMapData from "./useWorldMapData";
import { genreColors } from "./genreColors";
import Tooltip from "@mui/material/Tooltip";
import { Fragment } from "react";

const StyledComposableMap = styled(ComposableMap)`
  width: 100%;
  height: 80%;
`;

const WorldMap = () => {
  const { topSongFeaturesByCountry } = useWorldMapData();

  if (!topSongFeaturesByCountry) {
    return null;
  }

  return (
    <>
      <StyledComposableMap>
        <Geographies geography={"/worldFeatures.json"}>
          {({ geographies }) =>
            geographies.map((geo) => {
              const songData = topSongFeaturesByCountry[geo.id];
              const geoStyle = {
                fill: genreColors[songData?.genre] ?? "#D6D6DA",
                outline: "none"
              };
              const country = geo?.properties?.name ?? "N/A";

              return (
                <Fragment key={geo.rsmKey}>
                  <Tooltip title={songData?.genre ? `${country}-${songData?.genre}` : "No data"}>
                    <Geography
                      geography={geo}
                      style={{
                        default: geoStyle,
                        hover: geoStyle,
                        pressed: geoStyle
                      }}
                    />
                  </Tooltip>
                </Fragment>
              );
            })
          }
        </Geographies>
      </StyledComposableMap>
    </>
  );
};

export default WorldMap;
