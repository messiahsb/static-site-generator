import os
import shutil

def main():
    get_files_from('src', "public")
def get_files_from(src, dest):
    # check if both src and dest exist
    if not os.path.exists(src):
        raise Exception("src directory not found")
    if not os.path.exists(dest):
        raise Exception("dest directory not found")

    # delet all contents of destination directory
    shutil.rmtree(dest)
    os.mkdir(dest)

    # copy files sub directories and nested files
    move_files(src, dest)

def move_files(src, dest):
    # loop through files and directories of src to copy into public
    for idx in os.listdir(src):
        print(idx)
        if os.path.isfile(idx):
            shutil.copy(idx, dest)
        if os.path.isdir(idx):
            new_path = os.path.join(dest, idx) 
            os.mkdir(new_path)
            move_files(idx, new_path)
        # log path of each file copies
    
    return os.path.exists(src)
main()
