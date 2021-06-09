import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

from sql_queries import create_table_queries, drop_table_queries


def create_database(host="127.0.0.1", dbname="postgres", user="student", password="student", external_postgres_dbs=False):
    """
    - Creates and connects to the sparkifydb
    - Returns the connection and cursor to sparkifydb
    """
    
    # connect to default database
    if external_postgres_dbs:
        conn_details = {"host":"tai.db.elephantsql.com",
                        "dbname":"xnzxiluz",
                        "user":"xnzxiluz",
                        "password":"Ygv_W6DvmeC6Jtbo1VxhrQ4Yjgk2z2fd"
        }
        conn = psycopg2.connect(**conn_details)
        conn.set_session(autocommit=True)
        cur = conn.cursor()

    else:
        conn = psycopg2.connect(host=host, dbname=dbname, user=user, password=password)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = conn.cursor()

        # create sparkify database with UTF8 encoding
        # Before, give user student permission:
            # postgres =  # "ALTER USER student CREATEDB CREATEROLE LOGIN;"
        conn.commit()
        cur.execute("DROP DATABASE IF EXISTS sparkifydb")

        cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")
        conn.commit()

        # close connection to default database
        conn.close()

        # connect to sparkify database
        conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
        conn.set_session(autocommit=True)
        cur = conn.cursor()
    
    return cur, conn


def drop_tables(cur, conn):
    """
    Drops each table using the queries in `drop_table_queries` list.
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    Creates each table using the queries in `create_table_queries` list. 
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    - Drops (if exists) and Creates the sparkify database. 
    
    - Establishes connection with the sparkify database and gets
    cursor to it.  
    
    - Drops all the tables.  
    
    - Creates all tables needed. 
    
    - Finally, closes the connection. 
    """
    cur, conn = create_database()
    
    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
