import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a test node", "bold")
        node2 = TextNode("This is a test node", "bold")
        self.assertEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("omg wow", "italic", "https://google.com")
        node2 = TextNode("omg wow", "italic", "https://google.com")
        self.assertEqual(node, node2)
    
    def test_eq_false(self):
        node = TextNode("test node", "bold", "youtube.com")
        node2 = TextNode("test node", "italic", "youtube.com")
        self.assertNotEqual(node, node2)
    
    def test_eq_false2(self):
        node = TextNode("test node 1", "code")
        node2 = TextNode("test node 2", "code")
        self.assertNotEqual(node, node2)
    
    def test_repr(self):
        node = TextNode("testing node", "text", "https://google.com")
        self.assertEqual("TextNode(testing node, text, https://google.com)", repr(node))

if __name__ == "__main__":
    unittest.main()