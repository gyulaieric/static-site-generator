import shutil
import os

def main():
    if os.path.exists("public"):
        shutil.rmtree("public")

    copy_contents("static", "public")

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

if __name__ == "__main__":
    main()