import os
from extract import read_file, extract_title, write_file
from markdown_blocks import markdown_to_html_node


def generate_page(from_path, template_path, dest_path, basepath):
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')
    markdown_content = read_file(from_path)
    template_content = read_file(template_path)

    content_html = markdown_to_html_node(markdown_content).to_html()

    title = extract_title(markdown_content)

    print("TITLE: ", repr(title))
    print("CONTENT:", repr(content_html))

    final_html = (
        template_content
                  .replace("{{ Title }}", title)
                  .replace("{{ Content }}", content_html)
                  .replace('href="/', f'href="{basepath}')
                  .replace('src="/', f'src="{basepath}')
    )

    dest_dir = os.path.dirname(dest_path)
    if dest_dir != "":
        os.makedirs(dest_dir, exist_ok=True)

    write_file(dest_path, final_html)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for entry in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, entry)
        dest_path = os.path.join(dest_dir_path, entry)

        if os.path.isfile(from_path):
            if from_path.endswith(".md"):
                dest_path = dest_path.replace(".md", ".html")
                generate_page(from_path, template_path, dest_path, basepath)
        else:
            generate_pages_recursive(from_path, template_path, dest_path, basepath)

