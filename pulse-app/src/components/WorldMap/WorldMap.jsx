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
  const { topSongFeaturesByCountry, charts } = useWorldMapData();
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
              const chart = charts[geo.id];

              const geoStyle = {
                fill: chart ? byArtistTypeColor : "grey",
                outline: "none"
              };
              const country = geo?.properties?.name ?? "N/A";

              return (
                <Fragment key={geo.rsmKey}>
                  <Tooltip title={songData?.genre ? `${country}-${songData?.genre}` : "No data"}>
                    <Geography
                      onClick={() => modalProps.openModal({ country, chart })}
                      geography={geo}
                      style={{
                        default: geoStyle,
                        hover: { ...geoStyle, ...(chart && { cursor: "pointer" }) },
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
