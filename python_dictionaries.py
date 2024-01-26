
# Ways to create a dictionary in python
Students = ['Jack', 'Alice', 'Alex', 'Lisa']
Scores = [87, 90, 89, 92]


# Uses a nested for loop
def create_dict1(students, scores):
    dict1 = {}
    for student in students:
        for score in scores:
            dict1[student] = score
            scores.remove(score)
            break
    return dict1


# Uses a dictionary comprehension
def create_dict2(students, scores):
    dict2 = {students[i]: scores[i] for i in range(len(students))}
    return dict2


# Uses a dict, map, and lambda function
def create_dict3(students, scores):
    dict3 = dict(map(lambda student, score: (student, score), students, scores))
    return dict3


# Uses the enumerate and zip functions
def create_dict4(students, scores):
    tuples = [(student, score)
              for i, (student, score) in enumerate(zip(students, scores))]
    dict4 = dict(tuples)
    return dict4


# Uses dict and zip functions
def create_dict5(students, scores):
    dict5 = dict(zip(students, scores))
    return dict5
