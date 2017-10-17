element.append("<div id=\"{{uuid}}\" style=\"width: {{width}}; height: {{height}}px; overflow: visible;\"></div>");

requirejs(["mapboxgl"], function(mapboxgl) {
    var map = new mapboxgl.Map({
        container: "{{uuid}}",
        style: "{{style}}",
        {{#zoom}}
        zoom: {{zoom}},
        {{/zoom}}
        {{#center}}
        center: {{center.value}},
        {{/center}}
        {{#bearing}}
        bearing: {{bearing}},
        {{/bearing}}
        {{#pitch}}
        pitch: {{pitch}},
        {{/pitch}}
    });

    window.__jm_maps["{{uuid}}"] = map;
});
