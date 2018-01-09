# NASNet

* [Google NASNet Blog](https://research.googleblog.com/2017/11/automl-for-large-scale-image.html)
* [NASnet Keras](https://github.com/johannesu/NASNet-keras)
* [Inception Keras](https://github.com/EN10/KerasInception)

Install:

    sudo pip install -U pip
    sudo pip install tensorflow
    
    sudo apt update 
    sudo apt install python-dev 
    sudo pip install keras
    
    sudo pip install h5py imageio 

Performance:

    wget https://github.com/EN10/BuildTF/raw/771df48529285c69ef760327121e996750b3916e/tensorflow-1.4.0-cp27-none-linux_x86_64.whl    
    sudo pip install --ignore-installed --upgrade tensorflow-1.4.0-cp27-none-linux_x86_64.whl

Run:

    python predict.py

c9 Disk Usage Before:

    du -hd1 /
    54M     /home
    2.0G	/usr
    
Error:

`The TensorFlow library was compiled to use AVX2 instructions, but these aren't available on your machine.`

AVX2 flag missing from your CPU.

    less /proc/cpuinfo 