requirejs(["mapboxgl"], function(mapboxgl) {
    var map = window.__jm_maps["{{uuid}}"];

    var run = function() {
        map.addLayer({
            "id": "{{layer_uuid}}",
            "source": "{{source_uuid}}",
            "type": "{{kind}}",
            "paint": {{&paint}}
        });
    }

    if (map._loaded) {
        run();
    } else {
        map.on("load", run);
    }
});
