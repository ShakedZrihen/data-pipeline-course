import { createTheme, ThemeProvider } from "@mui/material/styles";
import { CssBaseline, styled } from "@mui/material";
import Timeline from "./components/Timeline/Timeline";
import WorldMap from "./components/WorldMap/WorldMap";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";

const darkTheme = createTheme({
  palette: {
    mode: "dark"
  }
});

const StyledHeader = styled("header")`
  width: 100%;
  display: flex;
  align-items: center;
  flex-direction: row;
`;

const StyledAppContainer = styled("div")`
  padding: 2rem 4rem;
  display: flex;
  flex-direction: column;
  width: 100%;
`;

const StyledContent = styled("div")`
  display: flex;
  flex-direction: row-reverse;
  width: 100%;
  justify-content: space-between;
`;

const StyledWorldMapContainer = styled("div")`
  width: 80%;
`;

const queryClient = new QueryClient();

const App = () => {
  return (
    <ThemeProvider theme={darkTheme}>
      <QueryClientProvider client={queryClient}>
        <CssBaseline />
        <StyledAppContainer>
          <StyledHeader>
            <h1 style={{ color: "white" }}>Pulse</h1>
          </StyledHeader>
          <StyledContent>
            <Timeline />
            <StyledWorldMapContainer>
              <WorldMap />
            </StyledWorldMapContainer>
          </StyledContent>
        </StyledAppContainer>
      </QueryClientProvider>
    </ThemeProvider>
  );
};

export default App;
