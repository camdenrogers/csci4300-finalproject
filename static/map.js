function initMap() {
    console.log(latitude)
    console.log(longitude)
    var location = {lat: latitude, lng: longitude};
    var map = new google.maps.Map(document.getElementById('map'), {zoom: 7, center: location});
    var marker = new google.maps.Marker({position: location, map: map});
}
