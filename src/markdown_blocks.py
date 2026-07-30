from enum import Enum

from textnode import TextNode, TextType, text_node_to_html_node
from inline_markdown import text_to_textnodes
from parentnode import ParentNode


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    QUOTE = "quote"
    CODE = "code"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

def block_to_block_type(markdown_block):
    lines = markdown_block.split("\n")
    # HEADING
    if markdown_block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    # CODE
    if len(lines) > 1 and lines[0].startswith("```",) and lines[-1].startswith("```"):
        return BlockType.CODE
    # QUOTE
    if markdown_block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    #UNORDERED_LIST
    if markdown_block.startswith("-"):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    # ORDERED_LIST
    if markdown_block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.ORDERED_LIST
    # DEFAULT
    return BlockType.PARAGRAPH

def text_to_children(text):
    text_nodes = text_to_textnodes(text)  # you already have this!
    children = []
    for text_node in text_nodes:
        children.append(text_node_to_html_node(text_node))  # and this!
    return children

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.HEADING:
                level = len(block) - len(block.lstrip("#"))
                text = block.lstrip("# ")
                node = ParentNode(f"h{level}", text_to_children(text))
            case BlockType.PARAGRAPH:
                node = ParentNode("p", text_to_children(block))
            case BlockType.QUOTE:
                text = "\n".join(line.lstrip("> ") for line in block.split("\n"))
                node = ParentNode("blockquote", text_to_children(text))
            case BlockType.UNORDERED_LIST:
                items = [ParentNode("li", text_to_children(line.lstrip("- "))) for line in block.split("\n")]
                node = ParentNode("ul", items)
            case BlockType.ORDERED_LIST:
                items = [ParentNode("li", text_to_children(line.split(". ", 1)[1])) for line in block.split("\n")]
                node = ParentNode("ol", items)
            case BlockType.CODE:
                # special case: no inline markdown parsing!
                text = block.strip("`").strip()
                text_node = TextNode(text, TextType.CODE)
                node = ParentNode("pre", [text_node_to_html_node(text_node)])
        children.append(node)
    return ParentNode("div", children)
    return None