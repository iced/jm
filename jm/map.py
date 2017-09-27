import uuid
import os.path

import jm

class Map(object):
    def __init__(self, style="mapbox://styles/mapbox/streets-v10", width="auto", height=650, zoom=None, center=None):
        self.uuid = jm._uuid()
        self.map = jm._run_js("map_init", {"uuid": self.uuid, "style": style, "width": width, "height": height, "zoom": zoom, "center": {"value": center}}, show=False)
        self.shown = False
        self.operations = []
        self.sources = []
        self.layers = []

    def _repr_javascript_(self, **kwargs):
        if self.shown:
            return None
        js_map = self.map._repr_javascript_(**kwargs)
        js_operations = "\n".join(map(lambda s: s._repr_javascript_(**kwargs), self.operations))
        self.shown = True
        self.operations = []
        return js_map + "\n" + js_operations

    def add_source(self, source):
        if not source.uuid in self.sources:
            r = jm._run_js("map_add_source", {"uuid": self.uuid, "source_uuid": source.uuid, "data": source.data}, show=self.shown)
            if not self.shown:
                self.operations.append(r)
            self.sources.append(source.uuid)

    def add_layer(self, layer):
        self.add_source(layer.source)
        if not layer.uuid in self.layers:
            r = jm._run_js("map_add_layer", {"uuid": self.uuid, "layer_uuid": layer.uuid, "source_uuid": layer.source.uuid, "kind": layer.kind, "paint": layer.paint, "popup": layer.popup}, show=self.shown)
            if not self.shown:
                self.operations.append(r)
            self.layers.append(layer.uuid)
