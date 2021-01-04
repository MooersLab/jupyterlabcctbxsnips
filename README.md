# jupyterlabcctbxsnips


## Installation of pymol, cctbx, and jupyter 

The installation of both CCTBX, PyMOL, and Jupyter can accomplished by one of several approaches.
All three packages are complex and are best kept isolated in a dedicated environment.
Configuration files and paths to prior installations  can still trip up new installations. 
Edits of the bashrc or zshrc startup files may be required.
On Mac OS X, I had to hide my ```/usr/local/include``` directory.
Another difficulty is the dependence of JupyterLab extensions on newer versions of Node.js.
The version installed from Anaconda can be quite old.
If the interpretable error messages have been addressed and there is still trouble, try another approach.
Once a setup is working, do not to tinker with it by adding new extensions or upgrading the packages.
All too often dependency conflicts will emerge.
Treat the setup as a house of cards!


### Pymol and cctbx share a Python interpreter from Anaconda

The first approach is outlined in the code listing below.
It creates one Anaconda environment for using both PyMOL and CCTBX.
This approach allows using the default Python3 kernel in Jupyter and eliminates the need to switch between kernels in one notebook.
The protocol worked on a new instance on Ubuntu 20.04, but it failed on a well-worn instance of MacOS 10.15.7
(conda create -n pc38 schrodinger::pymol conda-forge::cctbx-base schrodinger::tk conda-forge::nodejs conda-forge::jupyter conda-forge::jupyterlab)
After updating the existing software and installing Node.js and git, a software subdirectory is created for temporary storage of the the snippet libraries.
The libraries are downloaded into with the `git clone` command.
Next, the appropriate Anaconda installation script is downloaded and moved to the home directory where it is run to set up and install Anaconda3.
Next, one conda command with a long argument list is run to install pymol, cctbx, jupyter, and python3.7 while creating a Anaconda environment named `pc37`.
The environment name is shorthand for pymol-cctbx-python3.7.
The shorthand name reduces the typing required when using this environment.

```bash
apt install nodejs git
git clone https://github.com/MooersLab/pymolcctbx.git
wget -P /tmp /https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh
bash Anaconda3-2020.02-Linux-x86_64.sh
conda create -n pc37 python=3.7 schrodinger::pymol-bundle conda-forge::cctbx-base conda-forge::jupyter
conda activate pc37
conda install jupyterlab
pip install jupyterlab-snippets-multimenus
jupyter lab build 
jupyter --path # select the top option under Data for storing the libraries
cd ~.local/share/jupyter # change as per output from prior line
mkdir multimenus_snippets
cd multimenus_snippets
git clone https://github.com/MooersLab/juptyerlabpymolcctbx.git cctbx
git clone https://github.com/MooersLab/juptyerlabpymolcctbxplus.git cctbx+
git clone https://github.com/MooersLab/juptyerlabpymolpysnips.git pymol
git clone https://github.com/MooersLab/juptyerlabpymolpysnipsplus.git pymol+
jupyter lab # or libtbx.python -m jupyter-lab
```

This new environment is activated, and JupyterLab is installed with the conda command.
The pip command is then used to install the extension jupyterlab-snippets-multimenus from PyPi.
The activation of this extension requires that JupyterLab is rebuilt.
The `jupyter --path` command returns a list of paths that vary between operating systems.
The top path listed under Data is where the snippet libraries are stored.
Next, the `multimenus\_snippets` subfolder is move to this final location.

The final command launches JupyterLab in the default webbrowser.
No error messages should appear in the terminal.
The menu bar should contain the items `CCTBX` and `PyMOL` as in figure one.
The bash alias command `alias pcJL='conda activate pc37 \&\& juptyer lab'` can reduce subsequent typing.
If there are errors messages about PyMOL upon launching JuptyerLab, then try either of the next two protocols.
The broken environment can be removed with the command `conda env remove --name pc37`.
The first protocol has the upside using one kernel to call cctbx and pymol and the downside of possible  disruptions by updates to either PyMOL or CCTBX.


### Pymol and cctbx with separate Python interpreters from Anaconda


The second protocol creates a new conda environment for CCTBX but not PyMOL.
The upside of this approach is that updates to one program will not break the other program.
Separate kernels are created for CCTBX and for the PyMOL.app installed in the standard location.
This approach will necessitate not calling pymol and cctbx in the same cell and switching kernels when calling each program.
Objects may have to passed between programs by writing them to files from one program and then reading these files with the other program.
Name the new environment `cctbx37` to track the Python version used to create the environment. 
Next, create a kernel named cctbx37 via the command `ipython kernel install --name cctbx37 --user`.
With PyMOL installed in the usual location via its installer, open PyMOL and install Jupyter inside it with the command `conda install -c conda-forge jupyter -y` entered at the PyMOL prompt.
The install can be slow.
Next, create a kernel named `pymol2.4.1` by entering in the terminal the following command that contains the path to the Ipython executable inside of the PyMOL.app: `/Applications/PyMOL.app/Contents/bin/ipython kernel install --name pymol37 --user`.
Download and move the snippet libraries into place as above.


