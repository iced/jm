import json

import jm

class Line(object):
    def __init__(self, source, popup=None):
        self.uuid = jm._uuid()
        self.source = source
        self.popup = popup
        self.kind = "line"
        self.paint = json.dumps({
            "line-color": {
                "type": "identity",
                "property": "line-color",
                "default": "#FF0000"
            },
            "line-opacity": {
                "type": "identity",
                "property": "line-opacity",
                "default": 1
            },
            "line-width": {
                "type": "identity",
                "property": "line-width",
                "default": 1
            }
        })
