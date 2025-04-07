const musicianEntries = [
  {
    title: "My First Original Song",
    video: "https://www.youtube.com/embed/pdOTxXgzPV0",
    text: "This song was born from a quiet moment, where emotions felt louder than thoughts. It's a reminder that vulnerability and melody can live together and say what words alone can’t."
  },
  {
    title: "Improvising in the Dark",
    video: "https://www.youtube.com/embed/pdOTxXgzPV0",
    text: "Sometimes I sit at the piano with no plan and let the day speak through the keys. This piece came out of one of those nights—raw, unedited, and true."
  },
  {
    title: "The Rhythm of Silence",
    video: "https://www.youtube.com/embed/pdOTxXgzPV0",
    text: "Music isn’t always about sound. In this short piece, I explore the power of pauses and restraint, showing how silence can sometimes hit harder than any note."
  }
];

let musicIndex = 0;
const musicPerLoad = 3;

function loadMusicEntries() {
  const container = document.getElementById("musician-entries");

  for (let i = 0; i < musicPerLoad; i++) {
    if (musicIndex >= musicianEntries.length) return;

    const entry = musicianEntries[musicIndex];

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

    const text = document.createElement("p");
    text.textContent = entry.text;
    div.appendChild(text);

    container.appendChild(div);
    musicIndex++;
  }
}

window.addEventListener("scroll", () => {
  if (window.innerHeight + window.scrollY >= document.body.offsetHeight - 300) {
    loadMusicEntries();
  }
});

document.addEventListener("DOMContentLoaded", () => {
  loadMusicEntries();
});
