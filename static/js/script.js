var map = L.map('map').setView([49.981, 16.373], 8);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; OpenStreetMap contributors'
}).addTo(map);

L.marker([50.083, 14.417]).addTo(map)
    .bindPopup('Testovací bod: Praha')
    .openPopup();