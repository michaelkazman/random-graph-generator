# random-chart-generator
## About
The purpose of this project is to generate random charts (such as bar charts, box plots, histograms, etc.) from a multitude of visualization libraries.

These graphs will be used as input data for a Generative Adversarial Network tasked with translating graphical images to text for the visually impaired.

## Setup
The `setup/setup.sh` script can be used to automatically setup the project environment. However, if a manual installation is preferred, the instructions below provide a step-by-step breakdown of the entire process. Both options assume you are in the projects root dir.

**Note:** The setup instructions assume both [Anaconda](https://www.anaconda.com/products/individual) and [Jupyter](https://jupyter.org/install) are installed. If they are not already installed, please do so.

<br/>

### Automated
1. **Execute the `setup/setup.sh` script**
    ```
    sh setup/setup.sh
    ```
1. **Select created kernel**
    
    As seen in the following image, switch the kernel to
    ```
    random-graph-generator-kernel
    ```    
1. **Voila**
    
    The notebook is now ready to run!

<br/>

### Manual
1. **Create the conda environment using the `environment.yml` file included in the repository**
    ```
    conda env create -n random-graph-generator -f setup/environment.yml
    ```
1. **Activate the conda environment you just created**
    ```
    conda activate random-graph-generator
    ```
1.  **Install an iPython kernel in the new environment**
    ```
    ipython kernel install --user --name=random-graph-generator-kernel 
    ```
1. **Start Jupyter Notebook**
    ```
    jupyter notebook random_graph_generator.ipynb
    ````
1. **Select created kernel**
    
    As seen in the following image, switch the kernel to
    ```
    random-graph-generator-kernel
    ```
1. **Voila**
    
    The notebook is now ready to run!
