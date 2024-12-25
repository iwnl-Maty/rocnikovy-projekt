var map = L.map('map').setView([49.981, 16.373], 8);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; OpenStreetMap contributors'
}).addTo(map);

const points = [
    { name: "Praděd", coords: [50.083, 17.230], description: "Nejvyšší vrchol Jeseníků." },
    { name: "Šerák", coords: [50.170, 17.157], description: "Oblíbený turistický cíl s krásnými výhledy." },
    { name: "Karlova Studánka", coords: [49.790, 17.125], description: "Známé lázeňské město." },
    { name: "Rejvíz", coords: [50.244, 17.232], description: "Největší rašeliniště ve Slezsku." }
];

points.forEach(point => {
    L.marker(point.coords).addTo(map)
        .bindPopup(`<b>${point.name}</b><br>${point.description}`);
});

setTimeout(function () {
        map.invalidateSize();
    }, 100);

document.getElementById('search').addEventListener('input', function (e) {
    const query = e.target.value.toLowerCase();
    let found = false;

    points.forEach(point => {
        if (point.name.toLowerCase().includes(query)) {
            map.flyTo(point.coords, 12); // Přiblížení na bod
            found = true;

            L.popup()
                .setLatLng(point.coords)
                .setContent(`<b>${point.name}</b><br>${point.description}`)
                .openOn(map);
        }
    });

    if (!found && query !== "") {
        alert('Žádný bod zájmu nenalezen!');
    }
});