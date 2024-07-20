import { useContext } from "react";
import { StyledYear, StyledYearBox, StyledYearLabel } from "./Timeline.style";
import ChartsContext from "../../state/context";
import { onSelectYear } from "../../state/actions";

// eslint-disable-next-line react/prop-types
const YearBox = ({ year, label }) => {
  const {
    state: { selectedYear },
    dispatch
  } = useContext(ChartsContext);

  const showLabel = label != null || year % 10 === 0;
  const yearLabel = label ?? `${year.toString().slice(2)}'s`;

  return (
    <StyledYear onClick={() => dispatch(onSelectYear(year))}>
      <StyledYearBox selected={year === selectedYear} />
      {showLabel && <StyledYearLabel>{yearLabel}</StyledYearLabel>}
    </StyledYear>
  );
};

export default YearBox;
