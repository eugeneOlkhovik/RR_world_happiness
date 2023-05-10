import plotly.graph_objects as go
import pandas as pd


def plot_happiness_score(df: pd.DataFrame, happiness_score,
                         country, n, year):
    """
    Creates a horizontal bar plot of the top n happiest
    countries based on the 'Happiness score' column of the given data frame.

    Parameters:
        df (pandas DataFrame): the data frame to use
        happiness_score (str): since happiness score is different in each
        dataframe it will passed as parameter
        country (str): same as for country column
        n (int): the number of top happiest countries to display
        year  (int): add data year in plot's title

    Returns:
        None
    """

    # Sort the data frame by Happiness score and select the top n rows
    df_20 = df.sort_values(by=happiness_score, ascending=False).head(n)

    fig = go.Figure()
    fig.add_trace(go.Bar(x=df_20[happiness_score],
                         y=df_20[country],
                         orientation='h',
                         marker=dict(color=df_20[happiness_score],
                         colorscale='viridis')
                         ))

    # Set the layout of the plot
    fig.update_layout(title=f'Top {n} happiest countries in {year}',
                      yaxis=dict(
                                showgrid=False,
                                showline=False,
                                showticklabels=True,
                                categoryorder='total ascending'
                                ),
                      xaxis_title='Happiness score',
                      yaxis_title='country',
                      margin=dict(l=50, r=100, t=50, b=50))

    fig.show()
