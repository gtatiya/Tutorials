# How to install TensorFlow with GPU on Ubuntu 16.04?

You need to install Nvidia driver, CUDA and cuDNN before you install TensorFlow with GPU.
It is not necessary that their latest version is supported by the latest version of TensorFlow.
First, find which CUDA version and cuDNN version is supported by the latest version of TensorFlow: https://www.tensorflow.org/install/source#linux

<img src="https://github.com/gtatiya/Tutorials/blob/master/Ubuntu/TensorFlow_Linux_Versions.png" align="middle">

Currently, the latest version of TensorFlow supports `CUDA 9` and `cuDNN 7`.

Then, find the compatible Nvidia driver for `CUDA 9`: https://docs.nvidia.com/deploy/cuda-compatibility/index.html#binary-compatibility__table-toolkit-driver

<img src="https://github.com/gtatiya/Tutorials/blob/master/Ubuntu/CUDA_Driver_Version.png" align="middle">

You need `Nvidia driver 384` for `CUDA 9` .

Now that you know version of Nvidia driver, CUDA and cuDNN, you just need to install them.

## Installing Nvidia Driver

- Add the graphics drivers PPA:
```
sudo add-apt-repository ppa:graphics-drivers
sudo apt-get update
```

- Install Nvidia Driver for CUDA 9:
	`sudo apt-get install nvidia-384`

- Reboot your computer

- Run `nvidia-smi` and check your Nvidia Driver versiona and GPU.

- If you want to delete this installation, run `sudo apt-get purge nvidia*`

