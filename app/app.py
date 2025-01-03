from dash import Dash, html

app = Dash()

app.layout = html.Div(
    className="wrapper",
    children=[
        html.Div(
            className="navbar",
            children=[
                html.Button(
                    id="reloadBtn",
                    children=[
                        "Reload Data"
                    ]
                )
            ]
        ),
        html.Div(
            className="main", 
            children=[
                html.Div(
                    id="averageHeartRates",
                    className="stats__container flex-column",
                    children=[
                        html.Div(
                            className='stats__container--title border-bottom',
                            children="Average Heart Rate"
                        ),
                        html.Div(
                            className='stats__container--content flex-row',
                            children=[
                                html.Div(
                                    className='stats__card w-33 h-100 flex-column',
                                    children=[
                                        html.Div(
                                            className="card__section flex-column",
                                            children=[
                                                html.Div(
                                                    className="card__section-text",
                                                    children="Global"
                                                ),
                                                html.Div(
                                                    className="card__section-text",
                                                    children=html.Img(
                                                        src="assets/media/heart.png",
                                                        className="heart__img"
                                                    )
                                                ),
                                                html.Div(
                                                    className="card__section-text bold",
                                                    children="...bpm"
                                                )
                                            ]
                                        )
                                    ]
                                ),
                                html.Div(
                                    className='stats__card w-33 h-100 flex-column',
                                    children=[
                                        html.Div(
                                            className="card__section flex-column border-left border-right",
                                            children=[
                                                html.Div(
                                                    className="card__section-text",
                                                    children="Running"
                                                ),
                                                html.Div(
                                                    className="card__section-text",
                                                    children=html.Img(
                                                        src="assets/media/heart.png",
                                                        className="heart__img"
                                                    )
                                                ),
                                                html.Div(
                                                    className="card__section-text bold",
                                                    children="...bpm"
                                                )
                                            ]
                                        ),
                                    ]
                                ),
                                html.Div(
                                    className='stats__card w-33 h-100 flex-column',
                                    children=[
                                        html.Div(
                                            className="card__section flex-column",
                                            children=[
                                                html.Div(
                                                    className="card__section-text",
                                                    children="Strength"
                                                ),
                                                html.Div(
                                                    className="card__section-text",
                                                    children=html.Img(
                                                        src="assets/media/heart.png",
                                                        className="heart__img"
                                                    )
                                                ),
                                                html.Div(
                                                    className="card__section-text bold",
                                                    children="...bpm"
                                                )
                                            ]
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                html.Div(
                    id="lastActivities",
                    className="stats__container flex-column",
                    children=[
                        html.Div(
                            className='stats__container--title border-bottom',
                            children="Last Activities"
                        ),
                        html.Div(
                            className='stats__container--content flex-row',
                            children=[
                                html.Div(
                                    className="w-50 h-100 border-right",
                                    children=[
                                        html.Div(
                                            className="w-100 h-12_5 border-bottom centered",
                                            children="Running"
                                        ),
                                        html.Div(
                                            className="w-100 h-12_5 flex-row",
                                            children=[
                                                html.Div(
                                                    className="w-50 h-100 border-right border-bottom centered bold",
                                                    children="Average Heart Rate"
                                                ),
                                                html.Div(
                                                    className="w-50 h-100 border-bottom centered"
                                                )
                                            ]
                                        ),
                                        html.Div(
                                            className="w-100 h-12_5 flex-row",
                                            children=[
                                                html.Div(
                                                    className="w-50 h-100 border-right border-bottom centered bold",
                                                    children="Max Heart Rate"
                                                ),
                                                html.Div(
                                                    className="w-50 h-100 border-bottom centered"
                                                )
                                            ]
                                        ),
                                        html.Div(
                                            className="w-100 h-12_5 flex-row",
                                            children=[
                                                html.Div(
                                                    className="w-50 h-100 border-right border-bottom centered bold",
                                                    children="Distance"
                                                ),
                                                html.Div(
                                                    className="w-50 h-100 border-bottom centered"
                                                )
                                            ]
                                        ),
                                        html.Div(
                                            className="w-100 h-12_5 flex-row",
                                            children=[
                                                html.Div(
                                                    className="w-50 h-100 border-right border-bottom centered bold",
                                                    children="Duration"
                                                ),
                                                html.Div(
                                                    className="w-50 h-100 border-bottom centered"
                                                )
                                            ]
                                        ),
                                        html.Div(
                                            className="w-100 h-12_5 flex-row",
                                            children=[
                                                html.Div(
                                                    className="w-50 h-100 border-right border-bottom centered bold",
                                                    children="Average Speed"
                                                ),
                                                html.Div(
                                                    className="w-50 h-100 border-bottom centered"
                                                )
                                            ]
                                        ),
                                        html.Div(
                                            className="w-100 h-12_5 flex-row",
                                            children=[
                                                html.Div(
                                                    className="w-50 h-100 border-right border-bottom centered bold",
                                                    children="Max Speed"
                                                ),
                                                html.Div(
                                                    className="w-50 h-100 border-bottom centered"
                                                )
                                            ]
                                        ),
                                        html.Div(
                                            className="w-100 h-12_5 flex-row",
                                            children=[
                                                html.Div(
                                                    className="w-50 h-100 border-right border-bottom centered bold",
                                                    children="Calories"
                                                ),
                                                html.Div(
                                                    className="w-50 h-100 border-bottom centered"
                                                )
                                            ]
                                        )
                                    ]
                                ),
                                html.Div(
                                    className="w-50 h-100 border-right",
                                    children=[
                                        html.Div(
                                            className="w-100 h-12_5 border-bottom centered",
                                            children="Strength"
                                        ),
                                        html.Div(
                                            className="w-100 h-12_5 flex-row",
                                            children=[
                                                html.Div(
                                                    className="w-50 h-100 border-right border-bottom centered bold",
                                                    children="Average Heart Rate"
                                                ),
                                                html.Div(
                                                    className="w-50 h-100 border-bottom centered"
                                                )
                                            ]
                                        ),
                                        html.Div(
                                            className="w-100 h-12_5 flex-row",
                                            children=[
                                                html.Div(
                                                    className="w-50 h-100 border-right border-bottom centered bold",
                                                    children="Max Heart Rate"
                                                ),
                                                html.Div(
                                                    className="w-50 h-100 border-bottom centered"
                                                )
                                            ]
                                        ),
                                        html.Div(
                                            className="w-100 h-12_5 flex-row",
                                            children=[
                                                html.Div(
                                                    className="w-50 h-100 border-right border-bottom centered bold",
                                                    children="Total Reps"
                                                ),
                                                html.Div(
                                                    className="w-50 h-100 border-bottom centered"
                                                )
                                            ]
                                        ),
                                        html.Div(
                                            className="w-100 h-12_5 flex-row",
                                            children=[
                                                html.Div(
                                                    className="w-50 h-100 border-right border-bottom centered bold",
                                                    children="Duration"
                                                ),
                                                html.Div(
                                                    className="w-50 h-100 border-bottom centered"
                                                )
                                            ]
                                        ),
                                        html.Div(
                                            className="w-100 h-12_5 flex-row",
                                            children=[
                                                html.Div(
                                                    className="w-50 h-100 border-right border-bottom centered bold",
                                                    children="Activity Time"
                                                ),
                                                html.Div(
                                                    className="w-50 h-100 border-bottom centered"
                                                )
                                            ]
                                        ),
                                        html.Div(
                                            className="w-100 h-12_5 flex-row",
                                            children=[
                                                html.Div(
                                                    className="w-50 h-100 border-right border-bottom centered bold",
                                                    children="Rest Time"
                                                ),
                                                html.Div(
                                                    className="w-50 h-100 border-bottom centered"
                                                )
                                            ]
                                        ),
                                        html.Div(
                                            className="w-100 h-12_5 flex-row",
                                            children=[
                                                html.Div(
                                                    className="w-50 h-100 border-right border-bottom centered bold",
                                                    children="Calories"
                                                ),
                                                html.Div(
                                                    className="w-50 h-100 border-bottom centered"
                                                )
                                            ]
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                html.Div(
                    id="averageHeartRateByTimeSlot",
                    className="stats__container flex-column",

                    children=[
                        html.Div(
                            className='stats__container--title border-bottom',
                            children="Average Heart Rate by Time Slot"
                        ),
                        html.Div(
                            className='stats__container--content flex-column',
                            children=[
                                html.Div(
                                    className="stats__card w-100 h-25 flex-row border-bottom",
                                    children=[
                                        html.Div(
                                            className="w-50 h-100 border-right flex-column",
                                            children=[
                                                html.Div(
                                                    className="w-100 h-50 centered",
                                                    children="00:00-03:00"
                                                ),
                                                html.Div(
                                                    className="w-100 h-50 centered bold",
                                                    children="... bpm"
                                                )
                                            ]
                                        ),
                                        html.Div(
                                            className="w-50 h-100 flex-column",
                                            children=[
                                                html.Div(
                                                    className="w-100 h-50 centered",
                                                    children="03:00-06:00"
                                                ),
                                                html.Div(
                                                    className="w-100 h-50 centered bold",
                                                    children="... bpm"
                                                )
                                            ]
                                        )
                                    ]
                                ),
                                html.Div(
                                    className="stats__card w-100 h-25 flex-row border-bottom",
                                    children=[
                                        html.Div(
                                            className="w-50 h-100 border-right flex-column",
                                            children=[
                                                html.Div(
                                                    className="w-100 h-50 centered",
                                                    children="06:00-09:00"
                                                ),
                                                html.Div(
                                                    className="w-100 h-50 centered bold",
                                                    children="... bpm"
                                                )
                                            ]
                                        ),
                                        html.Div(
                                            className="w-50 h-100 flex-column",
                                            children=[
                                                html.Div(
                                                    className="w-100 h-50 centered",
                                                    children="09:00-12:00"
                                                ),
                                                html.Div(
                                                    className="w-100 h-50 centered bold",
                                                    children="... bpm"
                                                )
                                            ]
                                        )
                                    ]
                                ),
                                html.Div(
                                    className="stats__card w-100 h-25 flex-row border-bottom",
                                    children=[
                                        html.Div(
                                            className="w-50 h-100 border-right flex-column",
                                            children=[
                                                html.Div(
                                                    className="w-100 h-50 centered",
                                                    children="12:00-15:00"
                                                ),
                                                html.Div(
                                                    className="w-100 h-50 centered bold",
                                                    children="... bpm"
                                                )
                                            ]
                                        ),
                                        html.Div(
                                            className="w-50 h-100 flex-column",
                                            children=[
                                                html.Div(
                                                    className="w-100 h-50 centered",
                                                    children="15:00-18:00"
                                                ),
                                                html.Div(
                                                    className="w-100 h-50 centered bold",
                                                    children="... bpm"
                                                )
                                            ]
                                        )
                                    ]
                                ),
                                html.Div(
                                    className="stats__card w-100 h-25 flex-row",
                                    children=[
                                        html.Div(
                                            className="w-50 h-100 border-right flex-column",
                                            children=[
                                                html.Div(
                                                    className="w-100 h-50 centered",
                                                    children="18:00-21:00"
                                                ),
                                                html.Div(
                                                    className="w-100 h-50 centered bold",
                                                    children="... bpm"
                                                )
                                            ]
                                        ),
                                        html.Div(
                                            className="w-50 h-100 flex-column",
                                            children=[
                                                html.Div(
                                                    className="w-100 h-50 centered",
                                                    children="21:00-00:00"
                                                ),
                                                html.Div(
                                                    className="w-100 h-50 centered bold",
                                                    children="... bpm"
                                                )
                                            ]
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                html.Div(
                    id="deepSleepAverageHeartCorr",
                    className="stats__container flex-column",
                    children=[
                        html.Div(
                            className='stats__container--title border-bottom',
                            children="Relationship between Deep Sleep and Average Heart Rate during Activities"
                        ),
                        html.Div(
                            className='stats__container--content'
                        )
                    ]
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