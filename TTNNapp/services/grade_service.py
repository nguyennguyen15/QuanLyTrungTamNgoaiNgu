def calculate_result(midterm, final_exam, attendance_score):
    average = round(midterm * 0.3 + final_exam * 0.5 + attendance_score * 0.2, 2)
    return average, "Đạt" if average >= 5 else "Không đạt"
