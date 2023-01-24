import sqlite3

__author__ = 'agam'


class User(object):
    def __init__(self, id, username, email, password, is_logged,
    saved_playlists, liked_songs, average_duration):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.is_logged = is_logged
        self.saved_playlists = saved_playlists
        self.liked_songs = liked_songs
        self.average_duration = average_duration

    def __str__(self):
        return f'User: {self.id}\n' \
               f'username: {self.username}\n' \
               f'email: {self.email}\n' \
               f'password: ***\n' \
               f'logged rn?: {self.is_logged}\n' \
               f'saved playlists: {self.saved_playlists}\n' \
               f'liked songs: {self.liked_songs}\n' \
               f'average duration: {self.average_duration}'




class UsersORM():
    def __init__(self):
        self.conn = None  # will store the DB connection
        self.cursor = None  # will store the DB connection cursor

    def open_DB(self):
        """
        will open DB file and put value in:
        self.conn (need DB file name)
        and self.cursor
        """
        try:
            self.conn = sqlite3.connect('Users.db')
            self.current = self.conn.cursor()
        except Exception as e:
            print(e)

    def close_DB(self):
        self.conn.close()

    def commit(self):
        self.conn.commit()

    def table_exists(self, table_name):
        self.open_DB()
        result = self.current.execute(f"PRAGMA table_info({table_name})").fetchall()
        self.close_DB()
        if len(result) > 0:
            return True
        else:
            return False

    def create_users_table(self):
        self.open_DB()
        self.current.execute("""
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                email TEXT NOT NULL,
                password TEXT NOT NULL,
                is_logged BOOLEAN NOT NULL,
                saved_playlists INTEGER NOT NULL,
                liked_songs INTEGER NOT NULL,
                average_duration INTEGER NOT NULL
            );
        """)
        self.conn.commit()
        self.close_DB()

    def get_user(self, id):
        '''
        returns a user by the id provided
        :param id: a user's id
        :return: all details about a user
        '''
        if not self.table_exists("users"):
            print("Error: Table 'users' does not exist.")
            return None
        self.open_DB()
        user = None
        sql = f"SELECT * FROM users WHERE id == '{id}' ;"
        res = self.current.execute(sql)
        user = res.fetchall()
        self.close_DB()
        return user

    def get_all_users(self):
        '''
        get all the users in the database
        :return: all the users details
        '''
        self.open_DB()
        users = []
        sql = "SELECT * " \
              "FROM users;"
        res = self.current.execute(sql)
        users = res.fetchall()
        self.close_DB()
        return users

    def user_exists(self, entered_value):
        '''
        checks if user exists in the db
        :param entered_value: username/email address
        :return: true/false value
        '''
        self.open_DB()
        answer = None
        sql = "SELECT id " \
              f"FROM users WHERE username == '{entered_value}' OR email == '{entered_value}' ;"
        res = self.current.execute(sql)
        answer = res.fetchall()
        self.close_DB()
        if answer == None:
            return False
        return True

    def login_user(self, entered_value, password ):
        '''
        gets a username/mail addr and an entered password and checks if the user is valid
        :param entered_value: a username/mail
        :param password: the entered password after hash
        :return: are the credentials given true
        '''
        exists = self.user_exists(entered_value)
        if not exists:
            return False, '001'
        self.open_DB()
        answer = []
        sql = "SELECT id, password " \
            f"FROM users WHERE username == '{entered_value}' OR email == '{entered_value}' ;"
        res = self.current.execute(sql)
        answer = res.fetchall()
        if password == answer[0][1]:
            sql = "UPDATE users " \
                  f"SET is_logged = 'yes' " \
                  f" WHERE id == '{answer[0]}' ;"
            res = self.current.execute(sql)
            self.close_DB()
            return True, answer[0]
        else:
            self.close_DB()
            return False, '001'

    def get_logged_info(self,id):
        '''
        after login, get the info of a
        :param id: the user's id
        :return: all information about the user
        '''
        self.open_DB()
        answer = []
        sql = "SELECT * " \
              f"FROM users WHERE id == '{id}' ;"
        res = self.current.execute(sql)
        answer = res.fetchall()
        self.close_DB()
        return answer

    def get_saved_playlists(self, id):
        '''
        returns the id's of the saved playlists the user currently has
        :param id: the user's id
        :return:a list of the saved playlists id's
        '''
        self.open_DB()
        sql = f"SELECT saved_playlists FROM users WHERE id == '{id}';"
        res = self.current.execute(sql)
        playlists = []
        students_in_grade = res.fetchall()
        self.close_DB()
        return playlists

    def get_current_logged(self):
        '''
        returns all users's ids of the users who are currently connected and logged
        :return: ids of logged users
        '''
        self.open_DB()
        sql = f"SELECT id FROM users WHERE is_logged = 'yes';"
        res = self.current.execute(sql)
        playlists = []
        students_in_grade = res.fetchall()
        self.close_DB()
        return playlists
    def log_out(self,id):
        self.open_DB()
        sql = "UPDATE users " \
              f"SET is_logged = 'no' " \
              f"WHERE id == '{id}' ;"
        res = self.current.execute(sql)
        self.close_DB()

def main():
    db = UsersORM()
    #db.create_users_table()
    users_lst = db.get_user(1)
    print(users_lst)



if __name__ == "__main__":
    main()
