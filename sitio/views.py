from django.shortcuts import render
from .models import initmes, mission, valore, portfc, portfl, indicador, astronauta, portfcl, choicesportf

def index(request):
	template_name = 'sitio/index.html'
	slides = initmes.objects.all()
	mis = mission.objects.all()
	val = valore.objects.all()
	porc = portfc.objects.all()
	porl = portfl.objects.all()
	indc = indicador.objects.all()
	portcl = portfcl.objects.all()

	choice = choicesportf.objects.all()


	astro = astronauta.objects.order_by('name')

	context = {
		'initmess': slides,
		'missions': mis,
		'valores': val,
		'portfcs': porc,
		'portfls': porl,
		'indicadors': indc, 
		'astronautas': astro,
		'portfcls': portcl,
		'choicesportfs': choice,
	}

	return render(request, template_name, context)
