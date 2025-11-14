export default function handler(req, res) {
  const jokes = [
    "Why don’t programmers like nature? It has too many bugs!",
    "Why do Java developers wear glasses? Because they don't C#.",
    "Debugging: Being the detective in a crime movie where you are also the murderer.",
    "I told my computer I needed a break… it said 'No problem, I'll go to sleep.'"
  ];

  const randomJoke = jokes[Math.floor(Math.random() * jokes.length)];

  res.status(200).json({ joke: randomJoke });
}
