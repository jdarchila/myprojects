// Sample entries
const entries = [
  {
    title: "How to Stop Overthinking",
    video: "https://www.youtube.com/embed/pdOTxXgzPV0", // Replace with actual ID or leave empty
    text: "Overthinking is one of the biggest blockers of peace. In this entry, we explore simple techniques that allow us to return to the present moment and trust ourselves more deeply."
  },
  {
    title: "Letting Go of What No Longer Serves You",
    video: "https://www.youtube.com/embed/pdOTxXgzPV0",
    text: "There comes a time when we must let go of old habits, people, and beliefs to grow. This short essay is about recognizing that moment and taking action with kindness."
  },
  {
    title: "You Are Not Your Thoughts",
    video: "https://www.youtube.com/embed/pdOTxXgzPV0",
    text: "One of the most powerful shifts in therapy comes when people realize they are not their thoughts. This video and entry explain how to practice that realization daily."
  }
  ,
  {
    title: "You Are Not Your Thoughts",
    video: "https://www.youtube.com/embed/pdOTxXgzPV0",
    text: "One of the most powerful shifts in therapy comes when people realize they are not their thoughts. This video and entry explain how to practice that realization daily."
  }
  ,
  {
    title: "You Are Not Your Thoughts",
    video: "https://www.youtube.com/embed/pdOTxXgzPV0",
    text: "One of the most powerful shifts in therapy comes when people realize they are not their thoughts. This video and entry explain how to practice that realization daily."
  }
  // Add more entries here!
];

let currentIndex = 0;
const entriesPerLoad = 3; // Number of entries to load at a time

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

    const text = document.createElement("p");
    text.textContent = entry.text;
    div.appendChild(text);

    container.appendChild(div);
    currentIndex++;
  }
}

// Listen for scroll near bottom
window.addEventListener("scroll", () => {
  if (window.innerHeight + window.scrollY >= document.body.offsetHeight - 300) {
    loadEntries();
  }
});

// Initial load
document.addEventListener("DOMContentLoaded", () => {
  loadEntries();
});
