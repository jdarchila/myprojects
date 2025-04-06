// Array of poems
const poems = [
  {
    title: "Los caminos de ida y vuelta",
    text: `Es volver a empezar una y otra vez…
Sentir que todo gira al revés… 
Es saber lo que me espera 
Sin pensar en el tal vez…

Lucho contra la marea…
Me olvido del ayer…  
Las ideas me dan vueltas 
Me pregunto el porqué…

Cómo saber quién soy…
Si vengo y me voy…
Cómo saber quién fui…
Si nunca me pude ir… 

Son pocas las señales
Son tantos los caminos 
A veces me pregunto…
¿Cuál es mi destino? 

Es acaso mirar al cielo…
y perderme en suspiros…
Es acaso tomar su mano…
Aunque no esté a mi lado…

Me pierdo en los recuerdos
Como si fuera el viento…
Me pierdo entre historias 
Y me encuentro…

Soy más que un caminante que viene y va…
Soy esa persona que no vuelves a encontrar…
`
  },

  {
    title: "Perderme en mis pasos",
    text: `Un paso tras otro, avanzo sin pensar…
Izquierda o derecha, todo se ve igual…
Sólo he aprendido, a no mirar atrás…
Las heridas del pasado, no son mi realidad

El tiempo me ha enseñado… 
Poco a poco a sanar…
Pero a veces desconozco…
Quien soy en realidad… 

La oscuridad me asusta…
Lo quiero confesar…
Camino entre las sombras…
Buscando libertad…

Si pudiera alejarme de mí… 
Yo te buscaría a ti…
Pero eres un recuerdo…
De un amor, que no fue de cuento

No sé a dónde voy…
No sé ni en dónde estoy…
He llegado hasta aquí 
Y no sé ni qué decir…

Me pierdo por el miedo…
Me pierdo por el sol…
Soy todo lo que pienso
Soy todo lo que no…

Me pierdo y me encuentro, un día a la vez
No dudes en abrazarme si un día me ves

`
  },

];

let currentPoem = 0;

// DOM references
const poemTitle = document.getElementById('poem-title');
const poemText = document.getElementById('poem-text');

// Display a poem by index
function showPoem(index) {
  const poem = poems[index];
  poemTitle.textContent = poem.title;
  poemText.textContent = poem.text;

  // 👇 Scroll the poem box to the top
  poemText.scrollTop = 0;
  poemTitle.scrollIntoView({ behavior: 'smooth' });
}

// Go to next poem
function nextPoem() {
  currentPoem = (currentPoem + 1) % poems.length;
  showPoem(currentPoem);
}

// Go to previous poem
function previousPoem() {
  currentPoem = (currentPoem - 1 + poems.length) % poems.length;
  showPoem(currentPoem);
}

// Initial load
showPoem(currentPoem);
