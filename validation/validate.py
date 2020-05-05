import argparse
import os
import requests
from os.path import isfile, join
from termcolor import colored


def parse_args():
    """Parse the command line arguments"""
    ap = argparse.ArgumentParser(
        description='Script to valida the stfX tool.')

    ap.add_argument('-d', '--dir', type=str,
                    required=True, help='The directory containing the resources necessary for this test.\
                        The output is also written to this directory, in file result.txt')

    return ap.parse_args()


def save_result(result: str, out_dir: str):
    """Save the content to the given json file in the given dir"""
    with open("%s/result.txt" % out_dir, "w+") as fd:
        fd.write(result)


def verify_dir(dir: str) -> bool:
    """Verify if the given directory has the resources required for testing"""
    resources = [f for f in os.listdir(dir)
                 if isfile(join(dir, f))]
    # Verifying necessary resources
    if "dataset.json" not in resources:
        print(colored("Missing test dataset (dataset.json).", "red"))
        return False

    if "thresholds.json" not in resources:
        print(colored("Missing test thresholds (thresholds.json).", "red"))
        return False

    if "expected_result.json" not in resources:
        print(colored("Missing expected result (expected_result.json).", "red"))
        return False

    return True


def test(dir: str):
    # TODO
    return None


def main():
    """Main function"""
    args = parse_args()

    if verify_dir(args.dir):
        result = test(args.dir)
        save_result(result, args.dir)


if __name__ == '__main__':
    main()
