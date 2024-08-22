import { styled } from "@mui/material";

export const StyledStatsBox = styled("div")`
  width: 100%;
  height: 15rem;
  margin-top: 3rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
`;

export const LineBox = styled("div")`
  width: 1.7rem;
  height: 1rem;
  margin-bottom: 0.5rem;
  background-color: ${({ color }) => color ?? "red"};
`;

export const LineContainer = styled("div")`
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  height: 100%;
  margin: 0 0.3rem;
  align-items: center;
`;

export const GraphContainer = styled("div")`
  display: flex;
  align-items: flex-end;
  justify-content: center;
`;

export const Label = styled("p")`
  margin: 0;
`;
