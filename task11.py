import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data set.csv')
print("Dataset columns and sample data':")
print(df.head(10))

columns_to_plot = ['Region', 'IncomeGroup']

for column in columns_to_plot:
    if column in df.columns:
        plt.figure (figsize = (9,5))
        sns.countplot(
            data=df,
            x=column,
            palette='pastel',
            order=df[column].value_counts().index
        )

        plt.title(f'distribution of {column}')
        plt.xlabel(column)
        plt.ylabel('count')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()





