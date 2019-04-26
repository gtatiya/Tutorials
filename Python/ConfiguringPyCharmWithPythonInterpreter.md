
# Configuring PyCharm with Python interpreter

• There is a version of PyCharm made specifically for anaconda: https://www.jetbrains.com/pycharm/promo/anaconda/. As academics, you can get the Professional version for free: https://www.jetbrains.com/student/
• During first launch, don't click "Skip." There is a button for "Install Miniconda 3" which is good. Do that.
• After the initial dialogs, Create a new project > Pure Python
	○ If you want to create a separate python environment for the project, select New Environment using Conda and provide Python version you want and its installation location.
	○ If you want to use an existing python environment for the project, select Existing interpreter > Conda Environment, and provide the location existing python interpreter. Here you could selected the Miniconda 3 you just installed.
	○ If you want to use a remote Python interpreter for the project, select Existing interpreter > SSH Interpreter and provide your SSH credentials. More info: https://www.jetbrains.com/help/pycharm/configuring-remote-interpreters-via-ssh.html
• To install PyTorch 
	○ With your project open, at the bottom of the window, there is a Terminal tab. This is different from your standard Terminal.app, because it automatically loads your environment for you.
	○ Go to the terminal in the bottom tab
	○ Browse to https://pytorch.org > Get Started
	○ Use the configuration matrix.
	○ Paste the command into your Pycharm Terminal
• To install TensorFlow 
	○ If you have GPU: `pip install tensorflow-gpu`
	○ If you don’t have GPU: `pip install tensorflow`
