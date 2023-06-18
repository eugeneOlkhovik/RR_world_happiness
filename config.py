year_to_rank_column_name = {
    2015: "Happiness Rank",
    2016: "Happiness Rank",
    2017: "Happiness.Rank",
    2018: "Overall rank",
    2019: "Overall rank",
    2020: "RANK",
    2021: "RANK",
    2022: "RANK",
}

year_to_happiness_score_column_name = {
    2015: "Happiness Score",
    2016: "Happiness Score",
    2017: "Happiness.Score",
    2018: "Score",
    2019: "Score",
    2020: "Ladder score",
    2021: "Ladder score",
    2022: "Happiness score",
}

year_to_country_column_name = {
    2015: "Country",
    2016: "Country",
    2017: "Country",
    2018: "Country or region",
    2019: "Country or region",
    2020: "Country name",
    2021: "Country name",
    2022: "Country",
}

# Define the list of countries in the Global North
north_countries = ['United States', 'Canada'
                   'Austria', 'Belgium', 'Bulgaria',
                   'Croatia', 'Republic of Cyprus'
                   'Czech Republic', 'Denmark',
                   'Estonia', 'Finland', 'France'
                   'Germany', 'Greece', 'Hungary',
                   'Ireland', 'Italy', 'Latvia'
                   'Lithuania', 'Luxembourg',
                   'Malta', 'Netherlands', 'Poland'
                   'Slovakia', 'Slovenia', 'Spain'
                   'Sweden', 'United Kingdom',
                   'Portugal', 'Romania',
                   'Australia', 'New Zealand'
                   'Japan', 'South Korea']

# dict fior mapping column names
col_name_to_shorter_col_name = {
    'Country': 'country',
    'Happiness score': 'happiness_score',
    'Explained by: GDP per capita': 'gdp_per_capita',
    'Explained by: Social support': 'social_support',
    'Explained by: Healthy life expectancy': 'life_expectancy',
    'Explained by: Freedom to make life choices': 'freedom',
    'Explained by: Generosity': 'genorosity',
    'Explained by: Perceptions of corruption': 'perceptions_corruption'
}

# list for numerical variables
numerical_cols = ['happiness_score', 'Whisker-high', 'Whisker-low', 'Dystopia (1.83) + residual',
                  'gdp_per_capita', 'social_support', 'life_expectancy', 'freedom', 'genorosity',
                  'perceptions_corruption']

#list for independent variables
independent_variables = ['gdp_per_capita', 'social_support', 'life_expectancy', 'freedom', 'genorosity', 'perceptions_corruption', 'global_north']