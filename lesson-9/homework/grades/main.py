grades_input_text = """Name,Subject,Grade
Alice,Math,85
Bob,Science,78
Carol,Math,92
Dave,History,74"""

grades_file_name = "grades.csv"
average_grades_file_name = "average_grades.csv"

with open(grades_file_name, "w+") as file:
    file.write(grades_input_text)

with open(grades_file_name, "r") as file:
    subject_scores_dic = dict()
    file.readline()
    for row in file.readlines():
        row_list = row.strip().split(",")

        subject = row_list[1]
        score = int(row_list[2])

        scores_list = subject_scores_dic[subject] if subject in subject_scores_dic else []
        scores_list.append(score)
        subject_scores_dic[subject] = scores_list

average_scores_txt = "Name, Subject, Grade\n"
for subject in subject_scores_dic.keys():
    summa = sum(subject_scores_dic[subject])
    size = len(subject_scores_dic[subject])
    average_score_float = summa / size
    average_score = int(average_score_float) if (average_score_float).is_integer() else average_score_float
    average_scores_txt += subject + "," + str(average_score) + "\n"
average_scores_txt.strip()
print(average_scores_txt)
with open(average_grades_file_name, "w+") as file:
    file.write(average_scores_txt)
