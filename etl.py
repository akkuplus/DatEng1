import glob
import json
import os
import pandas as pd
import psycopg2

from sql_queries import *


def process_song_file(cur, filepath):
    """Import and insert song data for a given file."""

    song_data, artist_data = None, None
    try:
        # open a song file
        with open(filepath) as fio:
            list_of_dicts = [  # wee need a root -> wrap in list
                json.load(fio)
            ]
            df = pd.DataFrame.from_records(list_of_dicts)

        # extract data
        song_data = [tuple(x) for x in df.loc[:, ["song_id", "title", "artist_id", "year", "duration"]].to_numpy()]
        artist_data = [tuple(x) for x in df.loc[:, ["artist_id",
                                                     "artist_name",
                                                     "artist_location",
                                                     "artist_latitude",
                                                     "artist_longitude"]].to_numpy()
        ]

        # insert record
        cur.executemany(song_table_insert, song_data)
        cur.executemany(artist_table_insert, artist_data)

    except Exception as ex:
        print(f"Error inserting track: file: {filepath}, {artist_data}, song: {song_data}, Error: {ex}")
    return


def process_log_file(cur, filepath):
    """Import and insert logfile data for a given file."""
    try:
        # open log file
        list_of_dicts = [
            json.loads(line) for line in open(filepath, 'r')
        ]
        df = pd.DataFrame.from_records(list_of_dicts)

        # filter by NextSong action
        df = df.loc[df.page == "NextSong"]

        # convert timestamp column to datetime
        df["ts"] = pd.to_datetime(df["ts"], unit="ms")

        # insert time data records
        time_data = [(r, r.hour, r.day, r.weekofyear, r.month, r.year, r.weekday())
                     for r in df["ts"]]

        column_labels = ["Timestamp", "Hour", "Day", "Weekofyear", "Month", "Year", "Weekday"]
        time_df = pd.DataFrame(time_data, columns=column_labels)

        for i, row in time_df.iterrows():
            cur.execute(time_table_insert, row.to_list())

        # load user table
        user_df = df.loc[:, ['userId', 'firstName', 'lastName', 'gender', 'level']].drop_duplicates()

        # insert user records
        for i, row in user_df.iterrows():
            cur.execute(user_table_insert, row.to_list())

        # insert songplay records
        for index, row in df.iterrows():

            # get songid and artistid from song and artist tables
            cur.execute(song_select, (row.song, row.artist, row.length))
            results = cur.fetchone()

            if results:
                songid, artistid = results
            else:
                songid, artistid = None, None

            # insert songplay record
                # if no match (song title, artist name, song length) exists, insert NONE as ID for in table <songplays>
            songplay_data = (row.ts, row.userId, row.level, songid, artistid, row.sessionId, row.location, row.userAgent)
            cur.execute(songplay_table_insert, songplay_data)
    except Exception as ex:
        print(f"Error inserting log: file: {filepath}, Error: {ex}")
    return


def process_data(cur, conn, filepath, func):
    """Process files in (sub-)directories using a given function.
    1) Scan for files in the directories.
    2) Execute function (to import and insert) for given data types / data structure."""

    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root, '*.json'))
        for f in files:
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    """This module import data into a SQL schema.
    1) connects to a database.
    2) import and insert song data.
    3) import and insert logfile data."""

    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()
