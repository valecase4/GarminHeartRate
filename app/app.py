from dash import Dash, html

app = Dash()

app.layout = html.Div(
    className="wrapper",
    children=[
        html.Div(className="navbar", children="Navbar"),
        html.Div(
            className="main", 
            children=[
                html.Div(
                    id="averageHeartRates",
                    className="stats__container flex-column"
                ),
                html.Div(
                    id="lastActivities",
                    className="stats__container flex-column"
                ),
                html.Div(
                    id="averageHeartRateByTimeSlot",
                    className="stats__container flex-column"
                ),
                html.Div(
                    id="deepSleepAverageHeartCorr",
                    className="stats__container flex-column"
                ),
                html.Div(
                    id="downloadReportSection"
                )
            ]
        )
    ]
)

if __name__ == '__main__':
    app.run(debug=True)