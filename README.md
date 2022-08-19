## Sales Tool Project

A tool for a company to submit and review sales reports of their sales agents. <br>
This project is developed using Python, Django and Bootstrap

#### The company can do the following activities:

* Create new sales agent
*  Register the monthly sales volume for each agent (Sales Reports).
* Get a list of all Sales Agents. 
* Fetch all sales reports. 
* Get all the sales reports related to a particular Sales Agent.  

<br>

## How to install in local environment

<br>

* After cloning the repository, create virtual environment in the root directory using the following command:
```
python3 -m venv venv
```
* Activate Virtual environment by running the following command:
```
source ./venv/bin/activate 
```
* Be in the directory where `requirements.txt` file is present and run the following commands:

```
pip install -r requirements.txt
python3 manage.py runserver
```
* Open your browser and type `http://127.0.0.1:8000/home/` in the address bar

