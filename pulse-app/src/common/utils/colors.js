import { COLOR_PALETTES } from "../../components/WorldMap/featureColors";

export const hashGenreToIndex = (genre = "") => {
  let hash = 0;
  for (let i = 0; i < genre.length; i++) {
    hash = genre.charCodeAt(i) + ((hash << 5) - hash);
    hash = hash & hash; // Convert to 32bit integer
  }
  return Math.abs(hash) % COLOR_PALETTES.length;
};
