import sys
import logging
import argparse

from kirk.version import __version__, __version_info__


def main():
    parser = argparse.ArgumentParser(
        prog="kirk",
        description="captain of the enterprise",
        version="0.1.0"
    )
    print("hello world!")
