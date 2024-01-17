# Hypothesis: budget and company will be highly correlated with gross revenue. Analyze the data to verify if this is true.

import numpy as np
import pandas as pd
import seaborn as sns

import matplotlib
import matplotlib.pyplot as plt
plt.style.use('ggplot')
from matplotlib.pyplot import figure

# this line is only required in Jupyter Notebook, may not be required in other IDEs
%matplotlib inline

matplotlib.rcParams['figure.figsize'] = (12,8)

# read the data

df = pd.read_csv(r'C:\Users\Directory\movies.csv')

# View the data

print(df.head())

# Search for missing data

for col in df.columns:
    percent_missing = np.mean(df[col].isnull())
    print('{} - {}%'.format(col, percent_missing))

# Data types for columns

print(df.dtypes)

# Change data type of columns

df['budget'] = pd.to_numeric(df['budget'], errors='coerce').fillna(df['budget'].mean()).astype('float64')
df['gross'] = pd.to_numeric(df['gross'], errors='coerce').fillna(df['gross'].mean()).astype('float64')

# Create correct year column

df['yearcorrect'] = df['released'].astype(str).str[:4]

df.sort_values(by=['gross'], inplace=False, ascending=False)

pd.set_option('display.max_rows', None)

# Drop any duplicates

df['company'] = df['company'].drop_duplicates().sort_values(ascending=False)

# Scatter plot with company vs gross revenue

df_clean = df.dropna(subset=['company', 'gross'])
plt.scatter(x=df_clean['company'], y=df_clean['gross'])
plt.title('Company vs Gross Earnings')
plt.xlabel('Gross Earnings')
plt.ylabel('Company')
plt.show()

print(df.head())

# Scatter plot with budget vs gross revenue

df_clean = df.dropna(subset=['budget', 'gross'])
plt.scatter(x=df_clean['budget'], y=df_clean['gross'])
plt.title('Budget vs Gross Earnings')
plt.xlabel('Gross Earnings')
plt.ylabel('Budget for Film')
plt.show()

print(df.head())

# Plot budget vs gross earnings using seaborn

sns.regplot(x='budget', y='gross', data=df, scatter_kws={"color": "red"}, line_kws={"color": "blue"})
plt.show()

# Only shows correlation for numeric values

df_numeric = df.select_dtypes(include='number')

print(df_numeric.corr(method='pearson'))

# High positive correlation between budget and gross, 0.6 and above seems to indicate high correlation

'''
# pearson, kendall, and spearman are 3 methods of correlating available
print(df_numeric.corr(method='pearson'))
print(df_numeric.corr(method='kendall'))
print(df_numeric.corr(method='spearman'))
'''

# Correlation Heatmap for df_numeric

correlation_matrix = df_numeric.corr(method='pearson')

sns.heatmap(correlation_matrix, annot=True)

plt.title('Correlation Matrix for Numeric Features')
plt.xlabel('Movie Features')
plt.ylabel('Movie Features')
plt.show()

# Examine company

print(df.head())

df_numerized = df

for col_name in df_numerized.columns:
    if(df_numerized[col_name].dtype == 'object'):
        df_numerized[col_name] = df_numerized[col_name].astype('category')
        df_numerized[col_name] = df_numerized[col_name].cat.codes

print(df_numerized.head())

# Correlation Heatmap for df_numerized

correlation_matrix = df_numerized.corr(method='pearson')

sns.heatmap(correlation_matrix, annot=True)

plt.title('Correlation Matrix for Numeric Features')
plt.xlabel('Movie Features')
plt.ylabel('Movie Features')
plt.show()

# Sorting df_numerized into highly correlated pairs

correlation_mat = (df_numerized.corr())
correlation_pairs = correlation_mat.unstack()
sorted_pairs = correlation_pairs.sort_values()
high_correlation = sorted_pairs[(sorted_pairs) > 0.5]

print(high_correlation)

'''
Conclusion: After analyzing the data, I can determine that votes has high correlation to gross with a correlation of 0.628713 and budget also has high correlation to gross with a correlation of 0.711270. 
However, company was very lowly correlated to gross and had a correlation of -0.14. My Hypothesis was partially correct and partially incorrect. I was wrong about company but I was right about budget and votes.
'''
