#Data Modeling With PostGreSQL

## Summary

The project conducts ETL operations on JSON files and stores data in a Postgres database.   
This README summarized the underlying the data modeling project to collect and transfer the data into a star-schema.

## Data
The data sets consists of the subsets

- Song dataset (`subdir data/song_data`), that contains of JSON files:  

        {
        "num_songs": 1, 
        "artist_id": "AR8ZCNI1187B9A069B", 
        "artist_latitude": null, 
        "artist_longitude": null, 
        "artist_location": "", 
        "artist_name": "Planet P Project", 
        "song_id": "SOIAZJW12AB01853F1", 
        "title": "Pink World", 
        "duration": 269.81832, 
        "year": 1984
        }
  
- Log dataset (`subdir data/log_data`), that contains of JSON files:
  
        {
        "artist":"N.E.R.D. FEATURING MALICE",
        "auth":"Logged In",
        "firstName":"Jayden",				
        "gender":"M",						
        "itemInSession":0,
        "lastName":"Fox",					
        "length":288.9922,					
        "level":"free",							
        "location":"New Orleans-Metairie, LA",	
        "method":"PUT",				
        "page":"NextSong",
        "registration":1541033612796.0,
        "sessionId":184,
        "song":"Am I High (Feat. Malice)",		
        "status":200,
        "ts":1541121934796,						
        "userAgent":"\"Mozilla\/5.0 (Windows NT 6.3; WOW64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/36.0.1985.143 Safari\/537.36\"", '-> user_table
        "userId":"101" 
        }

## Prerequisites

The project requires a *Python* environment having the packages (see requirements.txt):  
> pandas,  
> pyscopg2,  
> jupyterlab  

and a *Postgres database* (database access: host=127.0.0.1, database_name=sparkifydb, user_login=student, user_password=student; this information is only provided for demo purposes).

## Data Model

### Table songplays  

Field | Type | Attribute
---   | ---  | ---
songplay_id | serial | Primary key
start_time | timestamp
user_id | int
level | varchar 
song_id | varchar 
artist_id | varchar 
session_id | int 
location | varchar
user_agent | varchar


### Table users

Field | Type | Attribute
---   | ---  | --- 
user_id | int | Primary key
first_name | varchar
last_name| varchar
gender| varchar 
level| varchar
                                            



### Table songs

Field | Type | Attribute
---   | ---  | ---  
song_id | varchar | Primary key
title | varchar 
artist_id | varchar 
year | int 
duration | float
                                            


### Table artists

Field | Type | Attribute
---   | ---  | ---
artist_id | varchar | Primary key 
name | varchar 
location | varchar 
latitude | varchar 
longitude | varchar
                                                
                                                

### Table times

Field | Type | Attribute
---   | ---  | ---
start_time | timestamp |  Primary key
hour | int |  
day | int |
week | int |
month | int |
year | int |
weekday | int |
                                            
                                            


## Getting Started
A running Python environment is assumed.  
First, connect to the DBMS and create the Sparkify databases:  

    python create_tables.py  

Second, execute the ETL operations and load the data into the databases:  
    To load data into the Sparkify database run the following command:

    python etl.py

Finally, validate the imported data using the JUPYTER notebook  
    
    `test.ipynb`.  
