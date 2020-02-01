# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 23:38:33 2018

@author: SilverDoe
"""

'''
conda --version
python --version
pip --version

conda info # detailed info
conda info pkgname # package and dependencies info
conda update anaconda
conda update -n base conda
conda install python=3.42 # replace current python version
conda install packagename 
or 
conda install --name envname packagename
conda install -c conda-forge packagename # install a package that is not on the channel list

# installing packages that are not available in conda
conda install -c conda-forge  nameofpackage

conda update python # update python to the latest version
conda update packagename 
conda update --all
conda remove
conda list
conda search




'''
============== Adding new env =================

conda create --name nameofenv python=3.4


============== Activate an env ================

conda activate nameofenv


============== Deactivate an env ==============

conda deactivate

============== List available envs ============

conda env list

============= Remove environment ==============

conda remove --name deeplearning --all


============= Export environment file =========

conda env export > environment.yml


============= Import an environment ===========

conda env create -f environment.yml


============= Export all packages in environment ==========

conda list -e > requirements.txt



============ Create an environment using requirements.txt =========

conda create --name nameofenv --file requirements.txt


========== Install packages from requirements.txt =================

conda install --yes --file requirements.txt  # all....if fails then the whole setup fails

or 


while read requirement; do conda install --yes $requirement; done < requirements.txt 2>error.log


=========== pip generate requirements.txt =========================

pip freeze > requirements.txt


========== pip install packages listed in requirements.txt ========

pip install -r requirements.txt



































