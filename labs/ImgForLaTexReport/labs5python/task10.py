def task_10():
    students = [("Анна", [5, 4, 5]), ("Иван", [3, 4, 4]), ("Мария", [5, 5, 5])]
    average_grades = {}

    for name, grades in students:
        average = sum(grades) / len(grades)
        average_grades[name] = average

    print("Словарь со средними оценками:")
    print(average_grades)


    best_student = None
    best_average = 0

    for name, average in average_grades.items():
        if average > best_average:
            best_average = average
            best_student = name

    print(f"\nСтудент с наибольшей средней оценкой:")
    print(f"Имя: {best_student}, Средний балл: {best_average}")