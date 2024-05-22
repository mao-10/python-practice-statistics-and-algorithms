import scipy.stats as st
import pandas as pd

scores = pd.read_csv('http://data-analytics.zybooks.com/ExamScores.csv')

# data for simple normal interval
# let n be num of people who voted
n = 1200
# let p be proportion of ppl who voted in favor
p = 348.0/1200.0
# The standard error is sqrt(p * (1-p)/n)
standardError = (p * (1 - p)/ n) ** 0.5
print(st.norm.interval(0.95, p, standardError))


# data from file
# let n be total num of students who took an exam
raw_n = scores[['Exam1']].count()
# let x be the total of all exam scores greater than 90
x = (scores[['Exam1']] > 90).values.sum()
# let p be the proportion of students who scored over 90
raw_p = x/raw_n * 1.0
# The standard error is sqrt(p * (1-p)/n)
stderr = (raw_p * (1 - raw_p)/ raw_n) ** 0.5
print(st.norm.interval(0.99, raw_p, stderr))
