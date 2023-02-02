import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="whitegrid", palette="muted")

df = pd.read_csv (r'categorical.csv')
print (df)

# Draw a categorical scatterplot to show each observation
ax = sns.swarmplot(data=df, x="Yield", y="Cultivars", hue="Irrigation")
ax.set(ylabel="")
plt.show()
