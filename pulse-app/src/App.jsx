import { createTheme, ThemeProvider } from "@mui/material/styles";
import { CssBaseline, styled } from "@mui/material";
import Timeline from "./components/Timeline/Timeline";
import WorldMap from "./components/WorldMap/WorldMap";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { ChartsContextProvider } from "./state/context";
import AppHeader from "./components/AppHeader";
import GenderStats from "./components/StatsBox/GenderStats";

const darkTheme = createTheme({
  palette: {
    mode: "dark"
  }
});

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
  display: flex;
`;

const StyledStatsContainer = styled("div")`
  display: flex;
  flex-direction: column;
  width: 25%;
`;

const queryClient = new QueryClient();

const App = () => {
  return (
    <ThemeProvider theme={darkTheme}>
      <CssBaseline />
      <QueryClientProvider client={queryClient}>
        <ChartsContextProvider>
          <StyledAppContainer>
            <AppHeader />
            <StyledContent>
              <Timeline />
              <StyledWorldMapContainer>
                <StyledStatsContainer>
                  <GenderStats />
                </StyledStatsContainer>
                <WorldMap />
              </StyledWorldMapContainer>
            </StyledContent>
          </StyledAppContainer>
        </ChartsContextProvider>
      </QueryClientProvider>
    </ThemeProvider>
  );
};

export default App;
