# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE songplays(songplay_id serial, 
                                                    start_time timestamp, 
                                                    user_id int, 
                                                    level varchar, 
                                                    song_id varchar, 
                                                    artist_id varchar, 
                                                    session_id int, 
                                                    location varchar, 
                                                    user_agent varchar,
                                                    
                                                    PRIMARY KEY(songplay_id)
                                                  )""")

user_table_create = ("""CREATE TABLE users(user_id int, 
                                            first_name varchar, 
                                            last_name varchar,
                                            gender varchar, 
                                            level varchar,
                                            
                                            PRIMARY KEY(user_id) )""")

song_table_create = ("""CREATE TABLE songs(song_id varchar, 
                                            title varchar, 
                                            artist_id varchar, 
                                            year int, 
                                            duration float,
                                            
                                            PRIMARY KEY(song_id))""")

artist_table_create = ("""CREATE TABLE artists(artist_id varchar, 
                                                name varchar, 
                                                location varchar, 
                                                latitude varchar, 
                                                longitude varchar,
                                                
                                                PRIMARY KEY (artist_id) )""")

time_table_create = ("""CREATE TABLE times(start_time timestamp, 
                                            hour int, 
                                            day int, 
                                            week int, 
                                            month int, 
                                            year int, 
                                            weekday int,
                                            
                                            PRIMARY KEY(start_time) )""")

# INSERT RECORDS
# row.ts, row.userId, row.level, songid, artistid, row.sessionId, row.location, row.userAgent
songplay_table_insert = ("""INSERT INTO songplays(start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)\
                            VALUES(%s, %s, %s, %s, %s, %s, %s, %s)
                            ON CONFLICT DO NOTHING;""")

user_table_insert = ("""INSERt INTO users(user_id, first_name, last_name, gender, level)
                        VALUES(%s, %s, %s, %s, %s)
                        ON CONFLICT DO NOTHING;""")

song_table_insert = ("""INSERT INTO songs(song_id, title, artist_id, year, duration) \
                        VALUES(%s, %s, %s, %s, %s)
                        ON CONFLICT DO NOTHING;""")

artist_table_insert = ("""INSERT INTO artists(artist_id, name, location, latitude, longitude) \
                        VALUES(%s, %s, %s, %s, %s)
                        ON CONFLICT DO NOTHING;""")
#artist_table_insert = ("""INSERT INTO artists(artist_id, name, location, latitude, longitude) \
#                        VALUES(%s, %s, %s, %s, %s)
#                        ON CONFLICT (artist_id) DO UPDATE SET
#                            name = artists.name || ';' || EXCLUDED.name,
#                            location = artists.location || ';' || EXCLUDED.location,
#                            latitude = artists.latitude || ';' || EXCLUDED.latitude,
#                            longitude = artists.longitude || ';' || EXCLUDED.longitude""")

time_table_insert = ("""INSERT INTO times(start_time, hour, day, week, month, year, weekday) \
                        VALUES(%s, %s, %s, %s, %s, %s, %s)
                        ON CONFLICT DO NOTHING;""")

# FIND SONGS
song_select = ("""
SELECT * from (
    SELECT * FROM songs as sg
    JOIN artists as ar ON sg.artist_id = ar.artist_id) as tracks
WHERE (tracks.name = %s
    AND tracks.title = %s
    AND tracks.duration = %s)
""")

# QUERY LISTS
create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]
