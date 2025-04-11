const startBtn = document.getElementById("start-button");
const backBtn = document.getElementById("back-button");
const musicToggle = document.getElementById("music-toggle");
const startScreen = document.getElementById("start-screen");
const gameScreen = document.getElementById("game-screen");
const bgMusic = document.getElementById("bg-music");

const container = document.getElementById("figure-container");
const figureName = document.getElementById("figure-name");
const message = document.getElementById("message");
const scoreDisplay = document.getElementById("score");

let score = 0;
const clickSound = new Audio("click2.mp3");

const figures = [
  // Figuras personalizadas con layout
  {
    name: "FIGURA T",
    type: "custom",
    layout: [
      [1, 1, 1],
      [0, 1, 0],
      [0, 1, 0]
    ]
  },
  {
    name: "CUADRADO GRANDE",
    type: "custom",
    layout: [
      [1, 1],
      [1, 1]
    ]
  },
  // Figura con SVG: CÍRCULO
  {
    name: "CÍRCULO",
    type: "svg",
    segments: 4,
    svg: `
      <svg viewBox="0 0 200 200" width="300" height="300">
        <path class="segment" d="M100,100 L100,0 A100,100 0 0,1 200,100 Z"/>
        <path class="segment" d="M100,100 L200,100 A100,100 0 0,1 100,200 Z"/>
        <path class="segment" d="M100,100 L100,200 A100,100 0 0,1 0,100 Z"/>
        <path class="segment" d="M100,100 L0,100 A100,100 0 0,1 100,0 Z"/>
      </svg>
    `
  },
  // Figura con SVG: TRIÁNGULO
  {
    name: "TRIÁNGULO",
    type: "svg",
    segments: 3,
    svg: `
      <svg viewBox="0 0 200 200" width="300" height="300">
        <polygon class="segment" points="100,10 10,180 100,100" />
        <polygon class="segment" points="100,10 190,180 100,100" />
        <polygon class="segment" points="10,180 190,180 100,100" />
      </svg>
    `
  },
  // Figura con SVG: ESTRELLA
  {
    name: "ESTRELLA",
    type: "svg",
    segments: 5,
    svg: `
      <svg viewBox="0 0 200 200" width="300" height="300">
        <polygon class="segment" points="100,10 120,70 100,100"/>
        <polygon class="segment" points="100,10 80,70 100,100"/>
        <polygon class="segment" points="80,70 20,75 100,100"/>
        <polygon class="segment" points="120,70 180,75 100,100"/>
        <polygon class="segment" points="20,75 100,190 180,75"/>
      </svg>
    `
  }
];

let currentFigureIndex = 0;

startBtn.addEventListener("click", () => {
  startScreen.style.display = "none";
  gameScreen.style.display = "block";
  bgMusic.pause();
  bgMusic.currentTime = 0;
  createFigure();
});

musicToggle.addEventListener("click", () => {
  if (bgMusic.paused) {
    bgMusic.play();
    musicToggle.textContent = "🎵";
  } else {
    bgMusic.pause();
    musicToggle.textContent = "🔇";
  }
});

backBtn.addEventListener("click", () => {
  gameScreen.style.display = "none";
  startScreen.style.display = "flex";
  bgMusic.play();
  resetGame();
});

function resetGame() {
  score = 0;
  scoreDisplay.textContent = "Puntos: 0";
  currentFigureIndex = 0;
  container.innerHTML = "";
  message.textContent = "";
}

function createFigure() {
  container.innerHTML = "";
  const figure = figures[currentFigureIndex];
  figureName.textContent = figure.name;
  message.textContent = "";

  if (figure.type === "custom") {
    const rows = figure.layout.length;
    const cols = figure.layout[0].length;
    container.style.display = "grid";
    container.style.gridTemplateColumns = `repeat(${cols}, 100px)`;
    container.style.gridTemplateRows = `repeat(${rows}, 100px)`;

    let segmentsClicked = 0;
    const totalSegments = figure.layout.flat().filter(n => n === 1).length;

    figure.layout.forEach((row) => {
      row.forEach((cell) => {
        const square = document.createElement("div");
        if (cell === 1) {
          square.classList.add("square-part");
          square.addEventListener("click", () => {
            if (!square.classList.contains("clicked")) {
              square.classList.add("clicked");
              clickSound.currentTime = 0;
              clickSound.play();
              segmentsClicked++;
              if (segmentsClicked === totalSegments) {
                score += 10;
                scoreDisplay.textContent = `Puntos: ${score}`;
                showMessageAndNext();
              }
            }
          });
        } else {
          square.style.visibility = "hidden";
          square.style.width = "100px";
          square.style.height = "100px";
        }
        container.appendChild(square);
      });
    });
  }

  if (figure.type === "svg") {
    container.style.display = "block";
    container.innerHTML = figure.svg;
    let segmentsClicked = 0;
    const parts = container.querySelectorAll(".segment");
    parts.forEach(part => {
      part.addEventListener("click", () => {
        if (!part.classList.contains("clicked")) {
          part.classList.add("clicked");
          clickSound.currentTime = 0;
          clickSound.play();
          segmentsClicked++;
          if (segmentsClicked === figure.segments) {
            score += 10;
            scoreDisplay.textContent = `Puntos: ${score}`;
            showMessageAndNext();
          }
        }
      });
    });
  }
}

function showMessageAndNext() {
  message.textContent = "¡Muy bien! La siguiente figura se cargará en...";
  let count = 3;
  const countdown = setInterval(() => {
    message.textContent = `¡Muy bien! La siguiente figura se cargará en... ${count}`;
    count--;
    if (count < 0) {
      clearInterval(countdown);
      currentFigureIndex = (currentFigureIndex + 1) % figures.length;
      createFigure();
    }
  }, 800);
}
