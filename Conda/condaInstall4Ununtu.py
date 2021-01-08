apt install nodejs git
wget -P /tmp /https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh
bash Anaconda3-2020.02-Linux-x86_64.sh
conda create -n pc37 python=3.7 schrodinger::pymol-bundle=2.4.1 conda-forge::cctbx-base conda-forge::jupyter
conda activate pc37
conda install conda-forge::jupyterlab=2.2.0
# The following may be needed
# jupyter serverextension enable --py jupyterlab --user 
pip install jupyterlab-snippets-multimenus
jupyter lab build
# Might be needed
# jupyter lab clean
jupyter --path # select the top option under Data for storing the libraries
cd ~/.local/share/jupyter # change as per output from prior line
mkdir multimenus_snippets
cd multimenus_snippets
git clone https://github.com/MooersLab/juptyerlabpymolcctbx.git cctbx
git clone https://github.com/MooersLab/juptyerlabpymolcctbxplus.git cctbx+
git clone https://github.com/MooersLab/juptyerlabpymolpysnips.git pymol
git clone https://github.com/MooersLab/juptyerlabpymolpysnipsplus.git pymol+
jupyter lab # or libtbx.python -m jupyter-lab
$0
# Description:  Enter this snippet on the command line in an empty directory.
# Source:  NA

apt install nodejs git
wget -P /tmp /https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh
bash Anaconda3-2020.02-Linux-x86_64.sh
conda create -n pc37 python=3.7 schrodinger::pymol-bundle=2.4.1 conda-forge::cctbx-base conda-forge::jupyter
conda activate pc37
conda install conda-forge::jupyterlab=2.2.0
# The following may be needed
# jupyter serverextension enable --py jupyterlab --user 
pip install jupyterlab-snippets-multimenus
jupyter lab build
# Might be needed
# jupyter lab clean
jupyter --path # select the top option under Data for storing the libraries
cd ~/.local/share/jupyter # change as per output from prior line
mkdir multimenus_snippets
cd multimenus_snippets
git clone https://github.com/MooersLab/juptyerlabpymolcctbx.git cctbx
git clone https://github.com/MooersLab/juptyerlabpymolcctbxplus.git cctbx+
git clone https://github.com/MooersLab/juptyerlabpymolpysnips.git pymol
git clone https://github.com/MooersLab/juptyerlabpymolpysnipsplus.git pymol+
jupyter lab # or libtbx.python -m jupyter-lab

# Description:  Enter this snippet on the command line in an empty directory.
# Source:  NA

