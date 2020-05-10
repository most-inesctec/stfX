import unittest

"""
https://www.mathopenref.com/coordpolygonarea.html
https://pypi.org/project/PyGLM/
https://towardsdatascience.com/the-concave-hull-c649795c0f0f
https://en.wikipedia.org/wiki/Alpha_shape
"""

X_COORDINATE = 0
Y_COORDINATE = 1


def surveyor_formula(polygon: list) -> float:
    """Find the area of the given polygon using the surveyor formula"""
    # Check if first and last points of polygon are equal
    parsed_poly = polygon[0:-1]\
        if polygon[0] == polygon[len(polygon)-1]\
        else polygon
    area = 0

    for i in range(-1, len(parsed_poly)-1):
        area += parsed_poly[i][X_COORDINATE] * parsed_poly[i+1][Y_COORDINATE] -\
            parsed_poly[i][Y_COORDINATE] * parsed_poly[i+1][X_COORDINATE]

    return abs(area / 2)


def extract_transformations(events: list) -> list:
    """Extract the transformations from the json object 'events'"""
    return [e["type"] for e in events]


def apply_m1(results: list, expected_results: list) -> float:
    """Apply the metric M2 and obtain its result, between 0 and 100"""
    return None


class TestM1(unittest.TestCase):

    def test_area(self):
        square = [
            [1, 1],
            [1, -1],
            [-1, -1],
            [-1, 1]
        ]
        self.assertEqual(surveyor_formula(square), 4)

        square_with_repeated_vertice = [
            [1, 1],
            [1, -1],
            [-1, -1],
            [-1, 1],
            [1, 1]
        ]
        self.assertEqual(surveyor_formula(square_with_repeated_vertice), 4)

    # def test_equal(self):
    #     results = [{
    #         "events": [
    #             {"type": "TRANSLATION"},
    #             {"type": "ROTATION"},
    #             {"type": "SCALE"}
    #         ],
    #         "temporalRange": [0, 100]
    #     }, {
    #         "events": [
    #             {"type": "TRANSLATION"}
    #         ],
    #         "temporalRange": [100, 120]
    #     }, {
    #         "events": [
    #             {"type": "ROTATION"},
    #             {"type": "SCALE"}
    #         ],
    #         "temporalRange": [120, 150]
    #     }]
    #     expected_results = [{
    #         "events": [
    #             {"type": "TRANSLATION"},
    #             {"type": "ROTATION"}
    #         ],
    #         "temporalRange": [0, 120]
    #     }, {
    #         "events": [
    #             {"type": "ROTATION"},
    #             {"type": "SCALE"}
    #         ],
    #         "temporalRange": [120, 150]
    #     }]

    #     self.assertEqual(apply_m1(results, expected_results), 100)

    # def test_different(Self):

    #     self.assertEqual(apply_m1(), 50)


if __name__ == '__main__':
    unittest.main()
