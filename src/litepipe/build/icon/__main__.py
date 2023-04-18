import argparse
import os
import sys

from litepipe.icon import api

from PySide2 import QtCore, QtGui, QtWidgets


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--spec", help="The icon file to use", default="./icon_spec.yml")
    parser.add_argument("--dir", help="The output file to write", default=".")
    args = parser.parse_args()

    app = QtWidgets.QApplication()
    if not os.path.exists(args.spec):
        print(f"Icon spec file does not exist: {args.spec}", file=sys.stderr)
        sys.exit(1)

    output_dir = os.path.abspath(args.dir)
    if not os.path.exists(args.dir):
        os.makedirs(args.dir)

    api.generate_icons(args.spec, output_dir)
