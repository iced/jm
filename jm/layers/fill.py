import json

import jm

class Fill(object):
    def __init__(self, source, popup=None):
        self.uuid = jm._uuid()
        self.source = source
        self.popup = popup
        self.kind = "fill"
        self.paint = json.dumps({
            "fill-color": {
                "type": "identity",
                "property": "fill-color"
            },
            "fill-outline-color": {
                "type": "identity",
                "property": "fill-outline-color"
            },
            "fill-opacity": {
                "type": "identity",
                "property": "fill-opacity"
            }
        })
