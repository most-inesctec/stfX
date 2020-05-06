import argparse
import os
import requests
from os.path import isfile, join
from termcolor import colored
import json


def parse_args():
    """Parse the command line arguments"""
    ap = argparse.ArgumentParser(
        description='Script to valida the stfX tool.')

    ap.add_argument('-d', '--dir', type=str,
                    required=True, help='The directory containing the resources necessary for this test.\
                        The output is also written to this directory, in file result.txt')
    ap.add_argument('-e', '--endpoint', type=str,
                    default='http://localhost:0080/stfx', help='The endpoint running stfX. Default is http://localhost:0080/stfx')

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


def load_dataset(dir: str, endpoint: str) -> str:
    """Load the dataset to the stfX server"""
    with open("%s/dataset.json" % dir, "r") as dataset_file:
        dataset = json.load(dataset_file)
        response = requests.post(endpoint + "/storyboard", json=dataset)
        if response.status_code != 200:
            raise Exception(
                colored("POST /storyboard %i" % response.status_code, "red"))
        else:
            return response.json()


def get_events_of_interest(dir: str, endpoint: str, id: str) -> str:
    """Get the events of interest from the stfX server"""
    with open("%s/thresholds.json" % dir, "r") as thresholds_file:
        thresholds = json.load(thresholds_file)
        response = requests.post("%s/storyboard/%s" % (endpoint, id),
                                 json=thresholds)
        if response.status_code != 200:
            raise Exception(
                colored("POST /storyboard/%s %i" % (id, response.status_code), "red"))
        else:
            events = response.json()
            # Removing representations
            for event in events:
                del event["phenomena"]
            return events


def test(dir: str, endpoint: str):
    """Pipeline of validatin the test using the files present in dir"""
    dataset_id = load_dataset(dir, endpoint)
    events = get_events_of_interest(dir, endpoint, dataset_id)
    # TODO -> Compare obtained with the expected result
    return None


def main():
    """Main function"""
    args = parse_args()

    if verify_dir(args.dir):
        result = test(args.dir, args.endpoint)
        save_result(result, args.dir)


if __name__ == '__main__':
    main()
