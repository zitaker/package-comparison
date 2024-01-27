## Package comparison  

#### Application:

From the public REST API, located at ```https://rdb.altlinux.org/api/```.  
From the method ```/export/branch_binary_packages/{branch}```.  
The following are used as branches sisyphus and p10.  

I receive binary packages and distribute them according to arch_value and three conditions:  

1) all packages that are in p10 but not in sisyphus;
2) all packages that are in sisyphus but are not in p10;
3) all packages with a higher version_release in sisyphus than in p10.

#### See the result  

![the result of the execution](https://github.com/zitaker/package-comparison/assets/92075508/3051b7e0-b2a7-4921-baa1-6ff7ff344444)  

#### Requirements:  

1. python;  
2. pip;  
3. requests;  
4. argparse;
5. make (not a mandatory requirement).  

#### Minimum requirements:  

1. python;  
2. pip.  

#### Install:  

1. clone the project;
2. go to the root directory of the project;
3. perform the installation with the command ```pip3 install -r requirements.txt``` or ```make install```;
4. run the application with the command ```python3 comparison_binary_packages/main.py sisyphus p10``` or ```make loading```.
