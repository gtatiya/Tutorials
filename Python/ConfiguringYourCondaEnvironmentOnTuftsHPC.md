
# Configuring Your Conda Environment on Tufts HPC

- If possible, coordinate with other users in your lab to use a shared Anaconda installation directory. This stuff is big, and if everyone gets their own copy, it takes up a lot of space.
- Your home directory does not have enough space for Anaconda installation. So, request for extra storage or get access to a lab research storage space.
- Before you begin: 
	- Login via ssh to login.cluster.tufts.edu
	- Ensure you do not have any modules loaded 
		- `module list`
		- If necessary, edit your .bashrc and .bash_profile to remove modules, then module purge, or logout and login again
		- Software installations, etc. should happen on a compute node. Activity on the login nodes is monitored, and this installation takes enough CPU time that it will trigger an alert. Your friendly research sysadmin staff will contact you and remind you not to do this on login nodes.
		○ To get a prompt on a compute node, this will have a 2 hour limit and 2G memory, so adjust according to your needs: `srun -t 0-02:00 --mem 2000 -p interactive --pty bash`
- In your local web browser, go to https://www.anaconda.com/ > Download > Linux > Right-click the "64bit x86" link, copy URL
- Do this on a compute node:
- wget the URL 
	- In my case, `wget https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-x86_64.sh`
- Run it: `bash Anaconda3-2019.03-Linux-x86_64.sh` 
	- Accept license
	- Installation directory: 
		- You cannot use your home directory; not enough disk space.
		- Use something like this: `/cluster/tufts/SOMELAB/USERMANE/anaconda3`
		- Yes, initialize Anaconda3 by running conda init
- The installer has modified your `~/.bashrc` to source the new conda environment. If not, run `echo "source /cluster/tufts/SOMELAB/USERMANE/anaconda3/etc/profile.d/conda.sh" >> ~/.bashrc`
	- Logout and login again to get the new environment
- To install PyTorch:
	- Browse to https://pytorch.org > Get Started
	- Use the configuration matrix. I'm using Stable, Linux, Conda, Python 3.7, CUDA 10.0 
	- Paste the command into your compute node prompt
		- For me, it was: `conda install pytorch torchvision cudatoolkit=10.0 -c pytorch`
- To install TensorFlow: 
	- Browse to https://tensorflow.org/install/ > GPU Guide
	- Run this on a compute node: `pip install tensorflow-gpu`
- To create a separate environment, use `conda create -n py2 python=2 numpy matplotlib tensorflow-gpu jupyter`. Then use can activate this environment by `conda activate py2`.
