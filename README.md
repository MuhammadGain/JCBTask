# JCBTask

This repository contains a folder named "Job Task" which contains the code files for the test task provided by J&C Bachmann. The task consists of a total of 3 code files

* Image.py
* app.py
* home.html

## Image.py
This file contains the method called `get_df()`. Here a Dataframe is generated using the Pandas library which consists of two columns of data "a", 
consisting of random values in the range of 0-100, and "b", consisting of the Modulo 10 of the respective values from the column "a". This dataframe is then returned in 
JSON format
 
## app.py

This file contains the flask app with the necessary routes required for the web application. The first route `/` renders the home.html file. 
The second route `/data` consists of two methods, namely `call()` and `create_plot()`. The `call()` method retreives the dataframe generated 
using the `get_df()` function defined in Image.py, and then calls the `create_plot(data_json = none)` method which takes in a dataframe object, reads it and then 
plots it using the Plotly library. Finally returning the image in JSON format.

## home.html
This file makes use of the Cloud Delivery Network(CDN) so that there is no need for setup required at the user end. CDNs for Bootstrap(CSS and JS), JQuery, 
JQuery Ajax and Plotly. The article from [Towards Data Science](https://towardsdatascience.com/an-interactive-web-dashboard-with-plotly-and-flask-c365cdec5e3f) is used
as the inspiration for this task.

When the page is loaded, all the libraries are loaded as well. After that the code from line 58 to 61 is loaded only once. The page consists of a `<div>` for a 
bootstrap card and a `<div>` required by Plotly to construct a chart. 

The `<script>` from line 18 to 39 is also loaded. It executes on each instance of "Button Click" It uses Asynchronous Javascript and XML(AJAX) to retrieve 
the JSON data from the route `/data` and use Plotly to generate an interactive graph. The method `get_df()` is executed on each instance of "Button Click", therefore 
the graph that is generated has a new Dataframe each instance, leading to a new image each time.

# Excecuting the code.

When the flask app is running, if you open your browser to `http://127.0.0.1:5000/` you should see the front end of the web app at runtime. Due to the following 
code snippet there is no graph present when the website loads. 
```
<script type='text/javascript'>
  var graphs = {{graphJSON | safe}};
  Plotly.plot('chart', graphs,{staticPlot: true});
</script>
```
Upon clicking the **Load Graphic** button, the graphic loads asynchronously.  Upon each consequent click, the graphic refreshes with a new 
Dataframe as its input.


