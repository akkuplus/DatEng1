# Data Modeling With PostGreSQL

## Summary

The demo project conducts ETL operations on JSON files and stores data in a Postgres database.   
This README summarized the underlying project to collect and transfer the data into a star-schema.

## Data
The data sets consists of two subsets of files:

- Song dataset (in subdirectory `data/song_data`) contains files in JSON, like  

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
  
- Log dataset (in subdirectory `data/log_data`) contains files in JSON, like
  
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

## Data Model

### Table songplays  

Field | Type | Attribute
---   | ---  | ---
songplay_id | serial | Primary key
start_time | timestamp | NOT NULL
user_id | int | NOT NULL
level | varchar 
song_id | varchar 
artist_id | varchar 
session_id | int | NOT NULL
location | varchar
user_agent | varchar


### Table users

Field | Type | Attribute
---   | ---  | --- 
user_id | int | Primary key
first_name | varchar
last_name | varchar
gender | varchar 
level | varchar


### Table songs

Field | Type | Attribute
---   | ---  | ---  
song_id | varchar | Primary key
title | varchar | NOT NULL
artist_id | varchar | NOT NULL
year | int 
duration | float | NOT NULL
                                            


### Table artists

Field | Type | Attribute
---   | ---  | ---
artist_id | varchar | Primary key 
name | varchar | NOT NULL
location | varchar 
latitude | varchar 
longitude | varchar
                                                
                                                

### Table times

Field | Type | Attribute
---   | ---  | ---
start_time | timestamp |  Primary key
hour | int | NOT NULL
day | int | NOT NULL
week | int | NOT NULL
month | int | NOT NULL
year | int | NOT NULL
weekday | int | NOT NULL
                                            
               
## Star schema

Fact table | Dimensional table
---   | ---  
songplays | artists
. | songs
. | times
. | users


## Prerequisites

The project requires a *Python* environment having the packages (see requirements.txt):  
> pandas,  
> pyscopg2,  
> jupyterlab  

and a *Postgres database* (database access: host=127.0.0.1, database_name=sparkifydb, user_login=student, user_password=student; this information is only provided for demo purposes).


## Getting Started
A running Python environment is assumed.  
First, connect to the DBMS and create the Sparkify databases:  

    python create_tables.py  

Second, execute the ETL operations and load the data into the databases:  
    To load data into the Sparkify database run the following command:

    python etl.py

Finally, validate the imported data using the JUPYTER notebook  
    
    test.ipynb.  
