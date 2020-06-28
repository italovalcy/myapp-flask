// performance-test.js

import { sleep } from "k6";
import http from "k6/http";

export let options = {
  duration: "30s",
  vus: 50
};

export default function() {
  http.get("http://myapp-flask-1");
  sleep(1);
}

