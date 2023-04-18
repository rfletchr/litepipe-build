import os
import sys


def setup_subparser(subparsers):
    """setup the subparser for the icon command"""
    parser = subparsers.add_parser(
        "dir-to-rc",
        help="convert a directory of files into an importable PySide2 resource file",
    )

    parser.add_argument(
        "dir",
        help="the directory to convert into a resource file",
    )
    parser.add_argument(
        "file",
        help="the path for the generated resource file",
    )
    parser.set_defaults(func=execute)


def execute(args):
    from litepipe.build.resources import api

    if not os.path.isdir(args.dir):
        print(f"Directory does not exist: {args.dir}", file=sys.stderr)
        sys.exit(1)

    directory = os.path.abspath(args.dir)
    api.build_resource(directory, args.file)
