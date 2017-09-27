import uuid
import os.path

import jm

class Map(object):
    def __init__(self, style="mapbox://styles/mapbox/streets-v10", zoom=None, center=None):
        self.uuid = jm._uuid()
        self.map = jm._run_js("map_init", {"uuid": self.uuid, "style": style, "zoom": zoom, "center": center}, show=False)
        self.sources = []
        self.sources_uuids = []
        self.layers = []
        self.layers_uuids = []

    def _repr_javascript_(self, **kwargs):
        js_map = self.map._repr_javascript_(**kwargs)
        js_sources = "".join(map(lambda s: s._repr_javascript_(**kwargs), self.sources))
        js_layers = "".join(map(lambda s: s._repr_javascript_(**kwargs), self.layers))
        return js_map + js_sources + js_layers

    def add_source(self, source):
        if not source.uuid in self.sources_uuids:
            self.sources.append(jm._run_js("map_add_source", {"uuid": self.uuid, "source_uuid": source.uuid, "data": source.data}, show=False))
            self.sources_uuids.append(source.uuid)

    def add_layer(self, layer):
        self.add_source(layer.source)
        if not layer.uuid in self.layers_uuids:
            self.layers.append(jm._run_js("map_add_layer", {"uuid": self.uuid, "layer_uuid": layer.uuid, "source_uuid": layer.source.uuid, "kind": layer.kind, "paint": layer.paint}, show=False))
            self.layers_uuids.append(layer.uuid)
