#!/bin/sh
. venv/bin/activate
# First mock
echo "$(tput setaf 4)::: mocked_bad_non_multiple_sequence_test :::"
python validate.py -d experiments/bad_non_multiple_sequence_test -e http://localhost:8080
mv experiments/bad_non_multiple_sequence_test/m1.png results/mocked_bad_non_multiple_sequence_test_m1.png
mv experiments/bad_non_multiple_sequence_test/result.json results/mocked_bad_non_multiple_sequence_test.json
# Second mock
echo "$(tput setaf 4)::: mocked_awful_single_multiple_transformations_test :::"
python validate.py -d experiments/awful_single_multiple_transformations_test -e http://localhost:8080
mv experiments/awful_single_multiple_transformations_test/m1.png results/mocked_awful_single_multiple_transformantions_test_m1.png
mv experiments/awful_single_multiple_transformations_test/result.json results/mocked_awful_single_multiple_transformations_test.json
# Third mock
echo "$(tput setaf 4)::: mocked_bad_single_multiple_transformations_test :::"
python validate.py -d experiments/bad_single_multiple_transformations_test -e http://localhost:8080
mv experiments/bad_single_multiple_transformations_test/m1.png results/mocked_bad_single_multiple_transformantions_test_m1.png
mv experiments/bad_single_multiple_transformations_test/result.json results/mocked_bad_single_multiple_transformations_test.json