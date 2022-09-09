from django.shortcuts import render
from .plots import getFit
from bokeh.resources import CDN

# Create your views here.
def index(request):
    script, div = '<p></p>','<p></p>'
    fit = ''
    if request.method == 'POST':
        x_val = request.POST['x']
        y_val = request.POST['y']
        script, div, fit = getFit(x_val,y_val)
        return render(request,'linreg/index.html',{'scripts':script,'div':div, 'fit':fit,'resources':CDN.render()})
    return render(request,'linreg/index.html',{'scripts':script,'div':div, 'fit':fit,'resources':CDN.render()})