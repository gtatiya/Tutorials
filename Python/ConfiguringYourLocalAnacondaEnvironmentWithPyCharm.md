
# Configuring Your Local Anaconda Environment with PyCharm

- There is a version of PyCharm made specifically for anaconda: https://www.jetbrains.com/pycharm/promo/anaconda/. As academics, you can get the Professional version for free: https://www.jetbrains.com/student/

- During first launch, don't click "Skip." There is a button for "Install Miniconda 3" which is good. Do that.

- After the initial dialogs, click "Create a new project"
	
	- In the New Project dialog, create a new conda environment for your project by selecting "Pure Python" and new environment "Conda" as seen in the image below. You should always create a new environment for every new project. See [Using Pip in a Conda Environment](https://www.anaconda.com/using-pip-in-a-conda-environment/) for more info.
	  ![pycharm_new_project_conda](images/pycharm_new_project_conda.png)
	- To manage your environment, you may benefit from these commands:
	  - `conda list --export > requirements-conda.txt`
	  - `pip freeze > requirements.txt`
	  - `conda install --file requirements-conda.txt`
	  - `pip install -r requirements.txt`
	- If you want to use a remote Python interpreter for the project, select Existing interpreter > SSH Interpreter and provide your SSH credentials. More info: https://www.jetbrains.com/help/pycharm/configuring-remote-interpreters-via-ssh.html
	
- With your project open, go to the `Terminal` tab (or go to View > Tool Windows > Terminal). Notice your complete anaconda environment is available in this Terminal, so you can run `conda` commands.

  - If you want your regular Terminal (outside of PyCharm) to also use this anaconda environment, do this one-time setup. Use the `--dry-run` option first to see what it will do, then repeat without `--dry-run`.

          conda init --dry-run

- To install PyTorch 

  - Browse to https://pytorch.org > Get Started
  - Use the configuration matrix.
  - Paste the command into your anaconda-enabled Terminal (see above)

- To install TensorFlow 
	- Do not install any pip packages until after you have installed all conda packages. See [Using Pip in a Conda Environment](https://www.anaconda.com/using-pip-in-a-conda-environment/).  
	- If you have GPU (not supported on Mac): `pip install tensorflow-gpu`
	- If you don’t have GPU: `pip install tensorflow`
