import { FormControl, FormControlLabel, Radio, RadioGroup, styled } from "@mui/material";

const StyledHeader = styled("header")`
  width: 100%;
  display: flex;
  flex-direction: column;
`;

const AppHeader = () => {
  return (
    <StyledHeader>
      <h1 style={{ color: "white", marginBottom: 0 }}>Music Charts</h1>
      <FormControl>
        <RadioGroup row defaultValue="beGender">
          <FormControlLabel value="byGender" control={<Radio variant="plain" />} label="By Gender" />
          <FormControlLabel value="byGenre" control={<Radio variant="plain" />} label="By Genre" />
          <FormControlLabel value="bySong" control={<Radio variant="plain" />} label="By Song" />
        </RadioGroup>
      </FormControl>
    </StyledHeader>
  );
};

export default AppHeader;
