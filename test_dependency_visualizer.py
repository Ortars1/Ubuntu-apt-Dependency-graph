import unittest
from dependency_visualizer import get_package_dependencies, build_dependency_graph, save_graph
import os

class TestDependencyVisualizer(unittest.TestCase):

    def test_get_package_dependencies(self):
        dependencies = get_package_dependencies('bash')
        self.assertIsInstance(dependencies, list)
        self.assertGreater(len(dependencies), 0)

    def test_build_dependency_graph(self):
        graph = build_dependency_graph('bash')
        self.assertTrue(graph.has_node('bash'))
        dependencies = get_package_dependencies('bash')
        for dep in dependencies:
            self.assertTrue(graph.has_node(dep))

    def test_save_graph(self):
        graph = build_dependency_graph('bash')
        output_path = 'test_output.png'
        save_graph(graph, output_path)
        self.assertTrue(os.path.isfile(output_path))
        os.remove(output_path)

if __name__ == '__main__':
    unittest.main()
