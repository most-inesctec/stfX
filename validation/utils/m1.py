import unittest
from shapely import geometry, affinity

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


def polygon_to_vertices_list(polygon: geometry.Polygon) -> list:
    """Extract the polygon vertices as a list"""
    return list(polygon.exterior.coords)


def apply_transformations(initial_representation: list, events: list) -> float:
    """Apply the transformations in the events list to the initial representation"""
    scale = 1
    rot_angle = 0
    trans_vector = [0, 0]

    for item in events:
        for event in item["events"]:
            if event["type"] == "TRANSLATION":
                trans_vector[X_COORDINATE] += event["trigger"]["transformation"][X_COORDINATE]
                trans_vector[Y_COORDINATE] += event["trigger"]["transformation"][Y_COORDINATE]

            elif event["type"] == "ROTATION":
                rot_angle += event["trigger"]["transformation"]

            elif event["type"] == "UNIFORM_SCALE":
                scale *= event["trigger"]["transformation"]

    # Apply multiplication
    polygon = geometry.Polygon(initial_representation)
    s_polygon = affinity.scale(polygon, xfact=scale, yfact=scale)
    r_s_polygon = affinity.rotate(s_polygon, rot_angle)
    t_r_s_polygon = affinity.translate(r_s_polygon,
                                       xoff=trans_vector[0],
                                       yoff=trans_vector[1])
    return polygon_to_vertices_list(t_r_s_polygon)


def apply_m1(real_representation: list, perceived_representation: list) -> float:
    """Apply the metric M1 and obtain its result, between 0 and 1"""
    joint_point_set = real_representation + perceived_representation
    convex_hull = geometry.MultiPoint(joint_point_set).convex_hull
    return surveyor_formula(real_representation) / surveyor_formula(polygon_to_vertices_list(convex_hull))


class TestM1(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestM1, self).__init__(*args, **kwargs)

        self.representation = [
            [1, 1],
            [1, -1],
            [-1, -1],
            [-1, 1],
            [1, 1]
        ]
        self.transformations = [{
            "events": [
                {"type": "TRANSLATION", "trigger": {"transformation": [5, 5]}},
                {"type": "ROTATION", "trigger": {"transformation": 180}},
                {"type": "UNIFORM_SCALE", "trigger": {"transformation": 1.25}}
            ]
        }, {
            "events": [
                {"type": "TRANSLATION", "trigger": {"transformation": [5, 0]}},
                {"type": "ROTATION", "trigger": {"transformation": -90}},
                {"type": "UNIFORM_SCALE", "trigger": {"transformation": 1.6}}
            ]
        }]

    def test_area(self):
        square = [
            [1, 1],
            [1, -1],
            [-1, -1],
            [-1, 1]
        ]
        self.assertEqual(surveyor_formula(square), 4)
        self.assertEqual(surveyor_formula(self.representation), 4)

    def test_transformations(self):
        self.assertEqual(apply_transformations(self.representation, self.transformations), [
            (8.0, 7.0),
            (12.0, 7.0),
            (12.0, 3.0),
            (8.0, 3.0),
            (8.0, 7.0),
        ])

    def test_M1(self):
        self.assertEqual(apply_m1(self.representation, self.representation), 1)
        self.assertTrue(apply_m1(self.representation,
                                 apply_transformations(self.representation, self.transformations))
                        < 0.1)


if __name__ == '__main__':
    unittest.main()
