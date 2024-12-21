# Book Recommendation System with Streamlit
This repository contains the implementation of a Book Recommendation System built using Streamlit and machine learning. The project leverages Natural Language Processing (NLP) techniques to analyze book metadata, summaries, and user preferences to deliver personalized book recommendations.

# Features
	Personalized Recommendations: Suggests books based on users’ interests and reading habits.
	•	Content-Based Filtering: Analyzes book summaries, genres, and reviews using NLP to match user preferences.
	•	Interactive Interface: Provides an easy-to-use, dynamic UI with Streamlit for exploring book suggestions.
	•	Data Visualization: Offers insights and trends through visual analytics.
	•	Extensible: Modular structure allows for easy addition of new features or datasets.

## Usage 🛹
	1.	Launch the app using Streamlit. The main dashboard will load, displaying options for book recommendations and an “About” page.
	2.	Use the sidebar to input your preferences or explore different book categories.
	3.	View real-time recommendations and insights on user interactions.


- **streamlit+API_intro**: A branch with a working Streamlit application with a notebook giving a quick introduction to API and JSON.


### Environment 🌀 and Installation 👩🏽‍🔧👨🏽‍🔧
#### Prerequisite
+ Python 3.11.3 or above up to 3.11.6 ([pyenv](https://github.com/pyenv/pyenv#simple-python-version-management-pyenv) for Python Version Management is used but feel free to use any other tool)
+ Virtual environment (The module venv from python is used but you can use any other tool)


For __MacOs__/__Linux__ users
```bash
# Sets the local Python version to 3.11.3 using pyenv
pyenv local 3.11.3 
# Create a Virtual Environment named .streamlit_env using venv
python -m venv .streamlit_env
# Activate the Virtual Environment
source .streamlit_env/bin/activate
# Install Streamlit and Additional Libraries
pip install -r requirements.txt
```

For __Windows__ users with PowerShell CLI


```bash
# Sets the local Python version to 3.11.3 using pyenv
pyenv local 3.11.3 
# Create a Virtual Environment named .streamlit_env using venv
python -m venv .streamlit_env
# Activate the Virtual Environment
.streamlit_env\Scripts\Activate.ps1
# Install Streamlit and Additional Libraries
pip install -r requirements.txt
```

For __Windows__ users with GIT-BASH CLI


```bash
# Sets the local Python version to 3.11.3 using pyenv
pyenv local 3.11.3 
# Create a Virtual Environment named .streamlit_env using venv
python -m venv .streamlit_venv
# Activate the Virtual Environment
source .streamlit_venv/Scripts/activate
# Install Streamlit and Additional Libraries
pip install -r requirements.txt
```


#### 🧪 Test Streamlit Installation 👨🏽‍🔧👩🏽‍🔧
You can check if Streamlit is installed correctly and run a sample app with the following command:
```bash
streamlit hello
```
This should open a Streamlit web app in your default web browser. 


## License
[The MIT license](LICENSE)

## Acknowledgments
	•	Streamlit Community: For their great support and documentation.
	•	Open Source Libraries: For powering the core functionalities.
	•	Special thanks to everyone who contributed to this project!


## Contributing
Contributions are welcome!

## Happy recommending!😊
