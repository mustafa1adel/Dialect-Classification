# Project: Dialect-Classification
Building a classifier that classifies the dialects of 18 Arabic countries. 

### Project Overview
Arabic is one of the most widely spoken languages in the world, with 28 nations claiming it as their official language. The population of the Arab world is around 369.8 million people, with a geographical area stretching from Morocco to Dubai. With such a large space to cover, it’s no wonder that this language has so many different and important dialects.

The most common version of Arabic, adapted specifically for standardized speech and writing, is Modern Standard Arabic. MSA is used in writing and most formal speech throughout the Arabic world and serves as the linguistic glue of this incredibly diverse cultural landscape. This language has been spoken for centuries, resulting in a split from Classical Arabic. Classical Arabic is commonly found in religious texts like Qu’ran and has been preserved since the 7th century.

However, in this project We will work on an automatically collected dataset of tweets belonging to a wide range of country-level Arabic dialects —covering 18 different countries in the Middle East and North
Africa region. this dataset was collected and represented in [Arabic Dialect Identification in the Wild](https://arxiv.org/pdf/2005.06557.pdf)


### Install

This project requires **Python 3** and the following Python libraries installed:

- [NumPy](http://www.numpy.org/)==1.19.5
- [Pandas](http://pandas.pydata.org)==1.1.2
- [scikit-learn](http://scikit-learn.org/stable/)
- [Pickle](https://docs.python.org/3/library/pickle.html)==4.0
- [Flask](https://flask.palletsprojects.com/)

**Notice**
	You may also need to have software installed to run and execute an [iPython Notebook](http://ipython.org/notebook.html) or install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project.

### Code

Template code is provided in the `Dialect_classification.ipynb` notebook file as a whole project and it is divided into 3 python scripts `00_retrieve_data.py`, `01_data_preprocessing.py`, and `02_evaluating_models.py`. You will also find some functions in `helper.py` Python file but unfortunately I didn't provide the datasets here in this repo but you are very welcome to go through the project and check the process.

### Run

In a terminal or command window, navigate to the top-level project directory `Dialect-Classification/` (that contains this README) and run one of the following commands:

```bash
ipython notebook Dialect_classification.ipynb
```  
or
```bash
jupyter-notebook Dialect_classification.ipynb
```

This will open the iPython Notebook software and project file in your browser.




