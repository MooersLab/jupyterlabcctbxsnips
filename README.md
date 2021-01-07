# jupyterlabcctbxsnips
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4317774.svg)](https://doi.org/10.5281/zenodo.4317774)

This readme file serves this GitHub site and three others: [jupyterlabcctbxsnipsplus](https://github.com/MooersLab/jupyterlabpymolcctbxplus), [jupyterlabpymolpysnips](https://github.com/MooersLab/jupyterlabpymolpysnips), and [jupyterlabpymolpysnipsplus](https://github.com/MooersLab/jupyterlabpymolpysnipsplus). 


## Introduction

The PyMOL is a powerful and popular molecular graphics program, CCTBX is the Computational Crystallography Toolbox that is the open-source part of the Phenix project, and JuptyerLab is an Integrated Development Environment (IDE) for editing Jupyter Notebooks.
These three programs can play together to support reproducible computational work in structural biology.
These electronic notebooks are also useful for exploring new software and writing tutorials.
They are wildly popular in the computational sciences: 9.7 million Jupyter Notebooks shared on GitHub as of December 2020.

The purpose of this site is to support the use of PyMOL and CCTBX together in Jupyter Notebooks.
The computational work is supported by snippet libraries for PyMOL and CCTBX.
The snippet libraries depend on the `jupyterlab-snippets-multimenus` extension.

If the installation followed in the second protocol listed in the first subsection below is successful and JupyterLab is started,
a scene similar to the figure below will appear.
You will be able to select the kernel named `pc38` instead of the default Python3 kernel.
In this case, the default kernel will also work.
The open circle by `pc38` means that the kernel is running.

The column at the left margin shows that the `jupyterlab-snippets-multimenus` extension has been installed.
The menubar should have `cctbx cctbx+ pymol pymol+` listed between `Kernel` and `Tabs`. 
Cell [1] in the Juptyer Notebook has been executed. 
The execution imported the `map_model_manager` class from CCTBX.
No error messages were returned.
Cell [2] imported the `cmd` class from pymol.
No error messages were returned.
Cell [3] shows the use of bang to run a bash command. 
In this case, the Python interpreter is being used to return documentation to the area below the cell
The blue bar in the left margin was triple-clicked to fold this output and replace it with three dots.

<p align="center"><img src="./images/Fig1lab.png" alt="HTML5 Icon" style="width:791px;height:278px;"></p>

The figure below shows part of the cascading menus for the cctbx library.
The submenus correspond to the names of subfolders in the `cctbx` folder in the `multimenus_snippets` folder._
Each ultimate menu item is a Python snippet file.
The selection of a file by clicking on it with the left-mouse buttons leads to its insertion into a new cell below the current cell.
In the figure below, the `millerArrayFromMtz.py` snippet at the bottom of the pulldown menu was selected and inserted.
Commented lines have text that describes what this snippet does.
The code in this cell would be executed by entering `Shift-Enter`.

<p align="center"><img src="./images/Fig2Pulldown.png" alt="HTML5 Icon" style="width:606px;height:404px;"></p>

## Some simple examples

The figures below demonstrate running PyMOL from inside a Jupyter notebook.
The `cmd.do()` method is used to send PyMOL macro language commands to PyMOL.
This method takes the commands as its argument.
Several PyMOL macro language commands are concatenated together with semicolons to save space.
The concatenated commands are enclosed in one set of quotes, single or double.

The `cmd.png()` method is used to save a png file of an image of an RNA duplex.
This method has its arguments passed to it in the style of a Python function.
The Image class from IPython is used to load the png file and display it below cell [2].

The RNA duplex is displayed with the ambient occlusion effect. 
The ambient occlusion effect is not built into PyMOL.
It is rendered by running the `AOD` shortcut.
This variant of the effect colors the carbon atoms black.
The `AO` shortcut colors the carbons light grey. 
The `AODBW` and `AOBW` variants color the atoms in grayscale.
Grayscale coloring is also not found in PyMOL, but it is available in the pymolshortcuts.py file.
The `rein` shortcut is mapped to the `reinitialize` command.
The `U8` shortcut fetches PDB file 3nd4, generates the biological unit, and orients the molecular object.

These shortcuts are one of over 200 functions loaded by the running of the `pymolshortcuts.py` script in [1].
The shortcuts are listed below Cell [1] when the script is loaded.
This listing has been hidden by folding. 
It can be displayed by clicking on the three dots.

Cell [1] demonstrates how external Python scripts can be loaded and run in PyMOL inside a Jupyter Notebook.
Note that the script is run in the same manner that they are loaded and run at PyMOL prompt in the PyMOL GUI.

<p align="center"><img src="./images/Fig3pymol.png" alt="HTML5 Icon" style="width:606px;height:404px;"></p>

The function `get_symm()` is from Robert Campbell's script `list_symm.py`.
It takes the space group number as an argument to look up the space group information in the `sgtbx` module of CCTBX.
It is being used here to display the symmetry operators of space group 155 with the shorthand notation found in the International Tables of Crystallography and as rotation matrices plus translation vectors.
This space group is the same as that for the above crystal structure (3ND4).
This function uses the `sys` module.
That module was already loaded upon the running of the `pymolshortcuts.py` script in [1], so it does not need to be imported again.

<p align="center"><img src="./images/Fig4cctbx.png" alt="HTML5 Icon" style="width:606px;height:404px;"></p>















## Roadmap of rest of this page

The first section below describes five ways to install these three packages so that they can play together.
There may be more ways. 
Please post an issue if you want to share another approach.
Please post an issue if one of the ways below changes.
Of course, as per the License, use these protocoals at your own risk. 
There are other approaches like Binder and Collab that are good for demonstrations, but their limitations hinder serious work.

The second section provides quick checks of the installation that can be made on the command line or in the Jupyter Noteobook.

The third section provides scripts for running the test scripts.

## Five ways to install PyMOL, CCTBX, and Jupyter 

The installation of both CCTBX, PyMOL, and Jupyter can be accomplished by one of several approaches.
All three packages are complex and best kept isolated in a dedicated environment.
Configuration files and paths to prior installations can still trip up new installations. 
Edits of the bashrc or zshrc startup files may be required.
On Mac OS X, I had to hide my `/usr/local/include` directory by `sudo mv /usr/local/include /usr/local/oldInclude`.

The extensions to JupyterLab depend on Node.js. 
An error message from conda about needing to install node and npm can be misleading when both programs are already installed. 
Running the command to enable the serverextension solves this problem: `jupyter serverextension enable --py jupyterlab --user`.
The `jupyterlab-snippets-multimenus` is not compatible with JuptyerLab 3.0.0 so version 2.2.0 has to be installed.

If the interpretable error messages have been addressed and there is still trouble, try another approach.
To remove the broken conda env, enter `conda env remove --name pc37` where the argument for the `--name` option is the name of the env.
Once a setup is working, **Do NOT!** tinker with it by adding new extensions or upgrading the packages.
All too often conflicts between dependent software will emerge and break the setup.
If you must tinker, create a new environment and build your new setup there so that at least the old version remains functional.

I suggest keeping notes on the nature of your conda environments.
After you have created two, it is easy loose track of their nature.



### PyMOL and CCTBX share a Python interpreter from Anaconda

The first approach is outlined in the code listing below.
It creates one Anaconda environment for using both PyMOL and CCTBX.
This approach uses one kernel in Jupyter.
It eliminates the need to switch between kernels in one notebook.
The protocol worked on a new instance on Ubuntu 20.04.
It also works on Mac OSX, although I had to move my `/usr/local/include` directory to avoid conflicts. 
First, update the existing software on Ubuntu and install Node.js and git.
Next, download the appropriate Anaconda installation script.
This script is run in the home directory to install Anaconda locally.
One conda command with a long argument list is run to install juptyer, pymol, and cctbx.
Here, the environment name pc37 represents pymol-cctbx-python3.7.
The shorthand name for the environment reduces the typing required when using this environment.

```bash
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
```

This new environment is activated, and JupyterLab is installed with the conda command.
The pip command is used to install the extension jupyterlab-snippets-multimenus from PyPi.
JuptyerLab is a server extension for Jupyter Notebook.
It may need to be activated.
Activation of the extension requires that JupyterLab is rebuilt.

The `jupyter --path` command returns a list of paths that vary between operating systems.
The top path listed under Data is where the snippet libraries are stored.
This path varies with the operating system.
Next, navigate to this directory and create the subdirectory `multimenus_snippets`.
Then git clone the repositories of interest. 
The `+` versions are annotated with guides for editing the snippets.
These annotations become an annoyance for experienced users. 
If you are aksed for a username and passward to your GitHub accoung, you can instead download each repository as a zip file. 

The final command launches JupyterLab in the default web browser.
No error messages should appear in the terminal.
The menu bar should contain the items `cctbx`, `cctbx+`, `pymol` and `pymol+`.
The bash alias command `alias pcJL='conda activate pc37 && juptyer lab'` can reduce subsequent typing.
If there are irresolvable error messages, the broken environment can be removed with the command `conda env remove --name pc37`.
This first protocol has the upside of using one kernel to call CCTBX and PyMOL and the downside of possible disruptions by updates to either PyMOL or CCTBX.

Below is the alternate protocol for PyMOL version 2.4.1 and Python3.8.
This protocol worked on January 7, 2021.

```bash
apt install nodejs git
wget -P /tmp /https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh
bash Anaconda3-2020.02-Linux-x86_64.sh
conda create -n pc38 python=3.8 schrodinger::pymol-bundle=2.4.1 conda-forge::cctbx-base conda-forge::jupyter -y
conda activate pc38
conda install conda-forge::jupyterlab=2.2.0 -y
# The following may be needed
# jupyter serverextension enable --py jupyterlab --user 
pip install jupyterlab-snippets-multimenus
# jupyter lab clean
jupyter lab build # can take awhile
ipython kernel install --name pc38 --user # create a kernel
# Stored in /home/blaine/.local/share/jupyter/kernels/pc38
jupyter --path # select the top option under Data for storing the libraries
cd ~/.local/share/jupyter # change as per output from prior line
mkdir multimenus_snippets
cd multimenus_snippets
git clone https://github.com/MooersLab/juptyerlabpymolcctbx.git cctbx
git clone https://github.com/MooersLab/juptyerlabpymolcctbxplus.git cctbx+
git clone https://github.com/MooersLab/juptyerlabpymolpysnips.git pymol
git clone https://github.com/MooersLab/juptyerlabpymolpysnipsplus.git pymol+
jupyter lab # or libtbx.python -m jupyter-lab
```

The above protocols can be adapted to Mac OS X with the appropriate changes in the name of the Anaconda install script and changes in the paths.
The snippetes are stored in `~/Library/Juptyer/multimenus_snippers`.
The kernels are stored in `~/Library/Juptyer/kernels`.
If Node.js is missing, it can be installed with Anaconda or Home Brew. 
Node.js must of a version greater than 10.0.0 (e.g., `conda install conda-forge::nodejs=15.3`). 
Anaconda will sometimes degrade Node.js to around version 6 when installing some other software in the env.
A prior installation of JuptyerLab=3.0.0 can cause trouble.
Run `jupyter serverextension enable --py jupyterlab --user` to reset the configuration for JupyterLab=2.2.0.
If desparate, delete the configuration in `~/.juptyer` and reinstall.


### PyMOL and CCTBX have separate Python interpreters from Anaconda

This second protocol creates a new conda environment for CCTBX and uses an existing installation of PyMOL.
The upside of this approach is that updates to one program will not break the other program.
JuptyerLab is installed in both the CCTBX environment and again in PyMOL.
Separate kernels are created for CCTBX and for the Python interpreter in the PyMOL.app.
PyMOL and  CCTBX cannot be called from the same cell.
Also, the kernel has to be switched when changing programs.
The name  `cctbx37` is designed to track the Python version used to create the environment. 
Create a Juptyer kernel also named cctbx37.


With PyMOL installed in the usual location via its installer, open PyMOL and install Jupyter inside it with the command `conda install -c conda-forge jupyter -y` entered at the PyMOL prompt.
The install can be slow and the PyMOL prompt may appear to hang.
Give it several minutes to complete.
Success at installation will be reported to the command history window above the PyMOL prompt.
Next, create a kernel named `pymol2.4.1` by entering in the terminal the following command that contains the path to the Ipython executable inside of the PyMOL.app.
On the Mac, the path and command is as follows: `/Applications/PyMOL.app/Contents/bin/ipython kernel install --name pymol37 --user`.

Download and move the snippet libraries into place as above.

```bash

conda create -n cctbx37 python=3.7 conda-forge::cctbx-base conda-forge::jupyter 
conda install conda-forge::jupyterlab=2.2.0
ipython kernel install --name cctbx37 --user

# Inside PyMOL, paste the following at the command prompt
conda install conda-forge::jupyter conda-forge::jupyterlab=2.2.0 -y

# Inside PyMOL, paste the following at the command prompt
/Applications/PyMOL.app/Contents/bin/jupyter serverextension enable --py jupyterlab --user
/Applications/PyMOL.app/Contents/bin/pip install jupyterlab-snippets-multimenus
/Applications/PyMOL.app/Contents/bin/jupyter lab build
/Applications/PyMOL.app/Contents/bin/jupyter lab clean
/Applications/PyMOL.app/Contents/bin/ipython kernel install --name pymol --user
/Applications/PyMOL.app/Contents/bin/jupyter --path # select the top option under Data for storing the libraries
cd ~.local/share/jupyter # change as per output from prior line
mkdir multimenus_snippets
cd multimenus_snippets
git clone https://github.com/MooersLab/juptyerlabpymolcctbx.git cctbx
git clone https://github.com/MooersLab/juptyerlabpymolcctbxplus.git cctbx+
git clone https://github.com/MooersLab/juptyerlabpymolpysnips.git pymol
git clone https://github.com/MooersLab/juptyerlabpymolpysnipsplus.git pymol+
/Applications/PyMOL.app/Contents/bin/jupyter lab 
```

After starting JuptyerLab, select either the `pymol` kernel or the `cctbx37`.


### Install CCTBX inside of PyMOL

The third protocol uses the conda that ships with PyMOL; it does not require a separate Anaconda installation.
This protocol assumes that git is already installed.
Open PyMOL and then install with separate conda commands jupyter, jupyter-lab, and then cctbx-base.
The subsequent commands issued from the terminal.
Adjust the path to the PyMOL.app as needed.
Enalbe the JupyterLab severer extension.
Create a Juptyer kernel named `pymol`.
Install the JuptyerLab extension with pip.
Rebuild JuptyerLab and install the snippets via git clone.
Launch the JupyterLab with the command `/Applications/PyMOL.app/Contents/bin/jupyter-lab`.
To ease running this install of JupyterLab, add the following bash alias command to the standard location (e.g., .bashrc or .bashAliases): `alias pJL='/Applications/PyMOL.app/Contents/bin/jupyter-lab'`.

```bash
# At the PyMOL prompt in the PyMOL GUI paste the following:
conda install conda-forge::cctbx-base conda-forge::jupyter 
conda install conda-forge::jupyterlab=2.2.0
conda install conda-forge::cctbx-base
# In a terminal
/Applications/PyMOL.app/Contents/bin/jupyter serverextension enable --py jupyterlab --user
/Applications/PyMOL.app/Contents/bin/ipython kernel install --name pymol --user
/Applications/PyMOL.app/Contents/bin/pip install jupyterlab-snippets-multimenus
/Applications/PyMOL.app/Contents/bin/jupyter lab build
/Applications/PyMOL.app/Contents/bin/jupyter lab clean
/Applications/PyMOL.app/Contents/bin/jupyter --path # select the top option under Data for storing the libraries
cd ~.local/share/jupyter # change as per output from prior line
mkdir multimenus_snippets
cd multimenus_snippets
git clone https://github.com/MooersLab/juptyerlabpymolcctbx.git cctbx
git clone https://github.com/MooersLab/juptyerlabpymolcctbxplus.git cctbx+
git clone https://github.com/MooersLab/juptyerlabpymolpysnips.git pymol
git clone https://github.com/MooersLab/juptyerlabpymolpysnipsplus.git pymol+
/Applications/PyMOL.app/Contents/bin/ipython kernel install --name pymol37 --user
```

The upside of this approach is that CCTBX can be called while using the PyMOL kernel, so there is no need to switch kernels.
The downsides are that this approach may be fragile to updates of either PyMOL or CCTBX.
Prior to updating PyMOL by using the package installer, the old version of the application should be renamed to avoid overwriting it.
Appending the version number (e.g., PyMOL241.app) will not impede its operation.


### Install PyMOL wheel with the Python interpreter used to install CCTBX (Windows only)

A fourth protocol is restricted to Windows.
Wheel files for installing PyMOL are available for [download](https://www.lfd.uci.edu/~gohlke/pythonlibs/\#pymol-open-source).
Determine the version of Python already present and whether the operating system is 32 or 64 bit.
The Python interpreter used to run CCTBX can also be used to install PyMOL with the `pip.exe install` command. 
Both cctbx and pymol will share the same Python interpreter.
Conda or pip.exe can be used to install Jupyter and then JupyterLab. 
Then pip.exe would be used to install jupyterlab-snippets-multimenus as above.

```bash
/Applications/PyMOL.app/Contents/bin/ipython kernel install --name pymol37 --user
```


###  Install PyMOL with cctbx.python (Fedora, maybe other Linuxes)

A fifth protocol applies where there is a clear path to building PyMOL from source code.
The idea is to build and install PyMOL using the same Python Interpreter that was used to build CCTBX.
This approach is adapted from the one for [Fedora](https://pymolwiki.org/index.php/CCTBX-fedora32).
Although this approach uses conda to install the dependencies, it does not require creating an environment.
Supplement this protocol with the following commands.

```bash
/usr/local/miniconda3/bin/conda install -p /usr/local/cctbx-dev-2130/conda_base conda-forge::juptyer
/usr/local/miniconda3/bin/conda install -p /usr/local/cctbx-dev-2130/conda_base conda-forge::juptyerlab=2.2.0
/usr/local/miniconda3/bin/pip install jupyterlab-snippets-multimenus
/usr/local/miniconda3/bin/ipython kernel install --name pymolcctbx --user
/usr/local/miniconda3/bin/jupyter --path
cd ~.local/share/jupyter # change as per Data line in output from prior comment
mkdir multimenus_snippets
cd multimenus_snippets
git clone https://github.com/MooersLab/juptyerlabpymolcctbx.git cctbx
git clone https://github.com/MooersLab/juptyerlabpymolcctbxplus.git cctbx+
git clone https://github.com/MooersLab/juptyerlabpymolpysnips.git pymol
git clone https://github.com/MooersLab/juptyerlabpymolpysnipsplus.git pymol+
/usr/local/miniconda3/bin/jupyter lab
```


## Quick check of the installation

To quickly verify that PyMOL and CCTBX can be called in Jupyter from the same notebook, launch JupyterLab and open a new notebook.
Select the appropriate kernel.
Enter in the first cell `from pymol import cmd` and hit shift-return.
No error message should appear.
Enter in the next cell `from iotbx.map_model_manager import map_model_manager`.
No errors should be returned by this operation if all is installed correctly.

Where both CCTBX and PyMOL are run by the same Python interpreter, activate the appropriate environment and run the following command in a terminal:

```bash
python -c 'from pymol import cmd; from iotbx.map_model_manager import map_model_manager'
```

If all goes well, the terminal will hang for about five seconds and then return nothing.
Otherwise, error messages will be printed in the terminal window.


## More extensive tests


The CCTBX installation in conda environment can be tested by running the following bash script.

```bash
#! /bin/sh
set noglob
set verbose
libtbx.python $CONDA_PREFIX/lib/python3.7/site-packages/libtbx/run_tests.py
libtbx.python $CONDA_PREFIX/lib/python3.7/site-packages/iotbx/run_tests.py
libtbx.python $CONDA_PREFIX/lib/python3.7/site-packages/boost_adptbx/run_tests.py
libtbx.python $CONDA_PREFIX/lib/python3.7/site-packages/fable/run_tests.py
libtbx.python $CONDA_PREFIX/lib/python3.7/site-packages/scitbx/run_tests.py
libtbx.python $CONDA_PREFIX/lib/python3.7/site-packages/cctbx/run_tests.py
libtbx.python $CONDA_PREFIX/lib/python3.7/site-packages/cctbx/run_examples.py
libtbx.python $CONDA_PREFIX/lib/python3.7/site-packages/smtbx/run_tests.py
libtbx.python $CONDA_PREFIX/lib/python3.7/site-packages/cflib_adaptbx/run_tests.py
libtbx.python $CONDA_PREFIX/lib/python3.7/site-packages/reduce/run_tests.py
libtbx.python $CONDA_PREFIX/lib/python3.7/site-packages/mmtbx/run_tests.py
libtbx.python $CONDA_PREFIX/lib/python3.7/site-packages/cctbx_website/run_tests.py
libtbx.python $CONDA_PREFIX/lib/python3.7/site-packages/gltbx/run_tests.py
```

If cctbx was installed with python3.8, use the following bash script.

```bash
#! /bin/sh
set noglob
set verbose
libtbx.python $CONDA_PREFIX/lib/python3.8/site-packages/libtbx/run_tests.py
libtbx.python $CONDA_PREFIX/lib/python3.8/site-packages/iotbx/run_tests.py
libtbx.python $CONDA_PREFIX/lib/python3.8/site-packages/boost_adptbx/run_tests.py
libtbx.python $CONDA_PREFIX/lib/python3.8/site-packages/fable/run_tests.py
libtbx.python $CONDA_PREFIX/lib/python3.8/site-packages/scitbx/run_tests.py
libtbx.python $CONDA_PREFIX/lib/python3.8/site-packages/cctbx/run_tests.py
libtbx.python $CONDA_PREFIX/lib/python3.8/site-packages/cctbx/run_examples.py
libtbx.python $CONDA_PREFIX/lib/python3.8/site-packages/smtbx/run_tests.py
libtbx.python $CONDA_PREFIX/lib/python3.8/site-packages/cflib_adaptbx/run_tests.py
libtbx.python $CONDA_PREFIX/lib/python3.8/site-packages/reduce/run_tests.py
libtbx.python $CONDA_PREFIX/lib/python3.8/site-packages/mmtbx/run_tests.py
libtbx.python $CONDA_PREFIX/lib/python3.8/site-packages/cctbx_website/run_tests.py
libtbx.python $CONDA_PREFIX/lib/python3.8/site-packages/gltbx/run_tests.py
```

