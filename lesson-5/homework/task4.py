def enrollment_stats(unis):
    _universities = list(unis)
    enroll = []
    tuition = []
    for i in _universities:
        enroll.append(i[1])
        tuition.append(i[2])
    return enroll, tuition


def mean(_list):
    return round(sum(_list) / len(_list), 2)


def median(_list):
    l = list(_list)
    l.sort()
    if len(l) % 2 == 1:
        middle = int(len(l) / 2)
        return l[middle]
    else:
        middle1 = int(len(l) / 2) - 1
        middle2 = int(len(l) / 2)
        return (l[middle1] + l[middle2]) / 2


def add_coma(txt):
    text = str(txt)
    text = text.replace(" ", "")
    output = ""
    dot_index = len(text) if "." not in text else text.index(".")
    for index, value in enumerate(text):
        output += value
        if (len(text) - 1 - (len(text) - dot_index) - index) % 3 == 0:
            output += ","
            if index + 1 == dot_index:
                output = output[:-1]
            if index > dot_index:
                output = output[:-1]
    return output


universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

enrollments, tuitions = enrollment_stats(universities)
print("******************************")
print(f"Total students: {add_coma(sum(enrollments))}")
print(f"Total tuition: $ {add_coma(sum(tuitions))}")
print("\n")
print(f"Student mean: {add_coma(mean(enrollments))}")
print(f"Student median: {add_coma(median(enrollments))}")
print("\n")
print(f"Tuition mean: $ {add_coma(mean(tuitions))}")
print(f"Tuition median: $ {add_coma(median(tuitions))}")
print("******************************")
