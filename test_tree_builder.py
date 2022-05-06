import unittest
import json
from tree_builder import to_tree


class TestTreeBuilder(unittest.TestCase):
    def test_tree_builder_should_raise_exception_when_root_node_does_not_exist(self):
        source = [('a', 'a1'), ('a', 'a2')]
        with self.assertRaises(TypeError):
            to_tree(source)

    def test_tree_builder_should_return_expected_json_string_when_root_node_exists(self):
        source = [
            (None, 'a'),
            (None, 'b'),
            (None, 'c'),
            ('a', 'a1'),
            ('a', 'a2'),
            ('a2', 'a21'),
            ('a2', 'a22'),
            ('b', 'b1'),
            ('b1', 'b11'),
            ('b11', 'b111'),
            ('b', 'b2'),
            ('c', 'c1')
        ]
        expected = json.dumps(
            {
                'a': {'a1': {}, 'a2': {'a21': {}, 'a22': {}}},
                'b': {'b1': {'b11': {'b111': {}}}, 'b2': {}},
                'c': {'c1': {}}
            },
            indent=4,
            sort_keys=True
        )
        self.assertEqual(to_tree(source), expected)

    def test_tree_builder_should_return_expected_json_string_when_duplicated_tuples_exist(self):
        source = [
            (None, 'a'),
            (None, 'b'),
            ('a', 'a1'),
            ('a', 'a1'),
            ('b', 'b1')
        ]
        expected = json.dumps(
            {
                'a': {'a1': {}},
                'b': {'b1': {}}
            },
            indent=4,
            sort_keys=True
        )
        self.assertEqual(to_tree(source), expected)


if __name__ == '__main__':
    unittest.main()
