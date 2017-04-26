from django.shortcuts import render

from .models import initmes, mission, valore, apollo, gemini, mercury, portfc, portfl

def index(request):
	template_name = 'sitio/index.html'
	slides = initmes.objects.all()
	mis = mission.objects.all()
	val = valore.objects.all()
	apol = apollo.objects.all()
	gemi = gemini.objects.all()
	merc = mercury.objects.all()
	porc = portfc.objects.all()
	porl = portfl.objects.all()
	context = {
		'initmess': slides,
		'missions': mis,
		'valores': val,
		'apollos': apol,
		'geminis': gemi,
		'mercurys': merc,
		'portfcs':porc,
		'portfls':porl,
	}

	return render(request, template_name, context)
