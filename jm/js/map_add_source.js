requirejs(["mapboxgl"], function(mapboxgl) {
    var map = window.__jm_maps["{{uuid}}"];

    var run = function() {
        map.addSource("{{source_uuid}}", {{&data}})
    }

    if (map._loaded) {
        run();
    } else {
        map.on("load", run);
    }
});
