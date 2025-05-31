import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

## original dataframe
print("original dataframe")
filedata = r"/Users/ardanta/Downloads/Tugas/CourseraDataset-Clean_new.csv"
df = pd.read_csv(filedata)
print(df)

## deskripsi dataframe numerik
print('')
print("deskripsi dataframe numerik:")
df_numerik = df.drop(columns=["Course Title", "Level", "Schedule", "What you will learn", "Skill gain"], axis=0)
deskripsinumerik = df_numerik.describe()
print(deskripsinumerik)

## korelasi dataframe numerik
print('')
print("korelasi dataframe numerik:")
kornumerik = df_numerik.corr()
print(kornumerik)

## range dataframe numerik
print('')
print("range dataframe numerik:")
range = df_numerik.max() - df_numerik.min()
print(range)

## modus dataframe numerik
print('')
print("modus:")
dfmode = df.drop(columns=["Course Title"])
modus = dfmode.mode()
print(modus.iloc[:,:4])
print(modus.iloc[:,-4:])

##DATA VISUALISATION##

##Correlation number of review and duration scatterplot
rate_dur = df.drop(columns=["Course Title", "Level", "Schedule", "What you will learn", "Skill gain", "Rating"])
kor_rate_dur = rate_dur.corr
variable_x = 'Number of Review'
variable_y = 'Duration to complete (Approx.)'
sns.scatterplot(x=variable_x, y=variable_y, data=rate_dur)
plt.title (f'Scatter Plot of {variable_x} vs {variable_y}')
plt.show()

##Bar chart level and schedule
variable = "Level"
sns.countplot(x=variable, data=df)
plt.title(f'Bar Chart of {variable}')
plt.show()