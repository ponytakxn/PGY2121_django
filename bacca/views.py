from django.shortcuts import render

# Create your views here.
def index(request):
  context={}
  return render(request, 'bacca/index.html', context)

def praga(request):
  context={}
  return render(request, 'bacca/views/praga.html', context)