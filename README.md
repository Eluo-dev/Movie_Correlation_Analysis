# **MOVIE CORRELATION ANALYSIS REPORT** 

I explored key variables influencing box office earnings and used data visualization to reveal hidden patterns and insights.

## PROJECT DESCRIPTION:

Analyze 6820 box office movies spanning from 1986-2016 and develop data visualizations to display which variables correlate most to movie gross earnings.

### Hypothesis
- Which variables contribute to box office performance?

### Analysis
- Why?

### Conclusion
- What do your findings mean?

## Development Requirements

- Use Pandas to clean and format your dataset(s).
- Create a Jupyter Notebook describing the data exploration and cleanup process.
- Create a Jupyter Notebook illustrating the final data analysis.
- Use Matplotlib and Seaborn to create a total of 6–8 visualizations of your data (ideally, at least 2 per ”question” you ask of your data).
- Save PNG images of your visualizations to distribute and for inclusion in your presentation.

## Data Cleanup & Analysis
- CLEAN: Useless columns, duplicate values and Null values were removed.

- TRANSFORM: Columns were renamed, data types were altered, and non-numeric fields were converted to numeric fields.

- LOAD: The clean csv data was imported into Jupyter Notebook as this was found to be the best way to illustrate and connect the relationship within the data.

## Technology Overview
Python & Libraries | Pandas, Matplotlib, Seaborn, NumPy

## Hypothesis
The variables budget, votes, and company will be highly correlated with gross revenue. 
Analyze the data to verify if this is true.

## Analysis
After analyzing the data, I can determine that votes have a high correlation to gross with a correlation of 0.628713
budget also has a high correlation to gross, with a correlation of 0.711270

However, company was very lowly correlated to gross and had a correlation of -0.14.

My Hypothesis was partially correct and partially incorrect. I was wrong about company but I was right about budget and votes.

## Conclusion
My findings signal to me that when a company has a large budget and when votes increase, it is likely that their gross revenue will also increase.
This means that movie budgets and audience voting are important variables that are linked to gross revenue and influence a film's performance at the box office.

## Notes
- Dataset was downloaded from https://www.kaggle.com/datasets/danielgrijalvas/movies
- Insert your own directory when locating and reading the data
