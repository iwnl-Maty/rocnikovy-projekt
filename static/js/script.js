var map = L.map("map").setView([49.981, 16.373], 8);

L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
  maxZoom: 19,
  attribution: "&copy; OpenStreetMap contributors",
}).addTo(map);

const points = [
  {
    name: "Praděd",
    coords: [50.083, 17.23],
    description: "Nejvyšší vrchol Jeseníků.",
    image: "static/images/praded.png",
  },
  {
    name: "Šerák",
    coords: [50.17, 17.157],
    description: "Oblíbený turistický cíl s krásnými výhledy.",
    image: "static/images/serak.png",
  },
  {
    name: "Karlova Studánka",
    coords: [49.79, 17.125],
    description: "Známé lázeňské město.",
    image: "static/images/studanka.png",
  },
  {
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
            <a href='/detail?name=${encodeURIComponent(
              point.name
            )}&description=${encodeURIComponent(point.description)}'>
                Více informací
            </a>
        `);
});

document.getElementById("search").addEventListener("input", function (e) {
  const query = e.target.value.toLowerCase();
  let found = false;

  points.forEach((point) => {
    if (point.name.toLowerCase().includes(query)) {
      map.flyTo(point.coords, 12);
      found = true;

      L.popup()
        .setLatLng(point.coords)
        .setContent(`<b>${point.name}</b><br>${point.description}`)
        .openOn(map);
    }
  });

  if (!found && query !== "") {
    alert("Žádný bod zájmu nebyl nalezen!");
  }
});
