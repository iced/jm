import json

import jm

class GeoJSON(object):
    def __init__(self, geojson):
        self.uuid = jm._uuid()
        self.data = json.dumps({
            "type": "geojson",
            "data": geojson
        })
