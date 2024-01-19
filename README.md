# **MOVIE CORRELATION ANALYSIS REPORT** 

I explored key variables influencing box office earnings and used data visualization to reveal hidden patterns and insights.

## PROJECT DESCRIPTION:

Analyze 6820 box office movies spanning from 1986-2016 and develop data visualizations to display which variables correlate most to movie gross earnings. Download dataset from https://www.kaggle.com/datasets/danielgrijalvas/movies (Account required to login and download) 

### Hypothesis
- Which variables contribute to box office performance?

### Analysis
- What were your findings after analyzing the data?

### Conclusion
- What do your findings mean?

## Development Requirements

- Use Pandas to clean and format your dataset(s).
- Create a Jupyter Notebook describing the data exploration and cleanup process.
- Create a Jupyter Notebook illustrating the final data analysis.
- Use Matplotlib and Seaborn to create a total of 3-4 visualizations of your data (ideally, at least 1 per ”question” you ask of your data).
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
My findings signal to me that when a company has a large budget and when their film has a lot of audience voting, it is likely that their gross revenue will also increase.
This means that movie budgets and audience voting are important variables that are linked to gross revenue and influence a film's performance at the box office.

## Notes
It's worth noting that this analysis seems to be missing some context. The dataset also does not reflect positive or negative sentiment analysis of votes. My intuition tells me that"
- An increase in quantity of votes does not necessarily mean that movie will perform well.
- If there is an increase in positive sentiment votes then that film is more likely to have higher gross revenue
- If there is an increase in negative sentiment votes then that film is likely to have lower gross revenue.
- However, it is generally better that a film has more votes than no votes at all, because that means the film is at least receiving attention.
