# Person Data Saving Python Programme

This project is aimed to save person data coming from HTTP JSON request on to a MySQL database.

- It can be executed by

    `python .\SavePeopleData.py`

- It will print how many records entered into database

## Configuration
- Configuration data needed for the databse is saved on `config.json` file
- These data are as follows
    - host : Database hosted url
    - user : DB user name
    - password : DB password
    - db : DB name
    - port : DB connection port

## Prerequisites
- Following modules has to be installed
    - mysql-connector-python