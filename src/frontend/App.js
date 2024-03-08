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
        // Call a function to save coordinates to a file
        saveCoordinatesToFile(
          data.location_data.latitude,
          data.location_data.longitude
        );

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

function saveCoordinatesToFile(latitude, longitude) {
  // Create a GeoJSON-like structure with the coordinates
  const geoJsonData = {
    type: "FeatureCollection",
    features: [
      {
        type: "Feature",
        geometry: {
          type: "Point",
          coordinates: [longitude, latitude],
        },
        properties: {
          name: "Uploaded Location",
        },
      },
      // Add more features if needed
    ],
  };

  // Convert the GeoJSON data to a JSON string
  const jsonContent = JSON.stringify(geoJsonData, null, 2);

  // Create a Blob with the JSON content
  const blob = new Blob([jsonContent], { type: "application/json" });

  // Create a link element and trigger a download
  const link = document.createElement("a");
  link.href = URL.createObjectURL(blob);
  link.download = "uploaded_coordinates.geojson";
  link.click();
}

function displayLocationOnMap(latitude, longitude) {
  // Create a new marker and add it to the map
  var marker = L.marker([latitude, longitude])
    .addTo(map)
    .bindPopup("Uploaded Location")
    .openPopup();

  // Add the marker to the markers array
  markers.push(marker);
}
