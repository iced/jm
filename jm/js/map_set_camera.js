requirejs(["mapboxgl"], function(mapboxgl) {
    var map = window.__jm_maps["{{uuid}}"];

    var run = function() {
        var camera = {
            {{#center}}
            center: {{center.value}},
            {{/center}}
            {{#zoom}}
            zoom: {{zoom}},
            {{/zoom}}
            {{#bearing}}
            bearing: {{bearing}},
            {{/bearing}}
            {{#pitch}}
            pitch: {{pitch}},
            {{/pitch}}
        };

        if ({{animate}} != 0) {
            camera.duration = {{animate}};
            map.easeTo(camera);
        } else {
            map.jumpTo(camera);
        }
    }

    if (map._loaded) {
        run();
    } else {
        map.on("load", run);
    }
});
