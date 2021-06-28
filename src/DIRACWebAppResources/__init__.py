import importlib.resources
import sys
from pathlib import Path


def extension_metadata():
    return {
        "priority": -100,
        "web_resources": {
            "static": [Path(sys.prefix) / "share" / "dirac" / "DIRACWebAppResources" / "static"],
        }
    }
