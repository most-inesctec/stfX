#!/bin/sh
. venv/bin/activate
# First mock
echo "$(tput setaf 4)::: mocked_non_multiple_sequence_test :::"
python validate.py -d experiments/non_multiple_sequence_test -e http://localhost:8080
mv experiments/non_multiple_sequence_test/m1.png results/mocked_non_multiple_sequence_test_m1.png
mv experiments/non_multiple_sequence_test/result.json results/mocked_non_multiple_sequence_test.json
# Second mock
echo "$(tput setaf 4)::: mocked_single_multiple_transformations_test :::"
python validate.py -d experiments/single_multiple_transformations_test -e http://localhost:8080
mv experiments/single_multiple_transformations_test/m1.png results/mocked_single_multiple_transformations_test_m1.png
mv experiments/single_multiple_transformations_test/result.json results/mocked_single_multiple_transformations_test.json