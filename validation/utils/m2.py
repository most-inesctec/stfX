import unittest

NUMBER_POSSIBLE_TRANSFORMATIONS = 5


def find_splits(array1: list, array2: list) -> list:
    """Find the split points of the given array of events"""
    keys = set()
    for event in array1:
        keys.add(event["temporalRange"][0])
        keys.add(event["temporalRange"][1])
    for event in array2:
        keys.add(event["temporalRange"][0])
        keys.add(event["temporalRange"][1])

    return list(sorted(keys))


def subdivide(events: list, splits: list) -> list:
    """Split the given events to match the keys in the splits list"""
    return []


def apply_m2(results: list, expected_results: list) -> float:
    """Apply the metric M2 and obtain its result, between 0 and 100"""
    splits = find_splits(results, expected_results)
    print(find_splits(results, expected_results))
    formatted_results = subdivide(results, splits)\
        if len(results) < len(splits)\
        else results
    formatted_expected = subdivide(expected_results, splits)\
        if len(expected_results) < len(splits)\
        else expected_results

    return 0


class TestM2(unittest.TestCase):

    def test_m2(self):
        results = [{
            "events": [
                {"type": "TRANSLATION"},
                {"type": "ROTATION"},
                {"type": "SCALE"}
            ],
            "temporalRange": [0, 100]
        }, {
            "events": [
                {"type": "TRANSLATION"}
            ],
            "temporalRange": [100, 120]
        }, {
            "events": [
                {"type": "ROTATION"},
                {"type": "SCALE"}
            ],
            "temporalRange": [120, 150]
        }]
        expected_results = [{
            "events": [
                {"type": "TRANSLATION"},
                {"type": "ROTATION"}
            ],
            "temporalRange": [0, 120]
        }, {
            "events": [
                {"type": "ROTATION"},
                {"type": "SCALE"}
            ],
            "temporalRange": [120, 150]
        }]

        self.assertEqual(apply_m2(results, expected_results), 84)


if __name__ == '__main__':
    unittest.main()
