const entries = [
  {
    title: "How I Built My First App",
    video: "https://www.youtube.com/embed/dQw4w9WgXcQ", // Optional video
    text: "A short breakdown of how I structured and deployed my first web app using HTML, CSS, JS, and Firebase."
  },
  {
    title: "Code Snippet from My Portfolio",
    image: "home-image.png", // Optional image (put your image in the 'images' folder)
    text: "This is a snapshot from my portfolio site where I show how I use JavaScript to dynamically render content."
  },
  {
    title: "Tips for Learning to Code",
    text: "No media here! Just some honest thoughts on how to stay consistent and avoid burnout when learning to code."
  }
];

let currentIndex = 0;
const entriesPerLoad = 3;

function loadEntries() {
  const container = document.getElementById("entries-container");

  for (let i = 0; i < entriesPerLoad; i++) {
    if (currentIndex >= entries.length) return;

    const entry = entries[currentIndex];

    const div = document.createElement("div");
    div.className = "entry";

    const title = document.createElement("h3");
    title.textContent = entry.title;
    div.appendChild(title);

    if (entry.video) {
      const iframe = document.createElement("iframe");
      iframe.src = entry.video;
      iframe.allow = "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture";
      iframe.allowFullscreen = true;
      div.appendChild(iframe);
    }

    if (entry.image) {
      const img = document.createElement("img");
      img.src = entry.image;
      img.alt = entry.title;
      img.className = "entry-image";
      div.appendChild(img);
    }

    const text = document.createElement("p");
    text.textContent = entry.text;
    div.appendChild(text);

    container.appendChild(div);
    currentIndex++;
  }
}

window.addEventListener("scroll", () => {
  if (window.innerHeight + window.scrollY >= document.body.offsetHeight - 300) {
    loadEntries();
  }
});

document.addEventListener("DOMContentLoaded", () => {
  loadEntries();
});
