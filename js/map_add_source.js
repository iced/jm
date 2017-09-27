requirejs(["mapboxgl"], function(mapboxgl) {
    var map = window.__jm_maps["{{uuid}}"];

    var run = function() {
        map.addSource("{{source_uuid}}", {{&data}})
    }

    if (map.loaded()) {
        run();
    } else {
        map.on("load", run);
    }
});
