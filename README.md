<div align="center">

  <a href="https://www.tensorflow.org">![TensorFLow](https://img.shields.io/badge/TensorFlow-2.X-orange?style=for-the-badge) 
  <a href="https://github.com/EMalagoli92/PonderNet-TensorFlow/blob/main/LICENSE">![License](https://img.shields.io/github/license/EMalagoli92/PonderNet-TensorFlow?style=for-the-badge) 
  <a href="https://www.python.org">![Python](https://img.shields.io/badge/python-%3E%3D%203.9-blue?style=for-the-badge)</a>  
  
</div>

# PonderNet - TensorFlow

TensorFlow 2.X reimplementation of [PonderNet: Learning to Ponder](https://arxiv.org/abs/2107.05407), Andrea Banino, Jan Balaguer, Charles Blundell.

## Table of content
- [Abstract](#abstract)
- [Experiment on Parity Task](#paritytask)    
- [Installation](#installation)
- [Usage](#usage)    
- [Acknowledgement](#acknowledgement)    
- [Citations](#citations)
- [License](#license)    
    
<div id="abstract"/>

## Abstract
In standard neural networks the amount of computation used grows with the size of the inputs, but not with the complexity of the problem being learnt. To overcome this limitation we introduce PonderNet, a new algorithm that learns to adapt the amount of computation based on the complexity of the problem at hand. PonderNet learns end-to-end the number of computational steps to achieve an effective compromise between training prediction accuracy, computational cost and generalization. On a complex synthetic problem, PonderNet dramatically improves performance over previous adaptive computation methods and additionally succeeds at extrapolation tests where traditional neural networks fail. Also, our method matched the current state of the art results on a real world question and answering dataset, but using less compute. Finally, PonderNet reached state of the art results on a complex task designed to test the reasoning capabilities of neural networks.

<div id="paritytask"/>
    
## Experiment  on Parity Task


![Parity Task](https://raw.githubusercontent.com/EMalagoli92/PonderNet-TensorFlow/main/assets/images/parity_task.png)    
    
    
<div id="installation"/>
    
## Installation
Clone the repo and install necessary packages 
```
git clone https://github.com/EMalagoli92/PonderNet-TensorFlow.git
pip install -r requirements.txt
```
Tested on *Ubuntu 20.04.4 LTS x86_64*, *python 3.9.7*.    
    
<div id="usage"/>
    
## Usage
Train a PonderNet on Parity Task
```
python experiment.py    
```
  



<div id="acknowledgement"/>

## Acknowledgement
- [PonderNet](https://nn.labml.ai/adaptive_computation/ponder_net/index.html) (Official PyTorch Implementation)
    

<div id="citations"/>
    
## Citations
```bibtex
@misc{banino2021pondernet,
      title={PonderNet: Learning to Ponder}, 
      author={Andrea Banino and Jan Balaguer and Charles Blundell},
      year={2021},
      eprint={2107.05407},
      archivePrefix={arXiv},
      primaryClass={cs.LG}
}
```


<div id="license"/>

## License
This work is made available under the [MIT License](https://github.com/EMalagoli92/PonderNet-TensorFlow/blob/main/LICENSE)
