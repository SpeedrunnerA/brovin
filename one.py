
import sqlite3

conn = sqlite3.connect("university.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS students(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT,
               age INTEGER,
               major TEXT
               )
''')

cursor.execute('''CREATE TABLE IF NOT EXISTS courses(
               course_id INTEGER PRIMARY KEY AUTOINCREMENT,
               course_name TEXT,
               instructor TEXT
               )
''')

cursor.execute('''CREATE TABLE IF NOT EXISTS student_courses (student_id INTEGER,course_id INTEGER, FOREIGN KEY (student_id) REFERENCES students(id), FOREIGN KEY (course_id) REFERENCES courses(course_id),PRIMARY KEY (student_id, course_id))''')

while True:
    print("1. Додати нового студента")
    print("2. Додати новий курс")
    print("3. Показати список студентів")
    print("4. Показати курси")
    print("5. Зареєструвати на курс")
    print("6. Показати студентів на курсі")
    print("7. Вихід")

    choice = input("Оберіть від 1 до 7")

    if choice =="1":
        name= input("Введіть імя")
        age= int(input("Введіть вік"))
        major = input("Введіть спеціальність")
        cursor.execute('INSERT INTO students (name, age, major) VALUES (?, ?, ?)', (name, age, major))
        conn.commit()
    elif choice == "2":
        course_name = input("Введіть назву курсу")
        instructor = input("Введіть ім'я викладача")
        cursor.execute('INSERT INTO courses (course_name, instructor) VALUES (?, ?)', (course_name, instructor))
        conn.commit()
    elif choice == "3":
        cursor.execute('SELECT * FROM students')
        students = cursor.fetchall()
        for student in students:
            print(student)
            for s in student:
                print(s[0], s[1], s[2], s[3])
        else:
            print("Список студентів порожній")
    elif choice == "4":
        cursor.execute('SELECT * FROM courses')
        courses = cursor.fetchall()
        if not courses:
            print("Список курсів порожній")
        for course in courses:
            print(course[0], course[1], course[2])
    elif choice == "5":
        student_id = int(input("Введіть ID студента"))
        course_id = int(input("Введіть ID курсу"))
        cursor.execute('INSERT INTO student_courses (student_id, course_id) VALUES (?, ?)', (student_id, course_id))
        conn.commit()
    elif choice == "6":
        course_id = int(input("Введіть ID курсу"))
        cursor.execute('SELECT students.id, students.name FROM students JOIN student_courses ON students.id = student_courses.student_id WHERE student_courses.course_id = ?', (course_id,))
        enrolled_students = cursor.fetchall()
        if not enrolled_students:
            print("На курсі немає зареєстрованих студентів")
        else:
            for student in enrolled_students:
                print(student[0], student[1])
    elif choice == "7":
        print("Вихід з програми")
        break
    else:
        print("Невірний вибір, спробуйте ще раз")
conn.close()