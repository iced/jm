requirejs(["mapboxgl"], function(mapboxgl) {
    var map = window.__jm_maps["{{uuid}}"];

    var findBounds = function(bounds, coordinates) {
        if (coordinates[0] instanceof Array) {
            coordinates.forEach(function(c) {
                bounds = findBounds(bounds, c);
            });
        } else {
            if (bounds === undefined) {
                bounds = new mapboxgl.LngLatBounds(coordinates, coordinates);
            } else {
                bounds = bounds.extend(coordinates);
            }
        }
        return bounds;
    }

    var run = function() {
        var source = map.getSource("{{source_uuid}}");
        var geojson = source._data;
        var bounds = undefined;
        geojson.features.forEach(function(feature) {
            bounds = findBounds(bounds, feature.geometry.coordinates);
        });

        map.fitBounds(bounds, {
            padding: {{padding}},
            linear: true,
            {{#animate}}
            duration: {{animate}},
            animate: true,
            {{/animate}}
            {{^animate}}
            animate: false,
            {{/animate}}
        });
    }

    if (map._loaded) {
        run();
    } else {
        map.on("load", run);
    }
});
