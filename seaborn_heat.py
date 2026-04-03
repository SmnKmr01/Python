import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")
sns.heatmap(x="total_bill", y="tip", data=df, hue="size")
plt.show()
