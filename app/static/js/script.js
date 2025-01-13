var map = L.map("map").setView([49.981, 16.373], 8);

L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
  maxZoom: 19,
  attribution: "&copy; OpenStreetMap contributors",
}).addTo(map);

const points = [
  {
    id: 1,
    name: "Praděd",
    coords: [50.083, 17.23],
    description: "Nejvyšší vrchol Jeseníků.",
    image: "static/images/praded.png",
  },
  {
    id: 2,
    name: "Šerák",
    coords: [50.17, 17.157],
    description: "Oblíbený turistický cíl s krásnými výhledy.",
    image: "static/images/serak.png",
  },
  {
    id: 3,
    name: "Karlova Studánka",
    coords: [49.79, 17.125],
    description: "Známé lázeňské město.",
    image: "static/images/studanka.png",
  },
  {
    id: 4,
    name: "Rejvíz",
    coords: [50.244, 17.232],
    description: "Největší rašeliniště ve Slezsku.",
    image: "static/images/rejviz.png",
  },
];

points.forEach((point) => {
  L.marker(point.coords).addTo(map).bindPopup(`
    <b>${point.name}</b><br>
    ${point.description}<br>
    <a href='/detail/${point.id}'>Více informací</a>
  `);
});
