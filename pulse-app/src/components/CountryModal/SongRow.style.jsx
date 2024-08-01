import { styled } from "@mui/material";
import HeadphonesIcon from "@mui/icons-material/Headphones";

export const SongWrapper = styled("div")`
  display: flex;
  flex-direction: row;
  align-items: center;
  padding: 0 1rem;
  margin-bottom: 0.7rem;
  background: ${({ position }) => (position % 2 ? `#9cffcd` : `#ff9cce`)};
`;

export const Position = styled("p")`
  font-size: 2rem;
  color: #13000a;
  font-weight: bold;
  margin: 0 0.5rem 0 0;
`;

export const Song = styled("p")`
  font-size: 1rem;
  color: #13000a;
  font-weight: bold;
  margin: 0;
`;

export const Artist = styled("p")`
  font-size: 1rem;
  color: #13000a;
  margin: 0;
  margin-left: 0.5rem;
  flex: 1;
`;

export const ListenIcon = styled(HeadphonesIcon)`
  color: #13000a;
  :hover {
    cursor: pointer;
  }
`;
