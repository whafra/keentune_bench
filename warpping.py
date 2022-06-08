import re  
import os  
def warppingCheck():
    with open("keentune-bench.spec",'r') as f:
        spec = f.read()
        version_in_spec = re.search("Version:        ([\d.]+)\n",spec).group(1)
        release_in_spec = re.search("define anolis_release (\d)\n",spec).group(1)
        
        if re.search(" - {}-{}".format(version_in_spec, release_in_spec), spec):
            print("[OK] check changelog in spec")
        else:
            print("[Failed] changelog missing in keentune-bench.spec, {}-{}".format(
                version_in_spec, release_in_spec))
            return

    print("Start wrap up of keentune-bench-{}-{}".format(version_in_spec, release_in_spec))
    return version_in_spec, release_in_spec

if __name__ == "__main__":
    version_in_spec, _ = warppingCheck()
    os.system("tar -cvzf keentuned-bench-{}.tar.gz bench keentune-bench.service LICENSE README.md requirements.txt setup.py".format(version_in_spec))