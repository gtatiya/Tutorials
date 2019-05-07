
# Configuring Your Conda Environment on Tufts HPC

- You need an anaconda base installation, which will be shared across all your projects (and possibly shared with other people), and an individual conda environment for each of your projects. This document will guide you through setup of both.

- If possible, coordinate with other users in your lab to use a shared Anaconda base installation directory. This stuff is big, and if everyone gets their own copy, it takes up a lot of space.

  - If there is a pre-existing anaconda3 installation available, this is the easiest way to use it:

         cd /cluster/tufts/SOMELAB/anaconda3/bin
         ./conda init --dry-run
     
  - You should see `conda init` wants to modify your `.bashrc`. Run again without `--dry-run`, then logout and login. You should see your prompt preceded by `(base)` .

  - Skip all the steps below, until "After you have (base)"

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
	
- The installer has modified your `~/.bashrc` to source the new conda environment.
	
	- Logout and login again
	
- You should see your prompt preceded by `(base)` which means the anaconda base environment is available, and you have not activated any project environments.

#### After you have `(base)`

- After the anaconda base is installed, you will notice the command prompt preceded by `(base)`.  You can list your environments by `conda env list` and you can activate by `conda activate` and `conda deactivate`. 

- Always commit your environment configuration in your git repo, so you and others can recreate the environment later. This process also records pip packages, so it obsoletes the need for `requirements.txt`. Always install conda packages before any pip packages. If you need to install conda packages after you've already installed pip packages, it is recommended that you recreate your conda environment, with `conda env remove` followed by `conda env create -f conda-environment.yml`

  - Export your active environment to a new file

          conda env export > conda-environment.yml

  - Create a new environment from  `conda-environment.yml`
  
         conda env create -f conda-environment.yml

- You should always create a new environment for every new project. It does not take much disk space because each environment will internally use links for shared components that are in common to multiple environments. For more info, see [Using Pip in a Conda Environment](https://www.anaconda.com/using-pip-in-a-conda-environment/) and [Managing Environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html). 

- List your environments:

        conda env list

- Create an environment:

        conda create --name myenv
    
- Activate an environment:

        conda activate myenv

- Deactivate

        conda deactivate

#### To install PyTorch 

  - Browse to https://pytorch.org > Get Started
  - Use the configuration matrix.
  - Paste the command into your anaconda-enabled Terminal

#### To install TensorFlow 

- Do not install any pip packages until after you have installed all conda packages. See [Using Pip in a Conda Environment](https://www.anaconda.com/using-pip-in-a-conda-environment/). If you need to install conda packages after you've already installed pip packages, it is recommended that you recreate your conda environment (see above).
- Install tensorflow as follows:

        pip install tensorflow-gpu

