# Weather_Prediction

[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/mikitomi21/Weather_Prediction/blob/main/LICENSE)

***Weather_Prediction*** is an set of AI models predicting temperature based on a number of factors given in the input file.

Examplary data included in this project was borrowed from **[imgw.pl](https://danepubliczne.imgw.pl)**

Project currently contains linear and neural network models:
-   [**prenestation.ipynb**](https://github.com/mikitomi21/Weather_Prediction/blob/main/presentation.ipynb) contains linear models
-   [**pres_NeuralNetwork.ipynb**](https://github.com/mikitomi21/Weather_Prediction/blob/main/pres_NeuralNetwork.ipynb) contains neural network models

## Linear models
-   **Linear Regression**
-   **Linear Auto Regressive**
-   **Linear Auto Regressive with lag**

## Neural Network models
-   **Feedforward artificial neural networks**

## Inserting your own data
<ol typ="1">
<li>In order to imitate our environment, we recomend installing Visual Studio Code with Jupyter extension. Make sure you have the required libraries installed.</li>
<li>Download raw data from <a href="https://danepubliczne.imgw.pl">imgp.pl</a>.</li>
<li>Unzip files to folders in data as you wish(in our example, we sorted individual .csv files into folders describing years). Use <a href="https://github.com/mikitomi21/Weather_Prediction/blob/main/csv_converter.ipynb">csv_converter.ipynb</a> in combination with getCSVFiles functions to merge them together into one resulting file <a href="https://github.com/mikitomi21/Weather_Prediction/blob/main/result.csv">result.csv</a>.</li>
<li>Open one of files containing presentations of AI models and run the program with Jupyter.</li>
<li>Notice the content of file change after running the program. Graphs changed according to your input files. Voilà!</li>
</ol>

## Libraries used in this proejct
<ul>
<li>statsmodels</li>
<li>matplotlib</li>
<li>pandas</li>
<li>numpy</li>
<li>csv</li>
<li>os</li>
</ul>
