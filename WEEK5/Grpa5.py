#Implement all the given functions below according to the docstring. 

import random

def generate_student_data(n_students, courses, cities, random_seed=42):
    '''
    Create a list of dictionaries representing student data.
    '''
    random.seed(random_seed)

    return [
        {
            "rollno": i,
            "city": random.choice(cities),
            **{course: random.randint(1, 100) for course in courses}
        }
        for i in range(1, n_students + 1)
    ]


def groupby(data: list, key: callable):
    '''
    Group items based on key(item).
    '''
    groups = {}

    for item in data:
        k = key(item)

        if k not in groups:
            groups[k] = []

        groups[k].append(item)

    return groups


def apply_to_groups(groups: dict, func: callable):
    '''
    Apply a function to each group.
    '''
    for key in groups:
        groups[key] = func(groups[key])


def min_course_marks(student_data, course):
    return min(student[course] for student in student_data)


def max_course_marks(student_data, course):
    return max(student[course] for student in student_data)


def rollno_of_max_marks(student_data, course):
    max_student = max(student_data, key=lambda s: s[course])
    return max_student["rollno"]


def sort_rollno_by_marks(student_data, course1, course2, course3):
    '''
    Sort roll numbers by marks in course1, course2, course3.
    '''
    records = [
        (s[course1], s[course2], s[course3], s["rollno"])
        for s in student_data
    ]

    records.sort(reverse=True)

    return [rollno for _, _, _, rollno in records]


def count_students_by_cities(student_data):
    '''
    Count students city-wise.
    '''
    counts = {}

    for student in student_data:
        city = student["city"]
        counts[city] = counts.get(city, 0) + 1

    return counts


def city_with_max_no_of_students(student_data):
    '''
    Find city having maximum students.
    '''
    city_counts = count_students_by_cities(student_data)
    return max(city_counts, key=city_counts.get)


def group_rollnos_by_cities(student_data):
    '''
    Group roll numbers city-wise.
    '''
    groups = {}

    for student in student_data:
        city = student["city"]
        rollno = student["rollno"]

        if city not in groups:
            groups[city] = []

        groups[city].append(rollno)

    for city in groups:
        groups[city].sort()

    return groups


def city_with_max_avg_course_mark(student_data, course):
    '''
    Find city with highest average marks in the given course.
    '''
    city_sums = {}
    city_counts = {}

    for student in student_data:
        city = student["city"]
        mark = student[course]

        city_sums[city] = city_sums.get(city, 0) + mark
        city_counts[city] = city_counts.get(city, 0) + 1

    city_avgs = {
        city: city_sums[city] / city_counts[city]
        for city in city_sums
    }

    return max(city_avgs, key=city_avgs.get) 