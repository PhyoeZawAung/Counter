import streamlit as st
import streamlit.components.v1 as components
html = """
<!DOCTYPE html>
<html lang="en" data-theme="dark">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <link
      href="https://cdn.jsdelivr.net/npm/daisyui@2.46.0/dist/full.css"
      rel="stylesheet"
      type="text/css"
    />
    <script src="https://cdn.tailwindcss.com"></script>
  </head>
  <body>
    <div class="flex flex-col w-screen h-screen justify-center items-center">
      <h1 class="text-5xl font-bold mb-10">
        Countdown to
        <span
          class="text-transparent bg-clip-text bg-gradient-to-r from-white to-amber-400"
          >5 PM</span
        >
      </h1>
      <div class="flex flex-row">
        <div
          class="flex flex-col p-2 bg-neutral rounded-box text-neutral-content mr-5"
        >
          <span class="countdown font-mono text-5xl">
            <span id="hoursDigit" style="--value: 0"></span>
          </span>
          hours
        </div>
        <div
          class="flex flex-col p-2 bg-neutral rounded-box text-neutral-content mr-5"
        >
          <span class="countdown font-mono text-5xl">
            <span id="minutesDigit" style="--value: 0"></span>
          </span>
          min
        </div>
        <div
          class="flex flex-col p-2 bg-neutral rounded-box text-neutral-content mr-5"
        >
          <span class="countdown font-mono text-5xl">
            <span id="secondsDigit" style="--value: 0"></span>
          </span>
          sec
        </div>
      </div>
    </div>
  </body>
  <script>
    const addOneDay = (current) => {
      return new Date(current.getTime() + 24 * 60 * 60 * 1000);
    };
    const setTime = () => {
      const givenTime = new Date();
      let fivePM = new Date("2022-12-26 17:00:00");

      while (fivePM < givenTime) {
        fivePM = addOneDay(fivePM);
        console.log("Adding one day!!!");
      }

      const timeDifference = fivePM - givenTime;

      const hours = Math.floor(timeDifference / (1000 * 60 * 60));
      const minutes = Math.floor(
        (timeDifference % (1000 * 60 * 60)) / (1000 * 60)
      );
      const seconds = Math.floor((timeDifference % (1000 * 60)) / 1000);

      document.getElementById("hoursDigit").style.setProperty("--value", hours);
      document
        .getElementById("minutesDigit")
        .style.setProperty("--value", minutes);
      document
        .getElementById("secondsDigit")
        .style.setProperty("--value", seconds);
    };
    setInterval(setTime, 100);
  </script>
</html>
"""
components.html(html, height=500)