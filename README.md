# NASNet

**Deprecated** for now, see [Keras Models](https://github.com/EN10/KerasInception/blob/master/Models.md) for working NASnet example.

* Based on [NASnet Keras](https://github.com/johannesu/NASNet-keras)
* [Google NASNet Blog](https://research.googleblog.com/2017/11/automl-for-large-scale-image.html)
* [Inception Keras](https://github.com/EN10/KerasInception)
* [Keras Weights](https://github.com/titu1994/Keras-NASNet/releases)

### Install:

    sudo pip install -U pip
    sudo pip install tensorflow
    
    sudo apt update 
    sudo apt install python-dev 
    sudo pip install keras
    
    sudo pip install h5py imageio 

### Performance:

    wget https://github.com/EN10/BuildTF/raw/771df48529285c69ef760327121e996750b3916e/tensorflow-1.4.0-cp27-none-linux_x86_64.whl    
    sudo pip install --ignore-installed --upgrade tensorflow-1.4.0-cp27-none-linux_x86_64.whl

[FloydHub](https://github.com/EN10/FloydHub)

### Run:

    python predict.py

### Error:

`The TensorFlow library was compiled to use AVX2 instructions, but these aren't available on your machine.`

AVX2 flag missing from your CPU.

    less /proc/cpuinfo 
    
### Info

c9 Disk Usage Before:

    du -hd1 /
    54M     /home
    2.0G	/usr

Data downloaded to `~/.keras`

c9 free supports: 1GB RAM & 5GB HDD