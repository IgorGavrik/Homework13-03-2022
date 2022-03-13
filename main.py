# 1. Создать таблицу
# 2. Добавить 5 записей
# 3. Получить всех пользователей с вашим
# именем
# 4. Получить всех пользователей младше 25
# 5. Получить всех пользователей в возрасте
# от 15 до 18




from sqlalchemy import create_engine

e = create_engine("sqlite:///table.db", echo=True)
e.execute("""
    CREATE TABLE user (
        id integer primary key autoincrement,
        firstname varchar(255),
        lastname varchar(255),
        age integer
    )
""")
e.execute("""
    INSERT INTO user (firstname, lastname, age)
    VALUES ("Igor", "Gavrik", "43"),
    ("Elena", "Kitun", "23"),
    ("Darya", "Gavrik", "10"),
    ("Kristina", "Chaikovskaya", "18"),
    ("Simona", "Vertinskaya", "16")
""")
result = e.execute("""SELECT * FROM user
    WHERE firstname = 'Igor' and lastname = 'Gavrik'
    WHERE age < 25
    WHERE age > 15 and age < 18
""")
for user in result:
    print(user)