const player = document.getElementById('player');
const npc = document.getElementById('npc');
const dialogueBox = document.getElementById('dialogue-box');
const gameContainer = document.getElementById('game-container');

let position = {
  x: 200,
  y: 200,
  step: 10
};

const playerSize = 40;
let score = 0;

document.addEventListener('keydown', (e) => {
  const containerWidth = gameContainer.clientWidth;
  const containerHeight = gameContainer.clientHeight;

  let nextX = position.x;
  let nextY = position.y;

  switch(e.key) {
    case 'ArrowUp':
      nextY -= position.step;
      break;
    case 'ArrowDown':
      nextY += position.step;
      break;
    case 'ArrowLeft':
      nextX -= position.step;
      break;
    case 'ArrowRight':
      nextX += position.step;
      break;
    case 'e':
    case 'E':
      if (isNearElement(npc)) {
        showDialogue();
      } else {
        tryPickupItems();
      }
      return;
  }

  if (
    nextX >= 0 &&
    nextX + playerSize <= containerWidth &&
    nextY >= 0 &&
    nextY + playerSize <= containerHeight &&
    !isCollidingWith(npc, nextX, nextY)
  ) {
    position.x = nextX;
    position.y = nextY;
    player.style.left = position.x + 'px';
    player.style.top = position.y + 'px';
  }
});

function isNearElement(element) {
  const rect1 = player.getBoundingClientRect();
  const rect2 = element.getBoundingClientRect();

  const distanceX = Math.abs(rect1.left - rect2.left);
  const distanceY = Math.abs(rect1.top - rect2.top);

  return distanceX < 50 && distanceY < 50;
}

function isCollidingWith(element, nextX, nextY) {
  const elX = element.offsetLeft;
  const elY = element.offsetTop;
  const elSize = 40;

  return (
    nextX < elX + elSize &&
    nextX + playerSize > elX &&
    nextY < elY + elSize &&
    nextY + playerSize > elY
  );
}

function showDialogue() {
  dialogueBox.style.left = npc.offsetLeft + 'px';
  dialogueBox.style.top = (npc.offsetTop - 50) + 'px';
  dialogueBox.style.display = 'block';

  setTimeout(() => {
    dialogueBox.style.display = 'none';
  }, 3000);
}

function tryPickupItems() {
  const items = document.querySelectorAll('.item');
  items.forEach(item => {
    if (isNearElement(item)) {
      const itemName = item.dataset.name || 'Objeto misterioso';
      item.remove();
      score++;
      document.getElementById('score').innerText = `Objetos: ${score}`;
      addToInventory(itemName);
    }
  });
}

function addToInventory(name) {
  const list = document.getElementById('inventory-list');
  const li = document.createElement('li');
  li.textContent = name;
  list.appendChild(li);
}
