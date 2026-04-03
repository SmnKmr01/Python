import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")
print(df.head())
sns.lineplot(x="total_bill", y="tip", data=df)
plt.show()
