# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
    #print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

#8a
df = pd.read_csv("~/PycharmProjects/statisticalLearning/venv/data/College.csv")
#print(df)

#8b
college = df.set_index(['Unnamed: 0'], append=True, verify_integrity=True)
college.rename_axis([None, 'College'], inplace=True)
#print(college.head())

#8c i
#print(college.describe())

#8c ii
sns.pairplot(college.iloc[:, 1:11])
plt.show()




