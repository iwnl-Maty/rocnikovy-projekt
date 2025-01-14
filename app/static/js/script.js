var map = L.map("map").setView([49.981, 16.373], 8);

L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    maxZoom: 19,
    attribution: "&copy; OpenStreetMap contributors",
}).addTo(map);

const staticPoints = [
    {
        name: "Praděd",
        coords: [50.083, 17.23],
        description: "Nejvyšší vrchol Jeseníků.",
    },
    {
        name: "Šerák",
        coords: [50.17, 17.157],
        description: "Oblíbený turistický cíl s krásnými výhledy.",
    },
    {
        name: "Karlova Studánka",
        coords: [49.79, 17.125],
        description: "Známé lázeňské město.",
    },
];

staticPoints.forEach((point) => {
    L.marker(point.coords).addTo(map).bindPopup(`
        <b>${point.name}</b><br>${point.description}
    `);
});

points.forEach((point) => {
    L.marker([point.latitude, point.longitude])
        .addTo(map)
        .bindPopup(`<b>${point.name}</b><br>${point.description}`);
});
