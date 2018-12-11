# README #

The two demos in the repository show how to include group sparse regularization while training neural networks, both in TensorFlow and Keras. Group sparse regularization can be used to remove entire neurons (and/or input features) during training by pushing the corresponding rows of weights to zero simultaneously.

In the demos, we train a simple neural network with two hidden layers on the Boston dataset included inside scikit-learn. The number of neurons is monitored during training and shown at the end of the run (for the TensorFlow demo, we use the TensorBoard for visualization).

### What is group sparse regularization? ###

The use of group sparse regularization inside neural networks is described in the following paper:

Scardapane, S., Comminiello, D., Hussain, A. and Uncini, A., 2017. **Group sparse regularization for deep neural networks**. _Neurocomputing_, 241, pp.81-89.  
[**Preprint version from arXiv.**](https://arxiv.org/abs/1607.00485)
    
For each node in the network, we include a regularization term pushing the entire row of outgoing weights to be zero simultaneously. This is done by constraining the L2 norm of the row, weighted by the square root of its dimensionality (see the paper for more details). Note that in the code we do not regularize biases. Also, optimal results are achieved by combining this form of regularization with standard L1 or L2 regularization.

### How to run the demo ###

Simply run the demo corresponding to the desired library. Results for TensorFlow are saved in a folder inside 'summaries' and can be viewed from the TensorBoard, while results for the Keras demo are plotted using Matplotlib at the end of the run. This is an example of evolution of the number of neurons for a prototypical run:

![Example-neurons-TensorBoard.png](https://bitbucket.org/repo/ngEnX67/images/718405541-Example-neurons-TensorBoard.png)

### Contact me ###

The original code for the paper was written for Lasagne and Theano and is available here:
    [https://bitbucket.org/ispamm/group-lasso-deep-networks.](https://bitbucket.org/ispamm/group-lasso-deep-networks)

This code is only provided as a demo, and it was not optimized for efficiency, nor fully tested. If you find any bug or if you would like to extend the demo in some way, feel free to contact me at:

* simone (dot) scardapane (at) uniroma1 (dot) it.