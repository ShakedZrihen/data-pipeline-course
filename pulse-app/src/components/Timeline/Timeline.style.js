import { styled } from "@mui/material";

export const StyledTimeline = styled("div")`
  width: 10rem;
  display: flex;
  flex-direction: column;
`;

export const StyledYearBox = styled("div")`
  height: 1.2rem;
  width: 0.8rem;
  background-color: ${({ selected }) => (selected ? "#F4538A" : "white")};
`;

export const StyledYear = styled("div")`
  display: flex;
  align-items: center;
  margin-bottom: 1rem;

  :hover {
    cursor: pointer;
  }
`;

export const StyledYearLabel = styled("div")`
  margin-left: 1rem;
  font-weight: 700;
`;