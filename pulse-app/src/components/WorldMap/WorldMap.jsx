import { styled } from "@mui/material";
import { ComposableMap, Geographies, Geography } from "react-simple-maps";
import { artistTypeColors, genreColors } from "./featureColors";
import Tooltip from "@mui/material/Tooltip";
import { Fragment, useContext } from "react";
import CountryModal from "../CountryModal/CountryModal";
import useModalProps from "../CountryModal/useModalProps";
import ChartsContext from "../../state/context";
import { FILTERS } from "../../common/consts/filters";

const StyledComposableMap = styled(ComposableMap)`
  width: 100%;
  height: 80%;
`;

const WorldMap = () => {
  const {
    state: { worldMapData, byFilter }
  } = useContext(ChartsContext);
  const { topSongFeaturesByCountry, charts } = worldMapData;

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
              const byArtistTypeColor = artistTypeColors[songData?.artistType] ?? artistTypeColors.unknown;
              const byGenreColor = genreColors[songData?.genre] ?? "#D6D6DA";

              const colorByFilter = {
                [FILTERS.GENDER]: byArtistTypeColor,
                [FILTERS.GENRE]: byGenreColor
              };

              if (songData) {
                console.log({ songData });
              }

              const tooltipByFilter = {
                [FILTERS.GENDER]: songData?.artistType,
                [FILTERS.GENRE]: songData?.genre
              };

              const color = colorByFilter[byFilter];
              const tooltipDescription = tooltipByFilter[byFilter] ?? 'no data';

              const chart = charts[geo.id];

              const geoStyle = {
                fill: chart ? color : "grey",
                outline: "none"
              };
              const country = geo?.properties?.name ?? "N/A";

              return (
                <Fragment key={geo.rsmKey}>
                  <Tooltip title={`${country}-${tooltipDescription}`}>
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
