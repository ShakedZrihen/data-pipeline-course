import { styled } from "@mui/material";
import { useState } from "react";
import { ComposableMap, Geographies, Geography } from "react-simple-maps";


const StyledComposableMap = styled(ComposableMap)`
width: 100%;
height: 80%;
`

const WorldMap = () => {
  const [countryColors, setCountryColors] = useState({});

  const handleCountryClick = (geo) => {
    const countryId = geo.properties.ISO_A3;
    const newColor = prompt("Enter a color for this country (e.g., red, #ff0000):");
    if (newColor) {
      setCountryColors({
        ...countryColors,
        [countryId]: newColor
      });
    }
  };

  return (
    <StyledComposableMap>
      <Geographies geography={"/worldFeatures.json"}>
        {({ geographies }) =>
          geographies.map((geo) => (
            <Geography
              key={geo.rsmKey}
              geography={geo}
              onClick={() => handleCountryClick(geo)}
              style={{
                default: {
                  fill: countryColors[geo.properties.ISO_A3] || "#D6D6DA",
                  outline: "none"
                },
                hover: {
                  fill: "#F53",
                  outline: "none"
                },
                pressed: {
                  fill: "#E42",
                  outline: "none"
                }
              }}
            />
          ))
        }
      </Geographies>
    </StyledComposableMap>
  );
};

export default WorldMap;
