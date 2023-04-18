import argparse
import litepipe.build.icon.cli
import litepipe.build.resources.cli
import logging

modules = [
    litepipe.build.icon.cli,
    litepipe.build.resources.cli,
]


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(required=True, dest="command", help="the sub-command to run")
    parser.set_defaults(func=lambda _: parser.print_help())
    parser.add_argument("-v", "--verbose", action="store_true", help="enable verbose output")

    for module in modules:
        module.setup_subparser(subparsers)

    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO, format="%(message)s")

    args.func(args)
