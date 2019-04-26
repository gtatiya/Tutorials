# How to install TensorFlow with GPU on Ubuntu 16.04?

You need to install Nvidia driver, CUDA and cuDNN before you install TensorFlow with GPU.
It is not necessary that their latest version is supported by the latest version of TensorFlow.
First, find which CUDA version and cuDNN version is supported by the latest version of TensorFlow: https://www.tensorflow.org/install/source#linux

<img src="https://github.com/gtatiya/Tutorials/blob/master/Ubuntu/TensorFlow_Linux_Versions.png" align="middle">

Currently, the latest version of TensorFlow supports `CUDA 9` and `cuDNN 7`.

Then, find the compatible Nvidia driver for `CUDA 9`: https://docs.nvidia.com/deploy/cuda-compatibility/index.html#binary-compatibility__table-toolkit-driver

<img src="https://github.com/gtatiya/Tutorials/blob/master/Ubuntu/CUDA_Driver_Version.png" align="middle">

You need `Nvidia driver 384` for `CUDA 9` .

Now that you know versions of Nvidia driver, CUDA and cuDNN, you just need to install them.

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

## Installing CUDA

- Download `CUDA 9`: https://developer.nvidia.com/cuda-90-download-archive?target_os=Linux&target_arch=x86_64&target_distro=Ubuntu&target_version=1604&target_type=runfilelocal <br>
Here's the list of all the CUDA versions: https://developer.nvidia.com/cuda-toolkit-archive

- Press `Ctrl+Alt+F1` and login using your credentials

- kill your current X server session: `sudo service lightdm stop`

- Make the file executable

```
chmod +x cuda_9.0.176_384.81_linux.run
chmod +x cuda_9.0.176.1_linux.run
chmod +x cuda_9.0.176.2_linux.run
chmod +x cuda_9.0.176.3_linux.run
chmod +x cuda_9.0.176.4_linux.run
```

- Install

```
sudo sh cuda_9.0.176_384.81_linux.run
sudo sh cuda_9.0.176.1_linux.run
sudo sh cuda_9.0.176.2_linux.run
sudo sh cuda_9.0.176.3_linux.run
sudo sh cuda_9.0.176.4_linux.run
```

While installation select <b> NO </b> for Install NVIDIA Accelerated Graphics Driver for Linux-x86_64 387.26?

- Reboot your computer

- Open your bashrc: `gedit ~/.bashrc` and add these lines to the bottom and save:

```
export PATH=$PATH:/usr/local/cuda/bin
export LD_LIBRARY_PATH=/usr/local/cuda/lib64
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda/extras/CUPTI/lib64
```

- Configure dynamic linker run-time bindings: `sudo ldconfig`

- Run `nvcc --version` and check your CUDA versiona.

- If you want to delete this installation, run `sudo /usr/local/cuda-9.1/bin/uninstall_cuda_9.0.pl` 

## Installing cuDNN

- Download `cuDNN 7`: https://developer.nvidia.com/compute/machine-learning/cudnn/secure/v7.0.5/prod/9.0_20171129/cudnn-9.0-linux-x64-v7 <br>
Here's the list of all the cuDNN versions: https://developer.nvidia.com/rdp/cudnn-archive

- Extract the cudnn-9.0-linux-x64-v7.tgz

- Run this:
```
sudo cp cuda/include/cudnn.h /usr/local/cuda/include
sudo cp cuda/lib64/libcudnn* /usr/local/cuda/lib64
sudo chmod a+r /usr/local/cuda/include/cudnn.h
sudo chmod a+r /usr/local/cuda/lib64/libcudnn*
```

## Installing TensorFlow

- `pip install tensorflow-gpu==1.12.0`

- More info: https://www.tensorflow.org/install/
