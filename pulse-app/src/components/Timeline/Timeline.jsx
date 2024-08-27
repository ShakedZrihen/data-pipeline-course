import { StyledTimeline } from "./Timeline.style";
import YearBox from "./YearBox";
import useTimeline from "./useTimeline";

const Timeline = () => {
  const { latestWeeks } = useTimeline();

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

  return <StyledTimeline /*onWheel={handleWheel}*/>{dates}</StyledTimeline>;
};

export default Timeline;
