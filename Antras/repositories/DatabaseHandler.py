import sqlite3
from sqlite3 import Error


database = "local.db"


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None


def get_users():
    """
    Get all users
    :param id: if not provided returns all users
    :return:
    """
    conn = create_connection(database)
    cur = conn.cursor()

    sql = "SELECT * FROM User"

    cur.execute(sql)
    return cur.fetchall()


def get_user(id):
    """
    Get user by id
    :param id:
    :return:
    """
    conn = create_connection(database)
    cur = conn.cursor()

    sql = "SELECT * FROM User WHERE Id=?"

    cur.execute(sql, (id,))
    return cur.fetchone()


def get_user_notes(id):
    """
    Get user notes
    :param id:
    :return:
    """

    conn = create_connection(database)
    cur = conn.cursor()

    sql = "SELECT * FROM UserNotes WHERE UserId=?"

    cur.execute(sql, (id,))
    return cur.fetchall()


def add_user(user):
    """
    Add a single user
    :param user: tuple of FirstName LastName and Email
    :return:
    """
    conn = create_connection(database)
    cur = conn.cursor()

    sql = ''' INSERT INTO User(FirstName, LastName, Email) VALUES(?,?,?) '''

    try:
        cur.execute(sql, user)
        conn.commit()
        return cur.lastrowid
    except Error as e:
        return None


def add_user_note(user_note):
    """
    Add a user note
    :param user_note:
    :return:
    """
    conn = create_connection(database)
    cur = conn.cursor()

    sql = ''' INSERT INTO UserNotes(UserId, Note) VALUES(?,?) '''

    cur.execute(sql, user_note)
    conn.commit()


def update_user(user, id):
    """
    Update a user
    :param id: user id
    :param user: tuple of FirstName LastName and Email
    :return:
    """

    conn = create_connection(database)
    cur = conn.cursor()

    try:
        sql = '''   UPDATE User 
                    SET FirstName=?,
                    LastName=?,
                    Email=?
                    WHERE Id=?'''

        cur.execute(sql, user + (id,))
        conn.commit()
        return cur.lastrowid
    except Error as e:
        print(e)
        return None


def update_user_note(old_title, new_title):
    """
    Updates user note
    :param old_title:
    :param new_title:
    :return:
    """
    conn = create_connection(database)
    cur = conn.cursor()

    try:
        # Getting user
        sql = ''' SELECT * FROM UserNotes WHERE Note=?'''

        cur.execute(sql, (old_title,))
        user_to_update = cur.fetchone()

        user_note = (new_title, user_to_update[0])

        sql = '''   UPDATE UserNotes 
                    SET Note=?
                    WHERE Id=?'''

        cur.execute(sql, user_note)
        conn.commit()
        return cur.lastrowid
    except Error as e:
        print(e)
        return None


def delete_user(id):
    """
    Delete
    :param id:
    :return:
    """

    conn = create_connection(database)
    cur = conn.cursor()

    sql = ''' DELETE FROM User WHERE Id=?'''

    try:
        cur.execute(sql, (id,))
        conn.commit()
    except Error as e:
        print(e)


def delete_user_note(user_note):
    """
    Delete user note
    :param user_note:
    :return:
    """

    conn = create_connection(database)
    cur = conn.cursor()

    sql = ''' DELETE FROM UserNotes WHERE UserId=? AND Note=?'''

    try:
        cur.execute(sql, user_note)
        conn.commit()
    except Error as e:
        print(e)
