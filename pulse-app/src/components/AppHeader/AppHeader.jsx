import { FormControl, FormControlLabel, Radio, RadioGroup, styled } from "@mui/material";
import { useContext } from "react";
import ChartsContext from "../../state/context";
import { onChangeByFilter } from "../../state/actions";

const StyledHeader = styled("header")`
  width: 100%;
  display: flex;
  flex-direction: column;
`;

const AppHeader = () => {
  const { dispatch } = useContext(ChartsContext);

  return (
    <StyledHeader>
      <h1 style={{ color: "white", marginBottom: 0 }}>Music Charts</h1>
      <FormControl>
        <RadioGroup row defaultValue="byGender" onChange={(e) => dispatch(onChangeByFilter(e.target.value))}>
          <FormControlLabel value="byGender" control={<Radio variant="plain" />} label="By Gender" />
          <FormControlLabel value="byGenre" control={<Radio variant="plain" />} label="By Genre" />
          {/* <FormControlLabel value="bySong" control={<Radio variant="plain" />} label="By Song" /> */}
        </RadioGroup>
      </FormControl>
    </StyledHeader>
  );
};

export default AppHeader;
