import { StyledTimeline } from "./Timeline.style";
import { ALL_TIMES_YEAR } from "./consts";
import YearBox from "./YearBox";
import useTimeline from "./useTimeline";

const Timeline = () => {
  const { years, handleWheel } = useTimeline();

  return (
    <StyledTimeline onWheel={handleWheel}>
      <YearBox key={ALL_TIMES_YEAR} year={ALL_TIMES_YEAR} label="All times" />
      {years.map((year) => {
        return <YearBox key={year} year={year} />;
      })}
    </StyledTimeline>
  );
};

export default Timeline;
