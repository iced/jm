import pkg_resources
import uuid
import os.path
import IPython.display as ipd
import pystache

from jm.map import Map
import jm.sources
import jm.layers

def _run_js(js, bindings={}, show=True, debug=False):
    js_fname = pkg_resources.resource_filename("jm", os.path.join("js", "{0}.js".format(js)))
    with open(js_fname, "r") as f:
        content = f.read()
    content = pystache.render(content, bindings)
    if debug:
        print(content)
    content = ipd.Javascript(content)
    if show:
        display(content)
        return
    return content

def _uuid():
    return str(uuid.uuid4()).replace("-", "")

def init(acces_token, version="0.40.1"):
    _run_js("init", {"access_token": acces_token, "version": version})
    display(ipd.HTML("<link href=\"https://api.tiles.mapbox.com/mapbox-gl-js/v{0}/mapbox-gl.css\" rel=\"stylesheet\" />".format(version)))

def gj(geojson, layer=jm.layers.Fill, popup=None, padding=0):
    m = jm.Map()
    s = jm.sources.GeoJSON(geojson)
    m.add_layer(layer(s, popup=popup))
    m.fit_source(s, padding=padding)
    display(m)
    return m
