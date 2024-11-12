var map;
var markers = [];

document.addEventListener("DOMContentLoaded", function () {
  if (!map) {
    map = L.map("map").setView([49.2827, -123.1207], 12);

    // Add a tile layer from OpenStreetMap
    L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
      maxZoom: 19,
      attribution:
        '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
    }).addTo(map);

    console.log("Map initialization completed.");
  }
});

function uploadFile() {
  const fileInput = document.getElementById("fileInput");
  const file = fileInput.files[0];

  const formData = new FormData();
  formData.append("file", file);

  fetch("http://127.0.0.1:5000/upload", {
    method: "POST",
    body: formData,
  })
    .then((response) => response.json())
    .then((data) => {
      console.log("File uploaded successfully:", data);

      if (
        data.location_data &&
        data.location_data.latitude &&
        data.location_data.longitude
      ) {
        // Call a function to display the location on the map
        displayLocationOnMap(
          data.location_data.latitude,
          data.location_data.longitude
        );
      }
    })
    .catch((error) => {
      console.error("Error uploading file:", error);
    });
}

function displayLocationOnMap(latitude, longitude) {
  // Create a new marker and add it to the map
  var marker = L.marker([latitude, longitude])
    .addTo(map)
    .bindPopup("New Waste Hotspot")
    .openPopup();

  // Add the marker to the markers array
  markers.push(marker);
  console.log("Marker added to the map at coordinates:", [latitude, longitude]);
}
