from sklearn.ensemble import RandomForestRegressor


def model_fit(df):
    features = ["GDP per capita", "headcount_ratio_upper_mid_income_povline", "year"]
    target = "Life Expectancy (IHME)"

    X = df[features]
    y = df[target]

    model = RandomForestRegressor()
    model.fit(X, y)

    return model


def model_predict(model, new_data):
    return model.predict(new_data)
