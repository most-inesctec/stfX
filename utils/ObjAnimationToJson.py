import argparse
import os
import re
import json


def parse_args():
    """Parse the command line arguments"""
    ap = argparse.ArgumentParser(
        description='Script to convert a directory containing .obj files, describing an animation, to json.')

    ap.add_argument('-i', '--input_dir', type=str,
                    required=True, help='The input file containing the SPTDataLab output')
    ap.add_argument('-o', '--output_dir', type=str,
                    default='./', help='Output directory for the datasets. Default is current directory.')
    ap.add_argument('-of', '--output_file', type=str,
                    default='out', help='Output file name')

    return ap.parse_args()


def create_dir(dir_name: str):
    """Creates a directory wth the given name if it does not exist"""
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)


def save(dataset: dict, out_file: str, out_dir: str):
    """Save the content to the given json file in the given dir"""
    with open("%s/%s.json" % (out_dir, out_file), "w+") as fd:
        fd.write(json.dumps(dataset))


def parse_obj(in_dir: str, obj_file: str):
    """Parse and .obj file into a json type object"""
    polygon = []

    with open("%s/%s" % (in_dir, obj_file), "r") as fd:
        for line in fd.readlines():
            if (line[:2] == "v "):
                _, *line_contents = line.split(" ")
                polygon.append([
                    float(line_contents[0]),
                    float(line_contents[1])
                ])

    return polygon


def converter(in_dir: str) -> dict:
    """Convert the .obj files in the directory to a dataset object"""
    obj_files = [f for f in os.listdir(in_dir)
                 if os.path.splitext(f)[1] == ".obj"]
    obj_files.sort()
    dataset = []

    for obj in obj_files:
        dataset.append(parse_obj(in_dir, obj))

    return {'dataset': dataset}


def main():
    """Main function"""
    args = parse_args()

    create_dir(args.output_dir)
    dataset = converter(args.input_dir)
    save(dataset,
         args.output_file,
         args.output_dir,)


if __name__ == '__main__':
    main()
