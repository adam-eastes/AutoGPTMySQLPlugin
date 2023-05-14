"""This module contains functions for interacting with the a network mySQL server."""
import pandas as pd
import os

from atproto import Client
import mysql.connector


def isConfigSetup() -> bool:
    return True if os.getenv("MYSQL_HOST") and os.getenv("MYSQL_USER") and os.getenv("MYSQL_PASS") else False

def getHost():
    mysql_host = os.getenv("MYSQL_HOST")
    if not mysql_host:
        return "Error: mySQL query not made. MYSQL_HOST not set in environment."
    return mysql_host
    
def getUser():
    mysql_user = os.getenv("MYSQL_USER")
    if not mysql_user:
        return "Error: mySQL query not made. MYSQLMYSQL_USER_HOST not set in environment."
    return mysql_user

def getPass():
    mysql_pass = os.getenv("MYSQL_PASS")
    if not mysql_pass:
        return "Error: mySQL query not made. MYSQL_PASS not set in environment."
    return mysql_pass

def mysql_query(query: str) -> str:
    """Send an email

    Args:
        query (str): the MySQL query
    Returns:
        str: Any error messages or return from mySQL
    """
    mysql_host = getHost()

    mysql_user = getUser()

    mysql_pass = getPass()

    # Connect to server
    cnx = mysql.connector.connect(
        host=mysql_host,
        port=3306,
        user=mysql_user,
        password=mysql_pass)

    # Get a cursor
    cur = cnx.cursor()

    # Execute a query
    try:
        cur.execute(query)
    except mysql.connector.Error as err:
        return(f'Error: {err}')

    # Fetch one result
    res = cur.fetchone()

    # Close connection
    cnx.close()

    return("MySQL database returned: {0}".format(rres))

    