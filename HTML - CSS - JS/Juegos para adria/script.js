const container = document.getElementById("figure-container");
const figureName = document.getElementById("figure-name");
const clickSound = new Audio("click2.mp3");

// 10 figuras diferentes divididas
const figures = [
  {
    name: "TRIÁNGULO",
    segments: 3,
    svg: `
      <svg viewBox="0 0 200 200">
        <polygon class="segment" points="100,10 10,180 100,100" />
        <polygon class="segment" points="100,10 190,180 100,100" />
        <polygon class="segment" points="10,180 190,180 100,100" />
      </svg>
    `
  },
  {
    name: "CUADRADO",
    segments: 4,
    svg: `
      <svg viewBox="0 0 200 200">
        <rect class="segment" x="0" y="0" width="100" height="100"/>
        <rect class="segment" x="100" y="0" width="100" height="100"/>
        <rect class="segment" x="0" y="100" width="100" height="100"/>
        <rect class="segment" x="100" y="100" width="100" height="100"/>
      </svg>
    `
  },
  {
    name: "CÍRCULO",
    segments: 4,
    svg: `
      <svg viewBox="0 0 200 200">
        <path class="segment" d="M100,100 L100,0 A100,100 0 0,1 200,100 Z"/>
        <path class="segment" d="M100,100 L200,100 A100,100 0 0,1 100,200 Z"/>
        <path class="segment" d="M100,100 L100,200 A100,100 0 0,1 0,100 Z"/>
        <path class="segment" d="M100,100 L0,100 A100,100 0 0,1 100,0 Z"/>
      </svg>
    `
  },
  {
    name: "ESTRELLA",
    segments: 5,
    svg: `
      <svg viewBox="0 0 200 200">
        <polygon class="segment" points="100,10 120,70 100,100"/>
        <polygon class="segment" points="100,10 80,70 100,100"/>
        <polygon class="segment" points="80,70 20,75 100,100"/>
        <polygon class="segment" points="120,70 180,75 100,100"/>
        <polygon class="segment" points="20,75 100,190 180,75"/>
      </svg>
    `
  },
  {
    name: "RECTÁNGULO",
    segments: 4,
    svg: `
      <svg viewBox="0 0 400 200">
        <rect class="segment" x="0" y="0" width="100" height="200"/>
        <rect class="segment" x="100" y="0" width="100" height="200"/>
        <rect class="segment" x="200" y="0" width="100" height="200"/>
        <rect class="segment" x="300" y="0" width="100" height="200"/>
      </svg>
    `
  },
  {
    name: "ROMBO",
    segments: 4,
    svg: `
      <svg viewBox="0 0 200 200">
        <polygon class="segment" points="100,0 150,100 100,100"/>
        <polygon class="segment" points="100,0 50,100 100,100"/>
        <polygon class="segment" points="50,100 100,200 100,100"/>
        <polygon class="segment" points="150,100 100,200 100,100"/>
      </svg>
    `
  },
  {
    name: "PENTÁGONO",
    segments: 5,
    svg: `
      <svg viewBox="0 0 200 200">
        <polygon class="segment" points="100,0 150,70 100,100"/>
        <polygon class="segment" points="100,0 50,70 100,100"/>
        <polygon class="segment" points="50,70 30,150 100,100"/>
        <polygon class="segment" points="150,70 170,150 100,100"/>
        <polygon class="segment" points="30,150 170,150 100,100"/>
      </svg>
    `
  },
  {
    name: "HEXÁGONO",
    segments: 6,
    svg: `
      <svg viewBox="0 0 200 200">
        <polygon class="segment" points="100,0 140,30 100,100"/>
        <polygon class="segment" points="140,30 170,80 100,100"/>
        <polygon class="segment" points="170,80 140,130 100,100"/>
        <polygon class="segment" points="140,130 60,130 100,100"/>
        <polygon class="segment" points="60,130 30,80 100,100"/>
        <polygon class="segment" points="30,80 60,30 100,100"/>
      </svg>
    `
  },
  {
    name: "TRAPEZOIDE",
    segments: 4,
    svg: `
      <svg viewBox="0 0 200 200">
        <polygon class="segment" points="60,50 140,50 130,100 70,100"/>
        <polygon class="segment" points="70,100 130,100 120,150 80,150"/>
        <polygon class="segment" points="60,50 70,100 80,150 40,100"/>
        <polygon class="segment" points="140,50 130,100 120,150 160,100"/>
      </svg>
    `
  },
  {
    name: "CORAZÓN",
    segments: 3,
    svg: `
      <svg viewBox="0 0 200 200">
        <path class="segment" d="M100,30 A30,30 0 0,1 130,60 L100,100 Z"/>
        <path class="segment" d="M100,30 A30,30 0 0,0 70,60 L100,100 Z"/>
        <path class="segment" d="M70,60 Q100,150 130,60 L100,100 Z"/>
      </svg>
    `
  }
];

let currentFigureIndex = 0;

function createFigure() {
  container.innerHTML = '';
  const figure = figures[currentFigureIndex];
  figureName.textContent = figure.name;
  let segmentsClicked = 0;

  container.innerHTML = figure.svg;

  const parts = container.querySelectorAll('.segment');
  parts.forEach(part => {
    part.addEventListener('click', () => {
      if (!part.classList.contains('clicked')) {
        part.classList.add('clicked');
        clickSound.currentTime = 0;
        clickSound.play();
        segmentsClicked++;

        if (segmentsClicked === figure.segments) {
          setTimeout(() => {
            currentFigureIndex = (currentFigureIndex + 1) % figures.length;
            createFigure();
          }, 800);
        }
      }
    });
  });
}

createFigure();
