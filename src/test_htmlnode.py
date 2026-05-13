import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
            node = HTMLNode(
                "div",
                "Hello, world!",
                None,
                {"class": "greeting", "href": "https://boot.dev"},
            )
            self.assertEqual(
                node.props_to_html(),
                ' class="greeting" href="https://boot.dev"',
            )
    
    def test_values(self):
        node = HTMLNode(
                "div",
                "I wish I could read",
            )
        self.assertEqual(
                node.tag,
                "div",
            )
        self.assertEqual(
                node.value,
                "I wish I could read",
            )
        self.assertEqual(
                node.children,
                None,
            )
        self.assertEqual(
                node.props,
                None,
            )
            
    def test_eq(self):
        test_dict = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        
        node2 = HTMLNode('<p>', "hello world", None, test_dict)
        node = HTMLNode('<p>', "hello world", node2, test_dict)

        # self.assertEqual(node, node2)
        test_string = (' href="https://www.google.com" target="_blank"')
        self.assertEqual(test_string, node2.props_to_html())
        wrong_string = ('href="https://www.google.com" target="_blank"')
        self.assertNotEqual(wrong_string, node.props_to_html())

        wrong = ["href", "https://www.google.com", "target", "_blank",]
        node3 = HTMLNode('<p>', "hello world", node, test_dict)
        
        wrong_string = ('href="https://www.google.com" target="_blank"')
        self.assertNotEqual(wrong, node3.props_to_html())

        # test_string = (f'Tag: {node.tag}, Value: {node.value}, children = {node.children}, \n Props: {node.props}')

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(Tag: p, Value: What a strange world, children: None, Props: {'class': 'primary'})",
        )
    def test_leafto_html(self):
        node = LeafNode('p', "this is some text")
        self.assertEqual("<p>this is some text</p>",
            node.to_html())
        
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual('<a href="https://www.google.com">Click me!</a>',
            node2.to_html())

    def test_leafvalues(self):
        node = LeafNode(
                "div",
                "I wish I could read",
            )
        self.assertEqual(
                node.tag,
                "div",
            )
        self.assertEqual(
                node.value,
                "I wish I could read",
            )
        self.assertEqual(
                node.props,
                None,
            )

    def test_leafrepr(self):
         node = LeafNode(
             "p",
             "What a strange world",
             {"class": "primary"},
         )
         self.assertEqual(
             node.__repr__(),
             "LeafNode(Tag: p, Value: What a strange world, Props: {'class': 'primary'})",
         )           
    def test_leaf_to_html_no_tag(self):
             node = LeafNode(None, "Hello, world!")
             self.assertEqual(node.to_html(), "Hello, world!")      




    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
    
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )  
    def test_to_html_with_many_children(self):
            node = LeafNode("div", "I wish I could read")
            node_with_prop = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
            child_node = LeafNode("span", "child")
            parent_node = ParentNode("div", [child_node, node, node_with_prop])
            self.assertEqual(parent_node.to_html(), '<div><span>child</span><div>I wish I could read</div><a href="https://www.google.com">Click me!</a></div>')
        
    def test_to_html_with_many_grandchildren(self):
            node = LeafNode("div","node",)
            greatgrandchild = ParentNode("div", [node])
            grandchild_node = ParentNode("a", [greatgrandchild], {"href": "https://www.google.com"})
            child_node = ParentNode("span", [grandchild_node])
            parent_node = ParentNode("div", [child_node])
            self.assertEqual(
                parent_node.to_html(),
                '<div><span><a href="https://www.google.com"><div><div>node</div></div></a></span></div>',
            )

    def test_to_html_with_many_grandchildrens(self):
        grandchild_2 = LeafNode("b", "second grandchild")
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node, grandchild_2])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b><b>second grandchild</b></span></div>",
        )  
        
    def test_to_html_with_many_great_grandchildren(self):
            node = LeafNode("div","node",)
            greatgrandchild = LeafNode("div", "greatgrandchild")
            grandchild_node = ParentNode("a", [greatgrandchild, node], {"href": "https://www.google.com"})
            child_node = ParentNode("span", [grandchild_node])
            parent_node = ParentNode("div", [child_node])
            self.assertEqual(
                parent_node.to_html(),
                '<div><span><a href="https://www.google.com"><div>greatgrandchild</div><div>node</div></a></span></div>',
            )
if __name__ == "__main__":
    unittest.main()