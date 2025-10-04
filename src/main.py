import shutil
import os
import sys

from markdown_to_html import markdown_to_html_node

def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    print(basepath)

    if os.path.exists("docs"):
        shutil.rmtree("docs")

    copy_contents("static", "docs")

    generate_pages_recursive("content", "template.html", "docs", basepath)

def copy_contents(src, dest):
    if os.path.exists(src):
        items = os.listdir(src)
        if not os.path.exists(dest):
            os.mkdir(dest)
        for item in items:
            if os.path.isdir(f"{src}/{item}"):
                os.mkdir(f"{dest}/{item}")
                copy_contents(f"{src}/{item}", f"{dest}/{item}")
            else:
                print(f"Copying {src}/{item} to {dest}")
                shutil.copy(f"{src}/{item}", dest)

def extract_title(markdown):
    for line in markdown.split("\n"):
        if line[:2] == '# ':
            return line[1:].strip()
    raise Exception("No h1 header in markdown")

def generate_page(src, template_path, dest, basepath):
    print(f"Generating page from {src} to {dest} using {template_path}")

    source_file = open(src, "r")
    markdown = source_file.read()
    source_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace('src="/', f'src="{basepath}')

    destination = open(dest, "w")
    destination.write(template)
    destination.close()

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for entry in os.listdir(dir_path_content):
        if os.path.isdir(os.path.join(dir_path_content, entry)):
            dest = os.path.join(dest_dir_path, entry)
            os.mkdir(dest)
            generate_pages_recursive(os.path.join(dir_path_content, entry), template_path, dest, basepath)
        else:
            generate_page(os.path.join(dir_path_content, entry), template_path, os.path.join(dest_dir_path, "index.html"), basepath)


if __name__ == "__main__":
    main()