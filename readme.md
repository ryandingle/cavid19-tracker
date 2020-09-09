# INSTRUCTIONS
Please user python 3.8 for this application to and avoid some issues on library used.
This application contains a web application part to view the data in a table UI.

The main scripts of this application is inside the folder covid.
`models.py`
`views.py`

# What is the data processed by this application ?
The data processed by this application is a dataset contains covid 19 information for all countries around the world.
This will help to any company to have some research analysis based on the things related for health.

# REQUIREMENTS
python 3.8.x / can try also for python 3.6 and 3.7
virtualenv
mysql database installed
mysql connector
pip

# NOTES
Please create a database name for this application and put it in the .env variable

# CONFIG
open `.env` file and edit the variable values 
DB_NAME=your_database_name
DB_USER=your_database_username
DB_PASSWORD=your_database_password
DB_HOST=your_database_hostname
DB_PORT=your_database_port

# INSTALLATION
Before proceeding please make sure the config is setup and the database name is present
run the script install.sh `$ bash install.sh` to create a virtualenv and install needed python packages

# HOW TO RUN
Please make sure you run the install.sh before proceeding into this step
run the script run.sh `$ bash run.sh` to start the application and open your browser address `http://localhost:8000` to see the running app via web view.