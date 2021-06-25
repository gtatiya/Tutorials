# Basic conda notes

Create an environment with a specific version of python

    conda create -n myenv 'python>3.5'
    conda create -n myenv 'python=3.7.10'
    conda create -n myenv 'python>=3.8,<3.9'
    
    Use '' characters to prevent shell from parsing | and < and >
    | means OR
    , means AND
    <, >, <=, >=, ==, !=

To delete an environment

    (if it's active, deactivate it first)
        conda deactivate
    conda env remove -n myenv

Activate the environment

    conda activate myenv

Search for and install some modules

    conda search jupyterlab
    conda install -y jupyterlab

Save your environment, or reinstall a previously saved environment

    conda env export > conda-environment.yml
    	Optionally, edit the file. Suggested edits are:
    	- Remove the `prefix` line that has a path, which is specific to your system.
    	- Allow the python (and maybe other packages) patch number to vary with wildcard `*`
    	  python=3.8.*
    	- Comment-out all dependencies that conda added automatically.
    	  Only keep lines that correspond to packages you installed intentionally.
    	  This will allow conda to do its dependency work freely in the future,
    	  but maintain a record of exact package versions (commented out)
    	  just in case you need them.
    
    conda env create -f conda-environment.yml

