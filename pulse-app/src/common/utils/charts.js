export const getTopSongFeaturesByCountry = (charts) => {
  const featuresByCountry = Object.entries(charts).reduce((acc, [country, chart]) => {
    const genre = chart?.[0]?.songFeatures?.genre ?? "unknown";
    const artistType = chart?.[0]?.artistFeatures?.type ?? "unknown";
    const artistGender = chart?.[0]?.artistFeatures?.gender ?? "unknown";
    acc[country] = { genre, artistType: artistType === "Solo" ? artistGender : artistType, raw: chart[0] };

    return acc;
  }, {});

  return featuresByCountry;
};
