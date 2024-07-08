import { useContext } from "react";
import { StyledTimeline, StyledYear, StyledYearBox, StyledYearLabel } from "./Timeline.style";
import useChartAvailableDates from "../../hooks/useChartAvailableDates";
import ChartsContext from "../../state/context";
import { onSelectYear } from "../../state/actions";

const ALL_TIMES_YEAR = "all-times";

const Timeline = () => {
  const {
    state: { selectedYear },
    dispatch
  } = useContext(ChartsContext);
  const { data } = useChartAvailableDates();
  const years = Object.keys(data).sort((a, b) => Number(b) - Number(a));

  return (
    <StyledTimeline>
      <StyledYear key={ALL_TIMES_YEAR} onClick={() => dispatch(onSelectYear(ALL_TIMES_YEAR))}>
        <StyledYearBox selected={selectedYear === ALL_TIMES_YEAR} />
        <StyledYearLabel>All times</StyledYearLabel>
      </StyledYear>
      {years.map((year) => {
        const showLabel = year % 10 === 0;
        return (
          <StyledYear key={year} onClick={() => dispatch(onSelectYear(year))}>
            <StyledYearBox selected={year === selectedYear} />
            {showLabel && <StyledYearLabel>{year.toString().slice(2)}&apos;s</StyledYearLabel>}
          </StyledYear>
        );
      })}
    </StyledTimeline>
  );
};

export default Timeline;
