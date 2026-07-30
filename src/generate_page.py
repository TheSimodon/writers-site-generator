import os

from extract import read_file, extract_title, write_file
from markdown_blocks import markdown_to_html_node


def generate_page(from_path: str, template_path: str, dest_path: str):
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')
    markdown_content = read_file(from_path)
    template_content = read_file(template_path)

    content_html = markdown_to_html_node(markdown_content).to_html()

    title = extract_title(markdown_content)
    print("TITLE: ", repr(title))
    print("CONTENT:", repr(content_html))
    final_html = template_content.replace("{{ Title }}", title).replace("{{ Content }}", content_html)

    dest_dir = os.path.dirname(dest_path)
    if dest_path != "":
        os.makedirs(dest_dir, exist_ok=True)

    write_file(dest_path, final_html)
