## Package comparison  

#### Application:

From the public REST API, located at ```https://rdb.altlinux.org/api/```.  
From the method ```/export/branch_binary_packages/{branch}```.  
The following are used as branches sisyphus and p10.  

I receive binary packages and distribute them according to arch_value and three conditions:  

1) all packages that are in p10 but not in sisyphus;
2) all packages that are in sisyphus but are not in p10;
3) all packages with a higher version_release in sisyphus than in p10.

#### See the result of the execution in the new created directories  

here is the tree structure of the created directories !!!!  

#### Requirements:  

1. Python;  
2. Pip;  
3. Requests;  
4. Argparse.  

#### Minimum requirements:  

1. Python;  
2. Pip.  

#### Install:  

1. Clone the project;
2. Go to the root directory of the project;
3. Perform the installation with the command ```pip3 install -r requirements.txt```;
4. Run the application with the command ```python3 comparison_binary_packages/main.py sisyphus p10```.
