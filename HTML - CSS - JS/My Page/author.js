// Author entries: mix of poems, image-based pieces, video-based thoughts
const entries = [
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
Soy esa persona que no vuelves a encontrar…`
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
`},


{
  title: "Dónde (no) estás",
  text: `No quiero que estés en un lugar que no es el tuyo
Quiero que brilles y te llenes de orgullo
Del bueno, no del malo….
Lleno de historias que escribas con tus manos

Son muchos los lugares donde podrías estar
Es como en los cuentos…
Es cuestión de imaginar…
Cuál es esa historia… que quieres contar…

Sé que el tiempo es adverso
Y las dudas te carcomen
Y que tu corazón va lento…
Cuando sientes descontento…

No vayas con la multitud …
Las respuestas son esquivas…
cuando ignoras tu luz…
y no muestras tu virtud…

Si es necesario, construye desde cero…
La soledad es amiga… de un corazón sincero…
Tú no te encuentras en el bullicio de la ciudad…
Pero sí en el momento en que sientas paz…

Y si alguien te pregunta…
¿Dónde no estás?
Diles que en palabras rotas
E historias sin contar…

`},


  {
    title: "Sobre escribir en la madrugada",
    image: "home-image.png",
    text: `A veces las palabras solo vienen cuando el mundo duerme. 
Escribo en silencio, como quien lanza mensajes en una botella.`
  },
  {
    title: "Poemas para quien fui",
    video: "https://www.youtube.com/embed/pdOTxXgzPV0",
    text: "Este video lo hice pensando en las versiones de mí que ya no están. Cada verso es una despedida amable."
  },
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
Soy esa persona que no vuelves a encontrar…`
  },
  {
    title: "Sobre escribir en la madrugada",
    image: "home-image.png",
    text: `A veces las palabras solo vienen cuando el mundo duerme. 
Escribo en silencio, como quien lanza mensajes en una botella.`
  },
  {
    title: "Poemas para quien fui",
    video: "https://www.youtube.com/embed/pdOTxXgzPV0",
    text: "Este video lo hice pensando en las versiones de mí que ya no están. Cada verso es una despedida amable."
  }
];

let currentIndex = 0;
const entriesPerLoad = 3;

function loadEntries() {
  const container = document.getElementById("author-entries-container");

  for (let i = 0; i < entriesPerLoad; i++) {
    if (currentIndex >= entries.length) return;

    const entry = entries[currentIndex];
    const div = document.createElement("div");
    div.className = "entry";

    const title = document.createElement("h3");
    title.textContent = entry.title;
    div.appendChild(title);

    // Optional image
    if (entry.image) {
      const img = document.createElement("img");
      img.src = entry.image;
      img.alt = "entry image";
      img.className = "entry-image";
      div.appendChild(img);
    }

    // Optional video
    if (entry.video) {
      const iframe = document.createElement("iframe");
      iframe.src = entry.video;
      iframe.allow = "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture";
      iframe.allowFullscreen = true;
      div.appendChild(iframe);
    }

// Text
    if (entry.text) {
    const isPoem = entry.text.includes("…") || entry.text.includes("\n\n");

    if (isPoem) {
      const text = document.createElement("pre");
      text.textContent = entry.text;
      text.className = "poem-text";
      div.appendChild(text);
    } else {
      const text = document.createElement("p");
      text.textContent = entry.text;
      div.appendChild(text);
    }
}
    container.appendChild(div);
    currentIndex++;
  }
}

// Infinite scroll
window.addEventListener("scroll", () => {
  if (window.innerHeight + window.scrollY >= document.body.offsetHeight - 300) {
    loadEntries();
  }
});

// Initial load
document.addEventListener("DOMContentLoaded", () => {
  loadEntries();
});
