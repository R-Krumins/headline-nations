import os, sys, shutil, subprocess

def copy(file):
    if os.path.isfile(file):
        print(f"[{file}] already exists in working directory.")
        return
    srcFile = SECRET_FILES_PATH+"/"+file
    assert os.path.isfile(srcFile), "could not find "+srcFile
    shutil.copyfile(srcFile, file)
    print(f"Copied [{file}] to working directory.")

def executeIfYes(file):
    a = input().strip()
    if a == "y" or a == "yes":
        subprocess.run(["python3", file])

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

#execute procedures if user agrees
print("\nWould you like to test config files and enviroment setup? (y/n)")
executeIfYes("tests/test_config.py")

print("\nWould you like execute DB migation?(y/n)")
executeIfYes("migrate_db.py")





    