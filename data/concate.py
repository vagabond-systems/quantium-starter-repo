import pandas
import csv

df1 = pandas.read_csv('final_result.csv', parse_dates=['date'])
df2 = pandas.read_csv('final_result_1.csv', parse_dates=['date'])
df3 = pandas.read_csv('final_result_2.csv', parse_dates=['date'])

concat_df = pandas.concat([df1, df2, df3], axis=0)

concat_df.to_csv('concat_file.csv', index=False)

print(concat_df)


