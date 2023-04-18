import os
import glob
import shutil
import subprocess
import sys
import logging

logger = logging.getLogger(__name__)


def generate_qrc(directory, qrc_file_path):
    logger.info(f"Generating qrc file: {qrc_file_path}")
    with open(qrc_file_path, "w") as qrc_file:
        qrc_file.write("<!DOCTYPE RCC><RCC version=\"1.0\">\n")
        qrc_file.write("\t<qresource>\n")

        for filepath in glob.glob(os.path.join(directory, "**/*")):
            if os.path.isfile(filepath):
                relative_filepath = os.path.relpath(filepath, directory)
                logger.debug(f"Adding file: {filepath} as: {relative_filepath}")
                qrc_file.write(f"\t\t<file>{relative_filepath}</file>\n")

        qrc_file.write("\t</qresource>\n")
        qrc_file.write("</RCC>\n")


def compile_qrc(qrc_file, resource_file):
    compiler = shutil.which("pyside2-rcc")
    if not compiler:
        raise RuntimeError("Unable to find pyside2-rcc")

    subprocess.check_call([compiler, "-o", resource_file, qrc_file])


def build_resource(directory, rc_file):
    qrc = os.path.join(directory, "resources.qrc")
    generate_qrc(directory, qrc)
    compile_qrc(qrc, rc_file)
    os.remove(qrc)
