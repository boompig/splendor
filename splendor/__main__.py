import logging
import os
from argparse import ArgumentParser

import coloredlogs

from . import search

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("filename", nargs="?")
    parser.add_argument(
        "-t", "--threshold", type=int, default=12, help="Points threshold for search"
    )
    parser.add_argument(
        "-d",
        "--output-dir",
        default=os.path.join(os.getcwd(), "state_data"),
        help="Output directory",
    )
    parser.add_argument("-v", "--verbose", default=False, action="store_true")
    args = parser.parse_args()

    log_level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(level=log_level)
    coloredlogs.install(level=log_level)

    if not os.path.exists(args.output_dir):
        logging.debug("Created output directory %s", args.output_dir)
        os.makedirs(args.output_dir)

    search.POINT_THRESHOLD = args.threshold

    search.search(output_dir=args.output_dir, fname=args.filename)
