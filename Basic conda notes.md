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
    conda env create -f conda-environment.yml

