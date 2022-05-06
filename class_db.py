import sqlite3

class DB:
    def __init__(self):
        self.conn = sqlite3.connect("phonebook")
        self.cursor = self.conn.cursor()
    
    def execute(self, command):
        try:
            self.cursor.execute(command)
            self.conn.commit()
        except sqlite3.Error as erro:
            print(f"Error: {erro}")
    
    def create_table(self):
        try:
            self.cursor.execute(f"create table if not exists phonebook (id integer primary key autoincrement, name text not null, phone text not null, type_contact text not null)")
        except sqlite3.Error as erro:
            print(f"Error: {erro}")

    def get_filter(self, type_contact):
        try:
            self.cursor.execute(f"select * from phonebook where type_contact = '{type_contact}'")
            return self.cursor.fetchall()
        except sqlite3.Error as erro:
            print(f"Error: {erro}")
    
    def get_count(self):
        try:
            self.cursor.execute(f"select count(*) from phonebook")
            return self.cursor.fetchall()
        except sqlite3.Error as erro:
            print(f"Error: {erro}")

    def get_table(self):
        try:
            self.cursor.execute(f"select * from phonebook")
            return self.cursor.fetchall()
        except sqlite3.Error as erro:
            print(f"Error: {erro}")

    def toLocate(self, name):
        try:
            self.cursor.execute(f"select * from phonebook where name like '{name}%'")
            return self.cursor.fetchall()
        except sqlite3.Error as erro:
            print(f"Error: {erro}")

    def insert(self, name, phone, type_contact):
        try:
            self.cursor.execute(f"insert into phonebook (name, phone, type_contact) values ('{name}', '{phone}', '{type_contact}')")
            self.conn.commit()
        except sqlite3.Error as erro:
            print(f"Error: {erro}")
    
    def update(self, id, name, phone, type_contact):
        try:
            self.cursor.execute(f"update phonebook set name = '{name}', phone = '{phone}', type_contact = '{type_contact}' where id = {id}")
            self.conn.commit()
        except sqlite3.Error as erro:
            print(f"Error: {erro}")
    
    def delete(self, id):
        try:
            self.cursor.execute(f"delete from phonebook where id = {id}")
            self.conn.commit()
        except sqlite3.Error as erro:
            print(f"Error: {erro}")

    def close(self):
        self.conn.close()

if __name__ == "__main__":
    bank = DB("exemplo.db")
    bank.print_table("pessoas")
    bank.close()