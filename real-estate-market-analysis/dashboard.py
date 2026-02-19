import os

import mysql.connector
import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

DB_CONFIG = {
    "host": os.environ.get("DB_HOST", "localhost"),
    "user": os.environ.get("DB_USER", ""),
    "password": os.environ.get("DB_PASSWORD", ""),
    "database": os.environ.get("DB_NAME", ""),
    "use_pure": True,
}


def fetch_data():
    with mysql.connector.connect(**DB_CONFIG) as conn:
        query = "SELECT * FROM real_estate_data"
        df = pd.read_sql(query, conn)
    return df


app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Real Estate Market Dashboard"),
    dcc.Dropdown(
        id="chart-type",
        options=[
            {"label": "Net Revenue by Month", "value": "revenue"},
            {"label": "Sales by State and Type", "value": "sales"},
        ],
        value="revenue",
        clearable=False,
    ),
    dcc.Graph(id="main-graph"),
])


@app.callback(
    Output("main-graph", "figure"),
    Input("chart-type", "value"),
)
def update_graph(chart_type):
    df = fetch_data()

    df["date_sale"] = pd.to_datetime(df["date_sale"])
    df["year"] = df["date_sale"].dt.year
    df["month"] = df["date_sale"].dt.month
    df["price"] = (
        df["price"].astype(str).str.strip().str.replace("$", "", regex=False).str.replace(",", "", regex=False)
    )
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df["net_price"] = df["price"].where(df["status"] == 1, 0)

    if chart_type == "revenue":
        revenue = df.groupby(["year", "month"])["net_price"].sum().reset_index(name="net_revenue")
        fig = px.line(
            revenue,
            x="month",
            y="net_revenue",
            color="year",
            markers=True,
            title="Monthly Net Revenue by Year",
            labels={"month": "Month", "net_revenue": "Net Revenue"},
        )
    else:
        df["state_label"] = df["state"].map({1: "California", 0: "Other"})
        sold = df[df["status"] == 1]
        counts = sold.groupby(["state_label", "type"]).size().reset_index(name="sales")
        fig = px.bar(
            counts,
            x="state_label",
            y="sales",
            color="type",
            barmode="stack",
            title="Sales by State and Building Type",
            labels={"state_label": "State", "sales": "Number of Sales"},
        )

    return fig


if __name__ == "__main__":
    debug = os.environ.get("DASH_DEBUG", "false").lower() == "true"
    app.run(debug=debug)
