from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import Chart

def index(request):
    if request.method == 'POST':
        chart_id = int(request.POST['chart_id'])
        chart = Chart.objects.get(id=chart_id)
        file = chart.filename
        chart_html = file.open(mode='r').read()
    else:
        chart_id = ''
        chart_html = ''
    charts = Chart.objects.order_by('shortname')
    context = {'charts': charts, 'chart_html': chart_html, "chart_id": chart_id}
    return render(request, 'mapminder_app/index.html', context)

def explanation(request):
    if request.method == 'POST':
        chart_id = int(request.POST['chart_id'])
        chart = Chart.objects.get(id=chart_id)
        file = chart.filename
        chart_html = file.open(mode='r').read()
    else:
        chart_id = ''
        chart_html = ''
    charts = Chart.objects.order_by('shortname')
    context = {'charts': charts, 'chart_html': chart_html, "chart_id": chart_id}
    return render(request, 'mapminder_app/regression_explanation.html', context)
