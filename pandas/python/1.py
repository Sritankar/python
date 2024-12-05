import pandas as pd

file_path = "student_marks.csv"  
df = pd.read_csv(file_path)


total_marks = df['Marks'].sum()       
average_marks = df['Marks'].mean()   
top_student = df.loc[df['Marks'].idxmax()]  

print("Total Marks:", total_marks)
print("Average Marks:", average_marks)
print("Top Student Details:\n", top_student)
