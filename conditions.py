adams_age = 35

if adams_age <= 50:
    print("You can still do anything you put your mind too!")

gpa_scores = [2.14, 3.3, 2.4, 1.99, 3.1, 1.5, 2.2, 2.0, 1.1, 3.5]
upper_bracket = []
lower_bracket = []
median_gpa = 0

for i in gpa_scores:
    if i > 2.2:
        upper_bracket.append(i)
    else:
        lower_bracket.append(i)

print(f"There are {len(upper_bracket)} in the upper bracket -", upper_bracket)
print(f"There are {len(lower_bracket)} in the lower bracket -", lower_bracket)
