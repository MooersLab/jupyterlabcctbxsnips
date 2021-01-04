# jupyterlabcctbxsnips


## Installation of pymol, cctbx, and jupyter 

The installation of both CCTBX, PyMOL, and Jupyter can accomplished by one of several approaches.
All three packages are complex and best kept isolated in a dedicated environment.
Configuration files and paths to prior installations can still trip up new installations. 
Edits of the bashrc or zshrc startup files may be required.
On Mac OS X, I had to hide my `/usr/local/include` directory by `sudo mv /usr/local/include /usr/local/oldInclude`.
The extensions to JupyterLab depend on Node.js. 
An error message from conda about needing to install node and npm can be misleasding when both programs are aleady installed. 
Running the command to enable the serverextension solves this problem.
The `jupyterlab-snippets-multimenus` is not compatable with JuptyerLab 3.0.0 so an old version has to be installed.

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
conda install jupyterlab=2.2.0
jupyter serverextension enable --py jupyterlab --user
pip install jupyterlab-snippets-multimenus
jupyter lab build 
juptyer lab clean
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
This path varies with operating system.
Next, navigate to this direcotry and create the subdirectory `multimenus\_snippets`.
Then git clone the repositories of interest. 
The `+` versions are annotated with guides for editing the snippets.
These will become a hindrance for experienced users.  

The final command launches JupyterLab in the default webbrowser.
No error messages should appear in the terminal.
The menu bar should contain the items `cctbx`, `cctbx+`, `pymol` and `pymol+`.
The bash alias command `alias pcJL='conda activate pc37 && juptyer lab'` can reduce subsequent typing.
If there are irresolvable error messages, the broken environment can be removed with the command `conda env remove --name pc37`.
This first protocol has the upside using one kernel to call cctbx and pymol and the downside of possible  disruptions by updates to either PyMOL or CCTBX.


### Pymol and cctbx with separate Python interpreters from Anaconda


The second protocol creates a new conda environment for CCTBX but not PyMOL.
The upside of this approach is that updates to one program will not break the other program.
Separate kernels are created for CCTBX and for the PyMOL.app installed in the standard location.
The downsides of this approach are that it will necessitate not calling pymol and cctbx in the same cell and switching kernels when calling each program.

Name the new environment `cctbx37` is desgined to track the Python version used to create the environment. 
Ccreate a kernel named cctbx37 via the command `ipython kernel install --name cctbx37 --user`.
With PyMOL installed in the usual location via its installer, open PyMOL and install Jupyter inside it with the command `conda install -c conda-forge jupyter -y` entered at the PyMOL prompt.
The install can be slow and the PyMOL prompt may appeaer to hang.
Give it several minutes to complete.
Success at installation will be reported to the command history window above the PyMOL prompt.
Next, create a kernel named `pymol2.4.1` by entering in the terminal the following command that contains the path to the Ipython executable inside of the PyMOL.app.
On the Mac, the path and command is as follows: `/Applications/PyMOL.app/Contents/bin/ipython kernel install --name pymol37 --user`.

Download and move the snippet libraries into place as above.

```bash
# At the PyMOL prompt
conda create -n cctbx37 python=3.7 conda-forge::cctbx-base conda-forge::jupyter 
conda install conda-forge::jupyterlab=2.2.0
# In a terminal
/Applications/PyMOL.app/Contents/bin/jupyter serverextension enable --py jupyterlab --user
/Applications/PyMOL.app/Contents/bin/pip install jupyterlab-snippets-multimenus
/Applications/PyMOL.app/Contents/binjupyter lab build
/Applications/PyMOL.app/Contents/binjupyter lab clean
/Applications/PyMOL.app/Contents/bin/ipython kernel install --name pymol --user
/Applications/PyMOL.app/Contents/bin/jupyter --path # select the top option under Data for storing the libraries
cd ~.local/share/jupyter # change as per output from prior line
mkdir multimenus_snippets
cd multimenus_snippets
git clone https://github.com/MooersLab/juptyerlabpymolcctbx.git cctbx
git clone https://github.com/MooersLab/juptyerlabpymolcctbxplus.git cctbx+
git clone https://github.com/MooersLab/juptyerlabpymolpysnips.git pymol
git clone https://github.com/MooersLab/juptyerlabpymolpysnipsplus.git pymol+
/Applications/PyMOL.app/Contents/bin/jupyter lab # or jupyter-lab

```

### 

The third protocol uses the conda that ships with PyMOL; it does not require the creation of a new environment.
Open PyMOL and then install with separate conda commands jupyter, jupyter-lab, and then cctbx-base.
From the terminal as described above, create a pymol kernel named pymol2.4.1 to distinguish from subsequent installations of PyMOL:
/Applications/PyMOL.app/Contents/bin/ipython kernel install --name pymol2.4.1 --user
Install the extension with the command '/Applications/PyMOL.app/Contents/bin/python -m pip install jupyterlab-snippets-multimenus'.
Rebuild JuptyerLab with the command '/Applications/PyMOL.app/Contents/bin/juptyer-lab build'.
Then launch the JupyterLab with the command '/Applications/PyMOL.app/Contents/bin/jupyter-lab'.
To ease running this install of JupyterLab, add the following bash alias command to the standard location (e.g., .bashrc or .bashAliases): `alias pJL='/Applications/PyMOL.app/Contents/bin/jupyter-lab'`.
Download and move the snippet libraries into place as above.
The upside of this approach is that CCTBX can be called while using the PyMOL kernel, so there is no need to switch kernels.
The downsides are that this approach may be fragile to updates of either PyMOL or CCTBX.
Prior to updating PyMOL by using the package installer, the old version of the application should be renamed to avoid overwriting it.

```bash


/Applications/PyMOL.app/Contents/bin/ipython kernel install --name pymol37 --user
```


### 

A fourth protocol is restricted Windows.
Wheel files for installing PyMOL are available for download (https://www.lfd.uci.edu/~gohlke/pythonlibs/\#pymol-open-source).
The Python interpreter used to run CCTBX can also be used to install the pymol with the `pip.exe install` command. 
Both cctbx and pymol will share the same Python interpreter.
Conda or pip.exe can then be used to install jupyter and then juptyerlab. 
Then pip.exe would be used to install jupyterlab-snippets-multimenus as above.



```bash


/Applications/PyMOL.app/Contents/bin/ipython kernel install --name pymol37 --user
```


###  


```bash


/Applications/PyMOL.app/Contents/bin/ipython kernel install --name pymol37 --user
```




## Quick check of the installation

To quickly verify that PyMOL and CCTBX can be called in Jupyter from the same notebook, launch JupyterLab and open a new notebook.
Select the appropriate kernel.
Enter in the first cell `from pymol import cmd`.
No error message should appear.
The cmd class will be the chief means of interacting with PyMOL.
Enter in the next cell `import mmtbx.model`.
This command will import the model class of the mmtbx module.
No errors should be returned by this operation if all is installed correctly.



