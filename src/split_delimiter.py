from htmlnode import LeafNode, ParentNode
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    closing_delimiters = ["`", '_', '**',]
    for node in old_nodes:

        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        # if delimiter not in closing_delimiters:
        #     raise

        delim_count = 0
        delim_count = node.text.count(delimiter)
        if delim_count % 2 != 0:
            raise Exception("missing delimiter, invalid markdown syntax") 
        
        split_text = node.text.split(delimiter)

        nodes = []
        for i in range(len(split_text)):
            if split_text[i] == "":
                continue
            if i%2 == 1:
                nodes.append(TextNode(split_text[i], text_type))
            else:
                nodes.append(TextNode(split_text[i], TextType.TEXT))
        
        new_nodes.extend(nodes)

    return new_nodes
        
     