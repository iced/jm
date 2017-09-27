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

    {{#popup}}
    map.on("click", "{{layer_uuid}}", function(e) {
        console.log(e);
        new mapboxgl.Popup()
            .setLngLat(e.lngLat)
            .setHTML(e.features[0].properties.{{popup}})
            .addTo(map);
    });
    {{/popup}}

    if (map._loaded) {
        run();
    } else {
        map.on("load", run);
    }
});
