"""
Icon Generation API
That API is used by the litepipe-icon command line tool to generate icons from a spec file
"""

import os
import sys
import qtawesome
import yaml
import logging

from PySide2 import QtGui, QtCore

logger = logging.getLogger(__name__)


def icon_from_spec(icon_spec):
    """
    Generate a qtawesome icon from a spec

    Args:
        icon_spec (dict): The icon spec to use

    A spec is a dict with the following keys:
    - size: The size of the icon, can be an int or a list of 2 ints
    - layers: A list of dicts with the following keys:

    A layer dict has the following keys:
    - icon: The name of the icon to use
    - color: The color of the icon, can be a list of 3 ints or a string
    - scale_factor: The scale factor of the icon, defaults to 1.0

    """
    assert isinstance(icon_spec, dict), f"Icon spec must be a dict got: {icon_spec}"

    icons = []
    options = []

    assert "layers" in icon_spec, f"Icon spec must have a 'layers' key got: {icon_spec}"
    assert isinstance(icon_spec["layers"], list), f"Icon spec 'layers' must be a list"

    for layer in icon_spec["layers"]:
        if isinstance(layer, str):
            icons.append(layer)
            options.append({})
        else:
            assert isinstance(layer, dict), f"Icon spec 'layers' must be dicts"
            assert "icon" in layer, f"Icon spec 'layers' must have a 'icon' key got: {layer}"

            icons.append(layer["icon"])

            color = layer.get("color", "black")

            if isinstance(color, list):
                color = QtGui.QColor(*color)

            options.append({"color": color, "scale_factor": layer.get("scale_factor", 1.0)})

    return qtawesome.icon(*icons, options=options)


def size_from_spec(spec, default_size):
    """
    Extract a QSize object from the given spec, defaulting to the given default_size

    Args:
        spec (dict): The spec to extract the size from
        default_size (QtCore.QSize): The default size to use if no size is specified in the spec
    """
    if "size" in spec:
        size = spec["size"]
        if isinstance(size, int):
            size = QtCore.QSize(size, size)
        elif isinstance(size, list):
            assert len(size) == 2, f"Icon spec 'size' must be a list of 2 ints got: {size}"
            size = QtCore.QSize(*size)
        else:
            assert False, f"Icon spec 'size' must be an int or list of 2 ints got: {size}"
    else:
        size = default_size

    return size


def generate_icons(spec_file, output_dir):
    """
    Generate icons from the given spec file
    Args:
        spec_file (str): The path to the icon spec file
        output_dir (str): The directory to write the icons to
        default_size (QtCore.QSize): The default size to use if no size is specified in the spec
    """
    with open(spec_file) as f:
        data = yaml.safe_load(f)

    assert "icons" in data, f"Icon spec must have a 'icons' key got: {data}"
    assert isinstance(data["icons"], dict), f"Icon spec 'icons' must be a dict"

    default_size = data.get("default_size", 256)

    logger.info(f"generating icons for: {spec_file} @ size: {default_size}")

    if isinstance(default_size, int):
        default_size = QtCore.QSize(default_size, default_size)
    elif isinstance(default_size, list):
        assert len(default_size) == 2, f"Icon spec 'default_size' must be a list of 2 ints got: {default_size}"
        default_size = QtCore.QSize(*default_size)

    icon_specs = data["icons"]

    for filename, spec in icon_specs.items():
        logger.debug(f"generating icon: {filename}")
        icon = icon_from_spec(spec)
        size = size_from_spec(spec, default_size)
        pixmap = icon.pixmap(size)
        full_path = os.path.join(output_dir, filename)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        pixmap.save(full_path)
