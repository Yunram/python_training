# Dictionaries
# print("Hello")
#
# student_scores = {"Harry": 81, "Ron": 78, "Hermione": 99, "Draco": 74, "Neville": 62, "Malcom": 170}
#
# student_grades = {}
#
# for person in student_scores:
#     if student_scores[person] >= 91 and student_scores[person] <= 100:
#         student_grades[person] = "Outstanding"
#     elif student_scores[person] >= 81 and student_scores[person] <= 90:
#         student_grades[person] = "Exceeds Expectations"
#     elif student_scores[person] >= 71 and student_scores[person] <= 80:
#         student_grades[person] = "Acceptable"
#     elif student_scores[person] >= 0 and student_scores[person] <= 70:
#         student_grades[person] = "Fail"
#     else:
#         student_grades[person] = "Not valid score"
#
# print(student_grades)

travel_log = [
{
 "country": "France",
 "cities_visited": ["Paris", "Lilles", "Nantes"],
 "visits": 3,
},
{
 "country": "Germany",
 "cities_visited": ["Berlin", "Hamburg", "Nurnberg"],
 "visits": 2,
},
]

def add_new_country(visited_country, visited_cities, num_of_visits):
    new_country = {}
    new_country["country"] = visited_country
    new_country["cities_visited"] = visited_cities
    new_country["visits"] = num_of_visits
    travel_log.append(new_country)

add_new_country("Russia", ["Moscow", "Kazan", "Tver"], 4)
print(travel_log)