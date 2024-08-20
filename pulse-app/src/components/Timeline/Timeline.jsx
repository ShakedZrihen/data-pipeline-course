import { StyledTimeline } from "./Timeline.style";
import { ALL_TIMES_YEAR } from "./consts";
import YearBox from "./YearBox";
import useTimeline from "./useTimeline";

const Timeline = () => {
  const { latestWeeks, handleWheel } = useTimeline();

  const years = Object.keys(latestWeeks).sort((a, b) => b - a);
  const dates = [];

  years.forEach((year) => {
    const yearDates = latestWeeks[year]; // DESC order
    const first = yearDates.pop();
    yearDates.forEach(({ date }) => {
      dates.push(<YearBox key={date} year={year} date={date} addLabel={false} />);
    });
    dates.push(<YearBox key={first.date} year={year} date={first.date} label={year} />);
  });

  return (
    <StyledTimeline /*onWheel={handleWheel}*/>
      <YearBox key={ALL_TIMES_YEAR} year={ALL_TIMES_YEAR} date={ALL_TIMES_YEAR} label="All times" />
      {dates}
    </StyledTimeline>
  );
};

export default Timeline;
