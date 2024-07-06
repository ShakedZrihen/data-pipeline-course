import { setupWorker } from "msw/browser";
import { http, passthrough } from "msw";
import { handlers } from "./handlers";

const worker = setupWorker(
  ...handlers,
  http.get("*", () => {
    return passthrough();
  })
);
await worker.start();
