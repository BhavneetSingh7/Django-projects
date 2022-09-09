from bokeh.plotting import figure
from bokeh.embed import components

def getPlot(x,y):
    x,y = x.split(','),y.split(',')
    x = [float(e) for e in x]
    y = [float(e) for e in y]
    # create a new plot with a title and axis labels
    p = figure(title="Simple line example", x_axis_label='x', y_axis_label='y')
    # add a line renderer with legend and line thickness to the plot
    p.line(x, y, legend_label="Temp.", line_width=2)
    script, div = components(p)
    return (script,div)

# prepare some data
# x_val = '1,2,3,4'
# y_val = '1,2,3,4'
# script, div = getPlot(x_val,y_val)
# print(script)
# print(div)