from django.shortcuts import render
from .plots import getPlot
from bokeh.resources import CDN

# Create your views here.
def index(request):
    script, div = '<p></p>','<p></p>'
    if request.method == 'POST':
        x_val = request.POST['x']
        y_val = request.POST['y']
        script, div = getPlot(x_val,y_val)
        return render(request,'plots/index.html',{'scripts':script,'div':div,'resources':CDN.render()})
    return render(request,'plots/index.html',{'scripts':script,'div':div,'resources':CDN.render()})