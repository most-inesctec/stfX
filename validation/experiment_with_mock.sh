#!/bin/sh
. venv/bin/activate

# Mock non multiple sequence test
echo "$(tput setaf 4)::: mocked_bad_non_multiple_sequence_test :::$(tput setaf 7)"
python validate.py -d experiments/bad_non_multiple_sequence_test -e http://localhost:8080
mv experiments/bad_non_multiple_sequence_test/m1.png results/mocked_bad_non_multiple_sequence_test_m1.png
mv experiments/bad_non_multiple_sequence_test/result.json results/mocked_bad_non_multiple_sequence_test.json

# Mock single multiple
# T1
echo "$(tput setaf 4)::: mocked_awful_single_multiple_transformations_test :::$(tput setaf 7)"
python validate.py -d experiments/awful_single_multiple_transformations_test -e http://localhost:8080
mv experiments/awful_single_multiple_transformations_test/m1.png results/mocked_awful_single_multiple_transformantions_test_m1.png
mv experiments/awful_single_multiple_transformations_test/result.json results/mocked_awful_single_multiple_transformations_test.json
# T2
echo "$(tput setaf 4)::: mocked_bad_single_multiple_transformations_test :::$(tput setaf 7)"
python validate.py -d experiments/bad_single_multiple_transformations_test -e http://localhost:8080
mv experiments/bad_single_multiple_transformations_test/m1.png results/mocked_bad_single_multiple_transformantions_test_m1.png
mv experiments/bad_single_multiple_transformations_test/result.json results/mocked_bad_single_multiple_transformations_test.json
# T3
echo "$(tput setaf 4)::: mocked_single_multiple_transformations_test :::$(tput setaf 7)"
python validate.py -d experiments/single_multiple_transformations_test -e http://localhost:8080
mv experiments/single_multiple_transformations_test/m1.png results/mocked_single_multiple_transformantions_test_m1.png
mv experiments/single_multiple_transformations_test/result.json results/mocked_single_multiple_transformations_test.json

# Mock multiple complex
echo "$(tput setaf 4)::: mocked_multiple_transformantions_test :::$(tput setaf 7)"
python validate.py -d experiments/multiple_transformantions_test -e http://localhost:8080
mv experiments/multiple_transformantions_test/m1.png results/mocked_multiple_transformantions_test.png
mv experiments/multiple_transformantions_test/result.json results/mocked_multiple_transformantions_test.json