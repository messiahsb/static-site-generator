import os
import shutil

def main():
    get_files_from('static', "public")
def get_files_from(src, dest):
    # check if both src and dest exist
    if not os.path.exists(src):
        raise Exception("src directory not found")
    if not os.path.exists(dest):
        os.mkdir(dest)

    # delet all contents of destination directory
    shutil.rmtree(dest)
    os.mkdir(dest)

    # copy files sub directories and nested files
    move_files(src, dest)

def move_files(src, dest):
    # loop through files and directories of src to copy into public
    for idx in os.listdir(src):
        src_path = os.path.join(src, idx)
        dest_path = os.path.join(dest, idx)
        if os.path.isfile(src_path):
            print(f"copying file {src_path} to {dest_path}")
            shutil.copy(src_path, dest)
        if os.path.isdir(src_path):
            print(f"copying directory {src_path} to {dest_path}")
            os.mkdir(dest_path)
            move_files(src_path, dest_path)
        # log path of each file copies
    
    return os.path.exists(src)
main()
