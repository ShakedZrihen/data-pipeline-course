import { useState } from "react";
import { StyledTimeline, StyledYear, StyledYearBox, StyledYearLabel } from "./Timeline.style";
import useChartAvailableDates from "../../hooks/useChartAvailableDates";

const Timeline = () => {
  const [selectedYear, setSelectedYear] = useState(2019);
  const { data } = useChartAvailableDates();
  const years = Object.keys(data).sort((a, b) => Number(b) - Number(a));

  return (
    <StyledTimeline>
      <StyledYear key="all-times" onClick={() => setSelectedYear("all-times")}>
        <StyledYearBox selected={selectedYear === "all-times"} />
        <StyledYearLabel>All times</StyledYearLabel>
      </StyledYear>
      {years.map((year) => {
        const showLabel = year % 10 === 0;
        return (
          <StyledYear key={year} onClick={() => setSelectedYear(year)}>
            <StyledYearBox selected={year === selectedYear} />
            {showLabel && <StyledYearLabel>{year.toString().slice(2)}&apos;s</StyledYearLabel>}
          </StyledYear>
        );
      })}
    </StyledTimeline>
  );
};

export default Timeline;
