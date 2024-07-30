import { http, passthrough } from "msw";
import { handlers as chartsHandlers } from "./charts";

export const handlers = [
  ...chartsHandlers,
  http.get("*", () => {
    return passthrough();
  })
];
