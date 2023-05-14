# Weather_Prediction

[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/mikitomi21/Weather_Prediction/blob/main/LICENSE)

***Weather_Prediction*** is a set of AI models predicting temperature based on a number of factors given in the input file.

Examplary data included in this project was borrowed from **[imgw.pl](https://danepubliczne.imgw.pl)**

Project currently contains linear and neural network models:
-   [**pres_linear_models.ipynb**](https://github.com/mikitomi21/Weather_Prediction/blob/main/pres_linear_models.ipynb) contains linear models
-   [**pres_neural_network.ipynb**](https://github.com/mikitomi21/Weather_Prediction/blob/main/pres_neural_network.ipynb) contains neural network model

# Models
<h3>Linear:</h3>
<ul>
<li>Linear Regression</li>
<li>Linear Auto Regressive</li>
<li>Linear Auto Regressive with lag</li>
</ul>

<h3>Neural Network:</h3>
<ul>
<li>Feedforward artificial neural networks</li>
</ul>

## Description of dataset
<b>Data from cities:</b>
<ul>
<li>GDANSK</li>
<li>WARSZAWA</li>
<li>BIALYSTOK</li>
<li>BIELSKO-BIALA</li>
<li>SZCZECIN</li>
<li>WROCLAW</li>
</ul>

<b>Features used:</b>
<ul>
<li>Minimum Temperature</li>
<li>Maximum Temperature</li>
<li>Average Temperature</li>
<li>Sum Of Falls</li>
<li>Kind Of Falls</li>
<li>Cloudiness</li>
<li>Wind Speed</li>
<li>Humidity</li>
<li>Pressure</li>
</ul>

## Inserting your own data
<ol typ="1">
<li>In order to imitate our environment, we recomend installing Visual Studio Code with Jupyter extension. Make sure you have the required libraries installed.</li>
<li>Download raw data from <a href="https://danepubliczne.imgw.pl">imgp.pl</a>.</li>
<li>Unzip files to folders in data as you wish(in our example, we sorted individual .csv files into folders describing years). Use <a href="https://github.com/mikitomi21/Weather_Prediction/blob/main/csv_converter.ipynb">csv_converter.ipynb</a> in combination with getCSVFiles functions to merge them together into one resulting file <a href="https://github.com/mikitomi21/Weather_Prediction/blob/main/result.csv">result.csv</a>.</li>
<li>Open one of files containing presentations of AI models and run the program with Jupyter.</li>
<li>Notice the content of file change after running the program. Graphs changed according to your input files. Voilà!</li>
</ol>

## Libraries used in this project
<ul>
<li>statsmodels</li>
<li>matplotlib</li>
<li>pandas</li>
<li>numpy</li>
<li>csv</li>
<li>os</li>
</ul>
