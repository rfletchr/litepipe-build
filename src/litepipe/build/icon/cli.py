def setup_subparser(subparsers):
    """setup the subparser for the icon command"""
    parser = subparsers.add_parser(
        "icons",
        help="build the icons defined in an icon spec file",
    )

    parser.add_argument(
        "--spec",
        help="The icon spec file to use",
        default="./icon_spec.yml",
    )
    parser.add_argument(
        "--dir",
        help="The output directory to write icons into",
        default=".",
    )
    parser.set_defaults(func=execute)


def execute(args):
    from PySide2 import QtWidgets
    from litepipe.build.icon import api
    app = QtWidgets.QApplication()
    api.generate_icons(args.spec, args.dir)
