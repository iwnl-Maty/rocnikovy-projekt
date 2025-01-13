var map = L.map("map").setView([49.981, 16.373], 8);

L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
  maxZoom: 19,
  attribution: "&copy; OpenStreetMap contributors",
}).addTo(map);

const points = JSON.parse(mapPoints);

points.forEach((point) => {
  L.marker([point.latitude, point.longitude]).addTo(map).bindPopup(`
    <b>${point.name}</b><br>
    ${point.description}<br>
    <a href="/detail/${point.id}">Více informací</a>
  `);
});
