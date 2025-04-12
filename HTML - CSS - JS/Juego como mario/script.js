const player = document.getElementById("player");
const game = document.getElementById("game");
const platforms = document.querySelectorAll(".platform");

let velocityY = 0;
let gravity = 0.8;
let isJumping = false;
let onGround = false;

let positionX = 100;
let positionY = 300;

const keys = {
  left: false,
  right: false
};

document.addEventListener("keydown", (e) => {
  if (e.key === "ArrowLeft") keys.left = true;
  if (e.key === "ArrowRight") keys.right = true;
  if (e.key === " " && onGround) {
    velocityY = -15;
    isJumping = true;
    onGround = false;
  }
});

document.addEventListener("keyup", (e) => {
  if (e.key === "ArrowLeft") keys.left = false;
  if (e.key === "ArrowRight") keys.right = false;
});

function gameLoop() {
  // Movimiento horizontal con límites
  if (keys.left) positionX -= 5;
  if (keys.right) positionX += 5;

  if (positionX < 0) positionX = 0;
  if (positionX > 760) positionX = 760; // 800 - 40 (ancho del juego - ancho del jugador)

  // Gravedad
  velocityY += gravity;
  positionY += velocityY;

  // Suelo
  if (positionY > 310) {
    positionY = 310;
    velocityY = 0;
    onGround = true;
    isJumping = false;
  }

  // Plataformas
  platforms.forEach(platform => {
    const pRect = platform.getBoundingClientRect();
    const playerRect = player.getBoundingClientRect();
    const gameRect = game.getBoundingClientRect();

    if (
      playerRect.bottom <= pRect.top + 10 &&
      playerRect.bottom + velocityY >= pRect.top &&
      playerRect.right > pRect.left &&
      playerRect.left < pRect.right
    ) {
      positionY = pRect.top - gameRect.top - 40;
      velocityY = 0;
      isJumping = false;
      onGround = true;
    }
  });

  // Aplicar posiciones
  player.style.left = positionX + "px";
  player.style.top = positionY + "px";

  requestAnimationFrame(gameLoop);
}

gameLoop();
