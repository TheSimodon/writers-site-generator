import os.path
import shutil
import sys

from generate_page import generate_page, generate_pages_recursive
from copystatic import copy_files_recursive

dir_path_static = "./static"
dir_path_public = "./docs"

basepath = sys.argv[1] if len(sys.argv) > 1 else "/"

def main() -> None:
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory")
    copy_files_recursive(dir_path_static, dir_path_public)

    generate_pages_recursive("content", "template.html", "public", basepath)

if __name__ == "__main__":
    main()
