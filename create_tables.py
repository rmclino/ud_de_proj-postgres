import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def create_database():
    """
    - Drop (if exists) existing DataBase sparkifydb and creates a new one with UTF-8 encoding
    - Create a connection and cursor to sparkifydb
    """
    
    # connect to default database
    try:
        conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=student password=student")
        conn.set_session(autocommit=True)
        cur = conn.cursor()
    
        # create sparkify database with UTF8 encoding
        cur.execute("DROP DATABASE IF EXISTS sparkifydb")
        cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")
        # close connection to default database
        conn.close()    

    except psycopg2.Error as e: 
        print("Error: Could not connect to the Postgres database")
        print(e)
    
    # connect to sparkify database
    try:
        conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
        cur = conn.cursor()  
        return cur, conn
    
    except psycopg2.Error as e: 
        print("Error: Could not connect to the Postgres database")
        print(e)
    


def drop_tables(cur, conn):
    """
    Drops each table using the queries in `drop_table_queries` list.
    """
    for query in drop_table_queries:
    
        try:
            cur.execute(query)
            conn.commit()
        except psycopg2.Error as e: 
            print("Error: Could not drop tables to the Postgres database")
            print(e)


def create_tables(cur, conn):
    """
    Creates each table using the queries in `create_table_queries` list. 
    """
    for query in create_table_queries:
        print("Created Table: {}".format(query[27:query.find('\n') - 2]))
        try:
            cur.execute(query)
            conn.commit()
        except psycopg2.Error as e: 
            print("Error: Could not create table to the Postgres database")
            print(e)


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