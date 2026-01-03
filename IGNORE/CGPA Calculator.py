def get_marks(subject):
    while True:
        try:
            m1 = int(input(f"Type your {subject} Insem 1 marks (out of 40): "))
            if 0 <= m1 <= 40:
                break
            print("Enter marks between 0 and 40.")
        except ValueError:
            print("Enter a valid number.")
    while True:
        try:
            m2 = int(input(f"Type your {subject} Insem 2 marks (out of 40): "))
            if 0 <= m2 <= 40:
                break
            print("Enter marks between 0 and 40.")
        except ValueError:
            print("Enter a valid number.")
    return m1, m2


def grade_assignment(percent):
    if percent < 40: return 0
    elif percent <= 44: return 4
    elif percent <= 49: return 5
    elif percent <= 59: return 6
    elif percent <= 69: return 7
    elif percent <= 79: return 8
    elif percent <= 89: return 9
    else: return 10


# Normal subjects (with Insems)
math1, math2 = get_marks("Engineering Mathematics - I")
chem1, chem2 = get_marks("Engineering Chemistry")
cs1, cs2     = get_marks("Communication Skills")
cplt1, cplt2 = get_marks("CPLT")

# Special subjects (no Insems)
print("\nNow enter marks for DL and EDP:\n")

# -----------------------
# DIGITAL LITERACY (DL)
# -----------------------
quiz_total = 0
for i in range(1, 6):
    while True:
        try:
            quiz = float(input(f"DL Quiz {i} marks (out of 20): "))
            if 0 <= quiz <= 20:
                quiz_total += (quiz / 5)  # normalize each to /4 total
                break
            print("Enter marks between 0 and 20.")
        except ValueError:
            print("Enter a valid number.")

dl_assignment = 20   # full marks assumed
while True:
    try:
        dl_project = float(input("DL Project marks (out of 30): "))
        if 0 <= dl_project <= 30:
            break
        print("Enter marks between 0 and 30.")
    except ValueError:
        print("Enter a valid number.")

dl_portfolio = 20    # full marks assumed
while True:
    try:
        attendance_pct = float(input("DL Attendance percentage (0-100): "))
        if 0 <= attendance_pct <= 100:
            dl_attendance = attendance_pct / 10  # normalized to /10
            break
        print("Enter percentage between 0 and 100.")
    except ValueError:
        print("Enter a valid number.")

dl_total = quiz_total + dl_assignment + dl_project + dl_portfolio + dl_attendance
dl_percent = dl_total  # already out of 100
dl_grade = grade_assignment(dl_percent)

# -----------------------
# EDP
# -----------------------
while True:
    try:
        edp_pitch = float(input("EDP Startup Pitch marks (out of 50): "))
        if 0 <= edp_pitch <= 50:
            break
        print("Enter marks between 0 and 50.")
    except ValueError:
        print("Enter a valid number.")

edp_linkedin = 25  # full marks assumed
while True:
    try:
        edp_mcq = float(input("EDP MCQ Test marks (out of 50): "))
        if 0 <= edp_mcq <= 50:
            edp_mcq = (edp_mcq / 2)  # normalized to /25
            break
        print("Enter marks between 0 and 50.")
    except ValueError:
        print("Enter a valid number.")

edp_total = edp_pitch + edp_linkedin + edp_mcq
edp_percent = edp_total  # out of 100
edp_grade = grade_assignment(edp_percent)

# -----------------------
# GPA Calculation Setup
# -----------------------
target_gpa = float(input("\nEnter your target GPA (e.g., 8.0): "))

subjects = {
    "Mathematics": {"credits": 4, "insem1": math1, "insem2": math2},
    "Chemistry":   {"credits": 3, "insem1": chem1, "insem2": chem2},
    "CPLT":        {"credits": 3, "insem1": cplt1, "insem2": cplt2},
    "Comms":       {"credits": 1, "insem1": cs1, "insem2": cs2}
}

print("\nRequired Endsem Marks (out of 100):\n")

results = []
total_weighted = 0
total_credits = 0

for sub, data in subjects.items():
    insem1_pct = data["insem1"] * 0.375
    insem2_pct = data["insem2"] * 0.375
    insem_contrib = insem1_pct + insem2_pct
    assign_contrib = 20  # full assignment marks (20%)
    known_total = insem_contrib + assign_contrib

    target_percent = target_gpa * 10
    required_endsem = (target_percent - known_total) / 0.50

    if required_endsem > 100:
        remark = f"Impossible 😬 (need {required_endsem:.1f})"
        percent = known_total
    elif required_endsem < 0:
        remark = "Already secured 🎉"
        percent = 100
    else:
        remark = f"Need {required_endsem:.1f} in Endsem"
        percent = known_total + (required_endsem * 0.5)

    grade = grade_assignment(percent)
    results.append((sub, percent, grade, data["credits"]))
    print(f"{sub:<15}: {remark}")

# Add DL and EDP
results.append(("Digital Literacy", dl_percent, dl_grade, 2))
results.append(("EDP", edp_percent, edp_grade, 1))

# Compute SGPA
for sub, percent, grade, credits in results:
    total_weighted += grade * credits
    total_credits += credits

sgpa = total_weighted / total_credits

# Display results
print("\nFinal SGPA Projection:")
for sub, percent, grade, credits in results:
    print(f"{sub:<18} - {percent:6.2f}% | Grade {grade} | Credits: {credits}")
