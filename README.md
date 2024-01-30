## Package comparison  

#### Application:

From the public REST API, located at ```https://rdb.altlinux.org/api/```.  
From the method ```/export/branch_binary_packages/{branch}```.  
The following are used as branches sisyphus and p10.  

I receive binary packages and distribute them according to arch_value and three conditions:  

1) all packages that are in p10 but not in sisyphus;
2) all packages that are in sisyphus but are not in p10;
3) all packages with a higher version_release in sisyphus than in p10.

#### Result  

![the result of the execution](https://github.com/zitaker/package-comparison/assets/92075508/3051b7e0-b2a7-4921-baa1-6ff7ff344444)  

A structure is being created.  

```
tests/
└── fixtures
    ├── aarch64
    │   ├── p10_aarch64.json
    │   ├── result_conditions
    │   │   ├── greater_version_release_sisyphus.json
    │   │   ├── packages_p10_not_in_sisyphus.json
    │   │   └── packages_sisyphus_not_in_p10.json
    │   └── sisyphus_aarch64.json
    ├── armh
    │   ├── p10_armh.json
    │   ├── result_conditions
    │   │   ├── greater_version_release_sisyphus.json
    │   │   ├── packages_p10_not_in_sisyphus.json
    │   │   └── packages_sisyphus_not_in_p10.json
    │   └── sisyphus_armh.json
    ├── i586
    │   ├── p10_i586.json
    │   ├── result_conditions
    │   │   ├── greater_version_release_sisyphus.json
    │   │   ├── packages_p10_not_in_sisyphus.json
    │   │   └── packages_sisyphus_not_in_p10.json
    │   └── sisyphus_i586.json
    ├── noarch
    │   ├── p10_noarch.json
    │   ├── result_conditions
    │   │   ├── greater_version_release_sisyphus.json
    │   │   ├── packages_p10_not_in_sisyphus.json
    │   │   └── packages_sisyphus_not_in_p10.json
    │   └── sisyphus_noarch.json
    ├── p10.json
    ├── ppc64le
    │   ├── p10_ppc64le.json
    │   ├── result_conditions
    │   │   ├── greater_version_release_sisyphus.json
    │   │   ├── packages_p10_not_in_sisyphus.json
    │   │   └── packages_sisyphus_not_in_p10.json
    │   └── sisyphus_ppc64le.json
    ├── sisyphus.json
    ├── x86_64
    │   ├── p10_x86_64.json
    │   ├── result_conditions
    │   │   ├── greater_version_release_sisyphus.json
    │   │   ├── packages_p10_not_in_sisyphus.json
    │   │   └── packages_sisyphus_not_in_p10.json
    │   └── sisyphus_x86_64.json
    └── x86_64-i586
        ├── p10_x86_64-i586.json
        ├── result_conditions
        │   ├── greater_version_release_sisyphus.json
        │   ├── packages_p10_not_in_sisyphus.json
        │   └── packages_sisyphus_not_in_p10.json
        └── sisyphus_x86_64-i586.json

```

#### Requirements:  

1. python;  
2. pip;  
3. requests;  
4. argparse;
5. rpm;
6. make (not a mandatory requirement).  

#### Minimum requirements:  

1. python;  
2. pip.  

#### Install:  

1. clone the project;
2. go to the root directory of the project;
3. perform the installation with the command ```pip3 install -r requirements.txt``` or ```make install```;
4. run the application with the command ```python3 comparison_binary_packages/main.py sisyphus p10``` or ```make loading```.
