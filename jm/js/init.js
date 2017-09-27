window.__jm_maps = {};

require.config({
  paths: {
      "mapboxgl": "https://api.mapbox.com/mapbox-gl-js/v{{version}}/mapbox-gl"
  }
});

requirejs(["mapboxgl"], function(mapboxgl) {
    mapboxgl.accessToken = "{{access_token}}";
});
