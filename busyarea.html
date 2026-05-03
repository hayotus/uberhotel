<?php
// ---------------------------
// DATA (districtlar)
// ---------------------------
$districts = [
    [
        "name" => "Soho",
        "color" => "#00ff00",
        "coords" => [
            [40.724, -74.002],
            [40.725, -73.995],
            [40.720, -73.995],
            [40.720, -74.002]
        ]
    ],
    [
        "name" => "Midtown",
        "color" => "#0000ff",
        "coords" => [
            [40.760, -73.990],
            [40.760, -73.975],
            [40.750, -73.975],
            [40.750, -73.990]
        ]
    ]
];

// agar API so‘rovi bo‘lsa JSON qaytaradi
if (isset($_GET['api'])) {
    header('Content-Type: application/json');
    echo json_encode($districts);
    exit;
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>NYC District Map</title>
    <link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css"/>
    <style>
        #map { height: 100vh; width: 100%; }
        body { margin: 0; }
    </style>
</head>
<body>

<div id="map"></div>

<script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
<script>
    // map center
    var map = L.map('map').setView([40.73, -73.98], 12);

    // tile layer
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: 'NYC Map'
    }).addTo(map);

    // PHP API dan data olish (shu faylning o‘zi)
    fetch('?api=1')
        .then(res => res.json())
        .then(data => {

            data.forEach(d => {
                let poly = L.polygon(d.coords, {
                    color: d.color,
                    fillColor: d.color,
                    fillOpacity: 0.4,
                    weight: 2
                }).addTo(map);

                poly.bindPopup("<b>" + d.name + "</b>");
            });

        });
</script>

</body>
</html>
