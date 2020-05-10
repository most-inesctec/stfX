import unittest

"""
https://www.mathopenref.com/coordpolygonarea.html
https://pypi.org/project/PyGLM/
https://towardsdatascience.com/the-concave-hull-c649795c0f0f
https://en.wikipedia.org/wiki/Alpha_shape
"""

X_COORDINATE = 0
Y_COORDINATE = 1


def area(x, y):
    n = len(x)
    s = 0.0
    for i in range(-1, n-1):
        s += x[i]*y[i+1] - y[i]*x[i+1]
    return 0.5*s


# def surveyor_formula(polygon: list) -> float:
#     return area([el[0] for el in polygon], [el[1] for el in polygon])


def surveyor_formula(polygon: list) -> float:
    """Find the area of the given polygon using the surveyor formula"""
    area = 0

    for i in range(-1, len(polygon)-1):
        area += polygon[i][X_COORDINATE] * polygon[i+1][Y_COORDINATE] -\
            polygon[i][Y_COORDINATE] * polygon[i+1][X_COORDINATE]

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
            [-1, 1],
            # [0, 0],
            # [0, 2],
            # [2, 2],
            # [2, 0]
        ]
        self.assertEqual(surveyor_formula(square), 4)

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
