import { Modal, styled, Typography } from "@mui/material";
import useCountryData from "./useCountryData";
import SongRow from "./SongRow";

const Wrapper = styled("div")`
  width: 50%;
  height: 90%;
  top: 5%;
  background: rgba(61, 64, 91, 0.5);
  border-radius: 0.4rem;
  position: relative;
  outline: none;
  margin: auto;
  padding: 2rem;
`;

const ChartWrapper = styled("div")`
  display: flex;
  flex-direction: column;
  margin-top: 2rem;
`;

const CountryModal = (props) => {
  const { name, chart } = useCountryData();

  return (
    <Modal {...props}>
      <Wrapper>
        <Typography variant="h3" component="h3">
          {name}
        </Typography>
        <ChartWrapper>
          {chart.map((song) => (
            <SongRow key={song.position} song={song} />
          ))}
        </ChartWrapper>
      </Wrapper>
    </Modal>
  );
};

export default CountryModal;
