
def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    return_blocks = []
    for block in blocks:
        if block.strip():
            return_blocks.append(block.strip())

    return return_blocks