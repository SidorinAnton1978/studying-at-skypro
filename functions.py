# Импорт библиотеки json
import json


def load_json(filename):
    with open(filename) as f:
        return json.load(f)


def load_students():
    """ Загружает студентов из файла students.json в список """
    return load_json('students.json')


def load_professions():
    """ Загружает навыки из файла professions.json в список """
    return load_json('professions.json')


def get_student_by_pk(pk):
    """ Создает словарь с данными студента """
    for student in load_students():
        if student["pk"] == pk:
            return student


def get_profession_by_title(title):
    """ Создает словарь с данными профессии """
    for profession in load_professions():
        if profession["title"] == title:
            return profession


def chek_fitness(student, profession):
    """ Создает словарь пригодности студента к профессии """
    student_skills = set(student["skills"])
    profession_skill = set(profession["skills"])
    has_skill = student_skills.intersection(profession_skill)
    laks_skill = profession_skill.difference(has_skill)
    has_percent = round(len(has_skill)/len(profession_skill)*100)
    student_profession_skill = {"has": list(has_skill), "laks": list(laks_skill), "fit_percent": has_percent}
    return student_profession_skill
