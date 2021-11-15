from setuptools import setup, find_packages

long_description = ""

setup(
    name = "keentune-bench",
    version = "1.0.0",
    description = "KeenTune bench unit",
    long_description = long_description,
    url = "https://codeup.openanolis.cn/codeup/keentune/keentune_bench",
    license = "MulanPSLv2",
    classifiers = [
        "Environment:: KeenTune",
        "IntendedAudience :: Information Technology",
        "IntendedAudience :: System Administrators",
        "License :: OSI Approved :: MulanPSLv2",
        "Operating System :: POSIX :: Linux",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.6",
        "ProgrammingLanguage :: Python"
    ],

    packages = find_packages(),
    package_data={'bench': ['bench.conf']},
    
    data_files = [
        ("/etc/keentune/",["LICENSE"]),
        ("/etc/keentune/conf", ["bench/bench.conf"]),
    ],
)
