requirejs(["mapboxgl"], function(mapboxgl) {
    var map = window.__jm_maps["{{uuid}}"];

    var run = function() {
        var source = map.getSource("{{source_uuid}}");
        var geojson = source._data;
        var coordinates = geojson.features[0].geometry.coordinates[0];
        if (coordinates[0] instanceof Array) {
            coordinates = coordinates[0];
        }
        var bounds = new mapboxgl.LngLatBounds(coordinates, coordinates);
        geojson.features.forEach(function(feature) {
            coordinates = feature.geometry.coordinates;
            if (coordinates[0] instanceof Array) {
                coordinates = coordinates[0];
            }
            bounds = coordinates.reduce(function(bounds, coord) {
                return bounds.extend(coord);
            }, bounds);
        });

        map.fitBounds(bounds, {
            padding: {{padding}}
        });
    }

    if (map._loaded) {
        run();
    } else {
        map.on("load", run);
    }
});
