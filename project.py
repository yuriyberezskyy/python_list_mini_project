first_names = ["Ainsley", "Ben", "Chani", "Depak"]
age = []
age.append(42)
print(age)

all_ages = [32, 41, 29] + age
print(all_ages)

ids = range(0, 4)
name_and_age = zip(ids, first_names, all_ages)
print(list(name_and_age))
