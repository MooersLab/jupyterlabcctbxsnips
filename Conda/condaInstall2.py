conda remove --name cctbx37
conda create -n cctbx38 -c conda-forge cctbx-base python=3.8
conda activate cctbx38
conda install -c conda-forge cctbx-base
conda install -c anaconda ipykernel
python -m ipykernel install --user --name cctbx38 --display-name "cctbx38"
