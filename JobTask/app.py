from flask import Flask, render_template
from Image import get_df
import pandas as pd
import plotly
import plotly.express as px
import json

app = Flask(__name__)


@app.route("/")
def home():
    #Using an HTML template to render the front end result
    return render_template('home.html', graphJSON = create_plot())

@app.route("/data", methods = ['POST', 'GET'])
def call():
    #print("here at data")
    #Retrieving the Dataframe in JSON format from the method defined in Image.py
    data_json = get_df()
    return create_plot(data_json)


def create_plot(data_json = None):
    
    #Making sure the value is not "None"
    if(data_json):
        #Assigning the data in JSON format to a private variable
        json_ = data_json
        #Reading the JSON data 
        df = pd.read_json(json_, orient = 'split')
        
        #Plotting the graph using the JSON data with Plotly
        fig = px.line(df, x = 'a', y = 'b')
        
        #fig.show()
        #Using the image object to generate data required for the graph in HTML
        graphJSON = json.dumps(fig, cls = plotly.utils.PlotlyJSONEncoder)
        return graphJSON
    return None
    
   
    
    
if __name__ == "__main__": 
    app.run(debug = False)
    