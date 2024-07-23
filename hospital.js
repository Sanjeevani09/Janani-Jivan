// Locate Hospital start    

function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showNearbyHospitals);
    } else { 
        x.innerHTML = "Geolocation is not supported by this browser.";
    }
}

function showNearbyHospitals(position) {
  const latitude = position.coords.latitude;
  const longitude = position.coords.longitude;
  
  // Construct the Google Maps URL with a search query for nearby hospitals
  const googleMapsUrl = `https://www.google.com/maps/search/hospitals/@${latitude},${longitude}`;
  
  // Open Google Maps in a new tab
  window.open(googleMapsUrl, '_blank');
}

// Locate Hospital start