import { useContext } from "react";
import { StyledYear, StyledYearBox, StyledYearLabel } from "./Timeline.style";
import ChartsContext from "../../state/context";
import { onSelectDate } from "../../state/actions";

// eslint-disable-next-line react/prop-types
const YearBox = ({ year, label, date, addLabel }) => {
  const {
    state: { selectedDate },
    dispatch
  } = useContext(ChartsContext);

  const showLabel = addLabel ?? (label != null || year % 10 === 0);
  const yearLabel = label ?? `${year.toString().slice(2)}'s`;

  return (
    <StyledYear onClick={() => dispatch(onSelectDate(date))}>
      <StyledYearBox selected={selectedDate === date} />
      {showLabel && <StyledYearLabel>{yearLabel}</StyledYearLabel>}
    </StyledYear>
  );
};

export default YearBox;
