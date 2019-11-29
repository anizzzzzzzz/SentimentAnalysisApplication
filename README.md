# Sentiment Analysis Application

This is a simple sentiment analysis application developed using movie-review data. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine. 

### Technologies Used
* **Flask** : Python framework for making Webapp

### Prerequisities
Need python [any version].

### Installation
```sh
$ git clone https://github.com/anizzzzzzzz/SentimentAnalysisApplication.git
$ cd SentimentAnalysisApplication/
```

### Creating Virtual Environment
To create a virtual environment, go to your project's directory and run virtualenv.

#### On macOS and Linux:
``` 
python3 -m virtualenv venv
``` 
#### On windows:
``` 
py -m virtualenv venv
```
Note : The second argument is the location to create the virtualenv. Generally, you can just create this in your project and call it venv.
[ virtualenv will create a virtual Python installation in the venv folder.]

### Activating Virtual Environment
Before you can start installing or using packages in your virtualenv, you'll need to activate it.

#### On macOS and Linux:
```
source venv/bin/activate
```

#### On windows:
```
.\venv\Scripts\activate
```

#### Confirming virtualenv by checking location

##### On macOS and Linux:
```
which python
```
Output : .../venv/bin/python

##### On windows:
```
where python
```
Output : .../venv/bin/python.exe


### Installing packages with pip
```
pip install -r requirements.txt
```

### Creating and Initializing SQLite db 
The predicted data is stored in database for future use.  
Note : Open a terminal/comman prompt on source folder and run these commands.
```
$ flask db init 
$ flask db upgrade
$ flask db migrate -m "initializing the db"
$ flask db upgrade
```

## Running Web App
Get inside the project directory and enter the following command line code at terminal for Linux/MacOS or command prompt for Windows.
```
flask run
```
