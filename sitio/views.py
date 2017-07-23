from django.shortcuts import render
from .models import initmes, mission, valore, portfc, portfl, indicador, astronauta


def index(request):
	template_name = 'sitio/index.html'
	slides = initmes.objects.all()
	mis = mission.objects.all()
	val = valore.objects.all()
	porc = portfc.objects.all()
	porl = portfl.objects.all()
	indc = indicador.objects.all()
	astro = astronauta.objects.order_by('tipo')
	skil = mission.objects.filter(tipo='ski')
	miss = mission.objects.filter(tipo='mis')
	port = mission.objects.filter(tipo='por')
	context = {
		'initmess': slides,
		'missions': mis,
		'valores': val,
		'portfcs': porc,
		'portfls': porl,
		'indicadors': indc,
		'astronautas': astro,
		'skil': skil,
		'miss': miss,
		'port': port,
	}

	return render(request, template_name, context)