import argparse
import os
from os.path import isdir, join
from tqdm import tqdm
from termcolor import colored
from validate import validate


def parse_args():
    """Parse the command line arguments"""
    ap = argparse.ArgumentParser(
        description='Script to validate all the test-scenario, in the given directory, using the stfX tool.')

    ap.add_argument('-d', '--dir', type=str,
                    required=True, help='The directory containing the test-scenarios.')
    ap.add_argument('-o', '--out_dir', type=str,
                    default='results', help='The directory where the output of the test-scenario will be written to.\
                        If the directory does not exist, it is created. Defaults to \'./results\'')
    ap.add_argument('-e', '--endpoint', type=str,
                    default='http://localhost:0080/stfx', help='The endpoint running stfX. Default is http://localhost:0080/stfx')

    return ap.parse_args()


def get_test_scenarios(dir: str) -> list:
    """Identify the test scenarios, in the given dir, by their dir name"""
    return [f for f in os.listdir(dir)
            if isdir(join(dir, f)) and f[-5:] == "_test"]


def create_dir(dir: str):
    """Create the given directory if it does not exist"""
    if not isdir(dir):
        os.mkdir(dir)


def run_test_scenario(scenario_dir: str, output: str, endpoint: str):
    """Run the test scenario identified and store the results"""
    validate(scenario_dir, endpoint)

    scenario_name = scenario_dir.split("/")[1]
    os.rename(join(scenario_dir, "result.json"),
              join(output, "%s.json" % scenario_name))
    os.rename(join(scenario_dir, "m1.png"),
              join(output, "%s_m1.png" % scenario_name))


def main():
    """Main function"""
    args = parse_args()

    scenarios = get_test_scenarios(args.dir)
    create_dir(args.out_dir)

    for scenario in tqdm(scenarios):
        print(colored("::: %s :::" % scenario, "blue"))
        run_test_scenario(join(args.dir, scenario),
                          args.out_dir,
                          args.endpoint)


if __name__ == '__main__':
    main()
