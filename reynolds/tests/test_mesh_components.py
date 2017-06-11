from reynolds.blockmesh.mesh_components import Vertex3, Block, SimpleGrading, BoundaryRegion, Face
from unittest import TestCase


class TestMeshComponents(TestCase):
    def test_vertices(self):
        v = Vertex3(0, 0, 0)
        self.assertEqual('(0, 0, 0)', v.dict_string())

    def test_simple_grading(self):
        sg = SimpleGrading([1, 1, 1])
        self.assertEqual("simpleGrading (1 1 1)", sg.dict_string())

    def test_block(self):
        sg = SimpleGrading([1, 1, 1])
        b = Block(range(8), [20, 20, 1], sg)
        self.assertEqual("hex (0 1 2 3 4 5 6 7) (20 20 1) simpleGrading (1 1 1)", b.dict_string())

    def test_face(self):
        f = Face([0, 4, 7, 3])
        self.assertEqual("(0 4 7 3)", f.dict_string())

    def test_boundary_region(self):
        f1 = Face([0, 4, 7, 3])
        f2 = Face([2, 6, 5, 1])
        f3 = Face([1, 5, 4, 0])
        br = BoundaryRegion("fixedWalls", "wall", [f1, f2, f3])
        face_comps = ['\t\t' + f.dict_string() for f in [f1, f2, f3]]
        br_string_comps = ["fixedWalls", '{', '\ttype wall;', '\tfaces', '\t('] + face_comps + ['\t);', '}']
        br_string = '\n'.join(s for s in br_string_comps)
        print('Expected Region:\n\n' + br_string)
        self.assertEqual(br_string, br.dict_string())


