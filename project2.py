import numpy as np
import  pandas as pd
import matplotlib.pyplot as plt


np.random.seed(42)

student_ids = np.arange(31,71)
names = ['Amir', 'Humaera', 'Ratul', 'Fahad', 'Monira',
         'Nafisa', 'Tareq', 'Hasib', 'Sadia', 'Rima',
         'Reza', 'Farzana', 'Kamrul', 'Sakib', 'Rafi',
         'Lubna', 'Anika', 'Sami', 'Khaled', 'Mitu',
         'hamja', 'umme', 'morsalin', 'fahim', 'refuel',
         'ahmedd', 'instanse', 'gasib', 'islam', 'hamida',
         'molla', 'Farzana 2.0', 'zaman', 'al hasan', 'hehe',
         'ibne sina', 'amina', 'md sami', 'Khaled bin walwd', 'yasmin']

random_names = np.random.choice(names,size=40, replace=True)
section = np.random.choice(['61A','61B','61C'], size=40)
attandance = np.random.randint(0,11, size=40)
midturm = np.random.randint(0,31, size= 40)
final = np.random.randint(0,41, size=40)
assaigment = np.random.randint(0,11, size=40)
ct1 = np.random.randint(0,11, size = 40)
ct2 = np.random.randint(0,11, size=40)

df = pd.DataFrame({
    'students_id': student_ids,
    'student_name': random_names,
    'section': section,
    'attandence': attandance,
    'midturm': midturm,
    'final': final,
    'assaigment': assaigment,
    'ct1': ct1,
    'ct2': ct2
})


# data cleaning
df.isnull().sum()
df['students_id'] = df['students_id'].fillna(df['students_id'].mode())
df['student_name'] = df['student_name'].fillna('unkhown')
df['section'] = df['section'].fillna('not assaign')
df['attandence'] = df['attandence'].fillna(df['attandence'].mean())
df['final'] = df['final'].fillna(0)
df['assaigment'] = df['assaigment'].fillna(0)
df['ct1'] = df['ct1'].fillna(0)
df['ct2'] = df['ct2'].fillna(0)
df.drop_duplicates(inplace=True)

# -----------------------------------
num_col = ['midturm','final', 'assaigment', 'ct1','ct2', 'attandence']
df[num_col] = df[num_col].apply(pd.to_numeric)

df['ct'] = np.maximum(df['ct1'], df['ct2'])
# print(df.dtypes)

df['final_grade'] = df['midturm'] +  df['final'] + df['assaigment'] + df['attandence'] + df['ct']

df['pass'] = np.where(df['final_grade'] >= 45, 'Yes', 'No')



avg = df['final_grade'].mean()
median = df['final_grade'].median()
stander_deviation = df['final_grade'].std()

print(f'avrage final grade: {avg}')
print(f'median final grade: {median}')
print(f'stander_deviation final grade: {stander_deviation}')

section_performance = df.groupby('section')['final_grade'].agg(['mean','median','max','min','count'])
print(section_performance)

section_top = df.loc[df.groupby('section')['final_grade'].idxmax()]
print(section_top)

corr_atdvsgra = df['attandence'].corr(df['final_grade'])
print(f'corrrelation between attandance and final grades: {corr_atdvsgra}')



section_avg = df.groupby('section')['final_grade'].mean()

# Visualizations (Matplotlib)

plt.hist(df['final_grade'], bins=5, color='red', edgecolor='black')
plt.title('Final Grades')
plt.grid(True)
plt.show()

section_avg.plot(kind='bar', color=['skyblue','orange','green' ])
plt.title('average grade per section')
plt.xlabel('section')
plt.ylabel('average grade')
plt.grid(True)
plt.show()

plt.scatter(df['final_grade'],df['attandence'],color='green', s=100, marker='^' )
plt.title('attendance vs final grade')
plt.xlabel('final grade')
plt.ylabel('attandace')
plt.grid(True)
plt.show()


best_section = section_avg.idxmax()
print(f'best section is: {best_section}')

correlation = df['attandence'].corr(df['final_grade'])
print(f'correlation between attandace and finl grade: {correlation:.2f}')

pass_fail_count = df['pass'].value_counts()
pass_fail_parcentage = df['pass'].value_counts(normalize=True)* 100

print(f'total passed counts: {pass_fail_count}')
print(f'total passed parcentage: {pass_fail_parcentage}')

pass_student = df[df['pass'] == 'Yes']
fail_student = df[df['pass'] == 'No']

print(f'Passed students: {pass_student}')
print(f'failed students: {fail_student}')
# print(df)


df.to_csv('project2_students_exam_summury.csv')