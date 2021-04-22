import argparse

from . import launcher


def getup():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--dataset", type=str, help="Variable name of instance class DTS"
    )
    args = parser.parse_args()
    dataset = args.dataset or ""
    launcher.getup(dataset)
