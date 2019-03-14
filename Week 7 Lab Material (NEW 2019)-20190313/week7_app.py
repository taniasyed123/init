from flask import Flask, render_template, request, jsonify
import plotly.graph_objs as go
from plotly.utils import PlotlyJSONEncoder
import json
import requests



app = Flask(__name__)


crime_url_template = 'https://data.police.uk/api/crimes-street/all-crime?lat={lat}&lng={lng}&date={data}'
categories_url_template = 'https://data.police.uk/api/crime-categories?date={date}'


@app.route('/crimestat',  methods=['GET'])
def crimechart():
    my_latitude = request.args.get('lat','51.52369')
    my_longitude = request.args.get('lng','-0.0395857')
    my_date = request.args.get('date','2018-11')

    # compute  crime_category_stats
    # compute crime_outcome_stats


    graphs = [
            dict(
                data=[
                    dict(
                        values=list(crime_category_stats.values()),
                        labels=list(crime_category_stats.keys()),
                        hole=.4,
                        type='pie',
                        name='Category'
                    ),
                ],
                layout=dict(
                    title='Crime Categoty Stats During {}'.format(my_date)
                )
            ),
            dict(
                data=[
                    dict(
                        values=list(crime_outcome_stats.values()),
                        labels=list(crime_outcome_stats.keys()),
                        hole=.4,
                        type='pie',
                        name='Outcome'
                    ),
                ],
                layout=dict(
                    title='Crime Outcome Stats During {}'.format(my_date)
                )
            ),
        ]

    ids = ['graph-{}'.format(i) for i, _ in enumerate(graphs)]

    graphJSON = json.dumps(graphs, cls=PlotlyJSONEncoder)
    return render_template('plotholder.html',ids=ids,graphJSON=graphJSON)



if __name__=="__main__":
    app.run(port=8080, debug=True)
