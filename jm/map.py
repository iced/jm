import uuid
import os.path

import jm

class Map(object):
    def __init__(self, style="mapbox://styles/mapbox/streets-v10", width="auto", height=650, zoom=None, center=None, bearing=None, pitch=None):
        self.uuid = jm._uuid()
        if center is not None:
            center = {"value": center}
        self.map = jm._run_js("map_init", {"uuid": self.uuid, "style": style, "width": width, "height": height, "zoom": zoom, "center": center, "bearing": bearing, "pitch": pitch}, show=False)
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

    def __run_js(self, js, bindings={}):
        r = jm._run_js(js, bindings, show=self.shown)
        if not self.shown:
            self.operations.append(r)

    def remove(self):
        self.__run_js("map_remove", {"uuid": self.uuid})

    def add_source(self, source):
        if not source.uuid in self.sources:
            self.__run_js("map_add_source", {"uuid": self.uuid, "source_uuid": source.uuid, "data": source.data})
            self.sources.append(source.uuid)

    def add_layer(self, layer):
        self.add_source(layer.source)
        if not layer.uuid in self.layers:
            self.__run_js("map_add_layer", {"uuid": self.uuid, "layer_uuid": layer.uuid, "source_uuid": layer.source.uuid, "kind": layer.kind, "paint": layer.paint, "popup": layer.popup})
            self.layers.append(layer.uuid)

    def fit_source(self, source, padding=20, animate=0):
        self.__run_js("map_fit_source", {"uuid": self.uuid, "source_uuid": source.uuid, "padding": padding, "animate": animate})

    def set_camera(self, center=None, zoom=None, bearing=None, pitch=None, animate=0):
        if center is not None:
            center = {"value": center}
        self.__run_js("map_set_camera", {"uuid": self.uuid, "center": center, "zoom": zoom, "bearing": bearing, "pitch": pitch, "animate": animate})

    def set_ceneter(self, center, animate=0):
        self.set_camera(center=center, animate=animate)

    def set_zoom(self, zoom, animate=0):
        self.set_camera(zoom=zoom, animate=animate)

    def set_bearing(self, bearing, animate=0):
        self.set_camera(bearing=bearing, animate=animate)

    def set_pitch(self, pitch, animate=0):
        self.set_camera(pitch=pitch, animate=animate)

    def __del__(self):
        self.remove()
