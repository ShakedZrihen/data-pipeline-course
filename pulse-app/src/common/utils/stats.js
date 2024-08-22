export const normalizeCounts = (obj) => {
  const maxCount = Math.max(...Object.values(obj));
  const scale = 7 / maxCount;

  const normalizedObj = {};
  for (const key in obj) {
    normalizedObj[key] = Math.round(obj[key] * scale); // Round if you want to keep integers
  }

  return normalizedObj;
};
