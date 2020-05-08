import unittest

NUMBER_MAX_TRANSFORMATIONS = 5
TO_PERCENT = 100


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
    formatted_events = []

    for i in range(len(splits)-1):
        formatted_event = {}
        formatted_event["temporalRange"] = [splits[i], splits[i + 1]]
        # Get the events of the enclosing event (it must always be one)
        for event in events:
            tr = event["temporalRange"]
            if tr[0] <= splits[i] and tr[1] >= splits[i+1]:
                formatted_event["events"] = event["events"]
        # Adding the formatted event to the return result
        formatted_events.append(formatted_event)

    return formatted_events


def extract_transformations(events: list) -> list:
    """Extract the transformations from the json object 'events'"""
    return [e["type"] for e in events]


def apply_m2(results: list, expected_results: list) -> float:
    """Apply the metric M2 and obtain its result, between 0 and 100"""
    splits = find_splits(results, expected_results)

    formatted_results = subdivide(results, splits)\
        if len(results) < len(splits) - 1\
        else results
    formatted_expected = subdivide(expected_results, splits)\
        if len(expected_results) < len(splits) - 1\
        else expected_results

    # Computing the weighted average distance
    w_avg_distance = 0
    for e1, e2 in zip(formatted_results, formatted_expected):
        t_range = e1["temporalRange"]
        A = set(extract_transformations(e1["events"]))
        B = set(extract_transformations(e2["events"]))
        w_avg_distance += (len(A-B) + len(B-A)) * (t_range[1] - t_range[0])
    w_avg_distance /= splits[len(splits)-1] - splits[0]

    # Diving by worst-case scenario an return as percent
    return (1 - (w_avg_distance / NUMBER_MAX_TRANSFORMATIONS)) * TO_PERCENT


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
