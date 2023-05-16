import plotly.graph_objects as go
import seaborn as sns
import geopandas as gpd
import matplotlib.pyplot as plt
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
                      width=800,
                      height=500,
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


def create_bump_chart(year_to_data):
    df = pd.concat(year_to_data.values())[
        ['Country', 'rank', 'year', 'happiness_score']]
    df['rank'] = df['rank'].astype(int)
    df_top20 = df[df.groupby('year')['rank'].apply(lambda x: x <= 20)]

    fig = go.Figure()
    countries = df_top20['Country'].unique()
    colors = sns.color_palette('husl', len(countries))
    for i, country in enumerate(countries):
        country_df = df_top20[df_top20['Country'] == country]
        rgb_color = tuple(int(255 * x) for x in colors[i])
        fig.add_trace(
            go.Scatter(
                x=country_df['year'],
                y=country_df['rank'],
                mode='lines+markers',
                name=country,
                line=dict(color=f'rgb{rgb_color}'),
            )
        )

    fig.update_layout(
        yaxis=dict(
            autorange="reversed",
            tickmode='array',
            tickvals=list(range(1, 21)),
            ticktext=list(range(1, 21))
        ),
        width=1200,
        height=900,
        title="Bump Chart for Happiness Index Rank for Top 20 Countries",
        xaxis_title="Year",
        yaxis_title="Rank",
        margin=dict(l=50, r=100, t=50, b=50)
    )
    fig.show()


def plot_happiness_map(df, happiness_index_column, country_column):
    """
    Plot a world map of the World Happiness Report by happiness score.

    Args:
    df (pandas.DataFrame): DataFrame with 'country'
    and 'value' columns representing
    the country name and happiness score, respectively.

    Returns:
    None
    """
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    world = world.merge(df, how='left',
                        left_on='name', right_on=country_column)
    _, ax = plt.subplots(1, 1, figsize=(24, 12))
    world.plot(column=happiness_index_column,
               ax=ax,
               legend=True,
               cmap='coolwarm',
               legend_kwds={'label': "Happiness Score",
                            'orientation': "horizontal",
                            'shrink': 0.5},
               missing_kwds={"color": "darkgrey"})
    plt.title('World Map for 2022 World Happiness Report')
    plt.show()
