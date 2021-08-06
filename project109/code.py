import plotly.figure_factory as ff
import statistics
import random
import plotly.graph_objects as go

testScores = []
mathScores = []
readingScores = []
writingScores = []
testScores.append(mathScores + readingScores + writingScores)

mean = sum(testScores)/len(testScores)
print(mean)

median = statistics.median(testScores)
print(median)

mode = statistics.mode(testScores)
print(mode)

standardDeviation = statistics.stdev(testScores)
print(standardDeviation)

first_sd_start, first_sd_end = mean - standardDeviation, mean + standardDeviation
second_sd_start, second_sd_end = mean - (2*standardDeviation), mean + (2*standardDeviation)
third_sd_start, third_sd_end = mean - (3*standardDeviation), mean + (3*standardDeviation)

list_of_data_within_1_std_deviation = [result for result in testScores if result > first_sd_start and result < first_sd_end]
print('{}% of data lies within first standard deviation'.format(len(list_of_data_within_1_std_deviation)*100.0/len(testScores)))

list_of_data_within_2_std_deviation = [result for result in testScores if result > second_sd_start and result < second_sd_end]
print('{}% of data lies within second standard deviation'.format(len(list_of_data_within_2_std_deviation)*100.0/len(testScores)))

list_of_data_within_3_std_deviation = [result for result in testScores if result > third_sd_start and result < third_sd_end]
print('{}% of data lies within third standard deviation'.format(len(list_of_data_within_3_std_deviation)*100.0/len(testScores)))

#Plotting the chart, and lines for mean, 1 standard deviation and 2 standard deviations 
fig = ff.create_distplot([testScores], ["Result"], show_hist=False) 
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN")) 
fig.add_trace(go.Scatter(x=[first_sd_start, first_sd_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1")) 
fig.add_trace(go.Scatter(x=[first_sd_end, first_sd_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[second_sd_start, second_sd_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2")) 
fig.add_trace(go.Scatter(x=[second_sd_end, second_sd_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2")) 
fig.show()
