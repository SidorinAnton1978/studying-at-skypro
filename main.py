# Импорт из файла functions.py всех функций
from functions import *


def main():
    """ Тело программы """
    print(f'Введите номер студента: ')
    student_list = []
    for students in load_students():
        for key, values in students.items():
            if key == "pk":
                student_list.append(str(values))
    print(f'{", ".join(student_list)}')
    pk = int(input())
    if str(pk) not in student_list:
        print(f'У нас нет такого студента')
        quit()
    student = get_student_by_pk(pk)
    print(f'Студент: {student["full_name"]}')
    print(f'Знает: {", ".join(student["skills"])}')
    print(f'Выберите специальность для оценки студента {student["full_name"]}:')
    professions_list = []
    for professions in load_professions():
        for key, values in professions.items():
            if key == "title":
                professions_list.append(values)
    print(', '.join(professions_list))
    title = input().title()
    if title not in professions_list:
        print(f'У нас нет такой специальности')
        quit()
    profession = get_profession_by_title(title)
    student_profession_skills = chek_fitness(student, profession)
    print(f'Пригодность: {student_profession_skills["fit_percent"]}%')
    if student_profession_skills["fit_percent"] == 100:
        print(f'Студенту не надо ничего учить!!!')
    elif student_profession_skills["fit_percent"] == 0:
        print(f'Студенту {student["full_name"]} надо выучить все языки: {", ".join(student_profession_skills["laks"])}')
    else:
        print(f'{student["full_name"]} знает: {", ".join(student_profession_skills["has"])}')
        print(f'{student["full_name"]} не знает: {", ".join(student_profession_skills["laks"])}')


if __name__ == '__main__':
    main()
