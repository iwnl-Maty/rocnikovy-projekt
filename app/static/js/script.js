var map = L.map("map").setView([49.981, 16.373], 8);

L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
  maxZoom: 19,
  attribution: "&copy; OpenStreetMap contributors",
}).addTo(map);

// Iterate through points passed from Flask via template
points.forEach((point) => {
  if (point.id) {
    L.marker([point.latitude, point.longitude]).addTo(map).bindPopup(`
      <b>${point.name}</b><br>
      ${point.description}<br>
      <a href='/detail/${point.id}'>Více informací</a>
    `);
  } else {
    console.error("Chybí ID pro bod:", point);
  }
});

document.getElementById("search").addEventListener("input", function (e) {
  const query = e.target.value.toLowerCase();
  let found = false;

  points.forEach((point) => {
    if (point.name.toLowerCase().includes(query)) {
      map.flyTo([point.latitude, point.longitude], 12);
      found = true;

      L.popup()
        .setLatLng([point.latitude, point.longitude])
        .setContent(`<b>${point.name}</b><br>${point.description}`)
        .openOn(map);
    }
  });

  if (!found && query !== "") {
    alert("Žádný bod zájmu nebyl nalezen!");
  }
});
