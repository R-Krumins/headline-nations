import os, sys, shutil, subprocess

def copy(file):
    if os.path.isfile(file):
        print(f"[{file}] already exists in working directory.")
        return
    srcFile = SECRET_FILES_PATH+"/"+file
    assert os.path.isfile(srcFile), "could not find "+srcFile
    shutil.copyfile(srcFile, file)
    print(f"Copied [{file}] to working directory.")

try:
    SECRET_FILES_PATH = sys.argv[1]
except:
    print("Error: Path to secrets is not given as an argument!")
    exit()


#copy files from secrets folder
print("Copying secrets...")
copy("config.ini")
copy("log-config.yaml")
print("DONE!")

#test config and enviroment setup if user agrees
print("\nWould you like to test config files and enviroment setup? (y/n)")
a = input().strip()
if a == "y" or a == "yes":
    subprocess.run(["python3", "tests/test_config.py"])




    