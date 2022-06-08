import re  
import os 

def warppingCheck():
    with open("keentune-bench.spec",'r') as f:
        spec = f.read()
        version_in_spec = re.search("Version:        ([\d.]+)\n",spec).group(1)
        release_in_spec = re.search("define anolis_release (\d)\n",spec).group(1)
        print("Get version: {}-{}".format(version_in_spec, release_in_spec))

        if re.search(" - {}-{}".format(version_in_spec, release_in_spec), spec):
            print("[OK] check the version of changelog at keentune-bench.spec.")
        else:
            print("[Failed] wrong version number in changelog at keentune-bench.spec.")
            return

    with open("setup.py", 'r') as f:
        script = f.read()
        if re.search('version     = "{}",'.format(version_in_spec),script):
            print("[OK] check the version of setup.py.")
        else:
            print("[Failed] wrong version number in setup.py.")
            return

    print("Start wrap up of keentune-bench-{}-{}".format(version_in_spec, release_in_spec))
    return version_in_spec, release_in_spec

if __name__ == "__main__":
    version_in_spec, _ = warppingCheck()
    if os.path.exists("keentune-bench-{}".format(version_in_spec)):
        os.system("rm -rf keentune-bench-{}".format(version_in_spec))
    
    os.system("mkdir keentune-bench-{}".format(version_in_spec))
    os.system("cp -r bench keentune-bench-{}".format(version_in_spec))
    os.system("cp keentune-bench.service keentune-bench-{}".format(version_in_spec))
    os.system("cp LICENSE keentune-bench-{}".format(version_in_spec))
    os.system("cp README.md keentune-bench-{}".format(version_in_spec))
    os.system("cp requirements.txt keentune-bench-{}".format(version_in_spec))
    os.system("cp setup.py keentune-bench-{}".format(version_in_spec))
    os.system("tar -cvzf keentune-bench-{}.tar.gz --exclude=**/__pycache__ keentune-bench-{}".format(version_in_spec, version_in_spec))