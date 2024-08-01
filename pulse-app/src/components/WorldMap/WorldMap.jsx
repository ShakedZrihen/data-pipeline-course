import { styled } from "@mui/material";
import { ComposableMap, Geographies, Geography } from "react-simple-maps";
import useWorldMapData from "./useWorldMapData";
import { artistTypeColors } from "./featureColors";
import Tooltip from "@mui/material/Tooltip";
import { Fragment } from "react";
import CountryModal from "../CountryModal/CountryModal";
import useModalProps from "../CountryModal/useModalProps";

const StyledComposableMap = styled(ComposableMap)`
  width: 100%;
  height: 80%;
`;

const WorldMap = () => {
  const { topSongFeaturesByCountry } = useWorldMapData();
  const modalProps = useModalProps();

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
              // const byGenreColor = genreColors[songData?.genre] ?? "#D6D6DA";
              const byArtistTypeColor = artistTypeColors[songData?.artistType] ?? artistTypeColors.unknown;
              const geoStyle = {
                fill: byArtistTypeColor,
                outline: "none"
              };
              const country = geo?.properties?.name ?? "N/A";

              return (
                <Fragment key={geo.rsmKey}>
                  <Tooltip title={songData?.genre ? `${country}-${songData?.genre}` : "No data"}>
                    <Geography
                      onClick={modalProps.openModal}
                      geography={geo}
                      style={{
                        default: geoStyle,
                        hover: { ...geoStyle, cursor: "pointer" },
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
      <CountryModal {...modalProps} />
    </>
  );
};

export default WorldMap;
