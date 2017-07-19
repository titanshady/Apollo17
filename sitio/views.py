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
	indc2 = indicador.objects.all().first()
	astro = astronauta.objects.order_by('name')
	skil = mission.objects.filter(tipo='ski')
	miss = mission.objects.filter(tipo='mis')
	port = mission.objects.filter(tipo='por')
	percent = ( indc2.atual2 / indc2.meta2) * 100
	percent = int(percent)
	context = {
		'initmess': slides,
		'missions': mis,
		'valores': val,
		'portfcs': porc,
		'portfls': porl,
		'indicadors': indc,
		'indicadors2':indc2, 
		'astronautas': astro,
		'skil':skil,
		'miss':miss,
		'port':port,
		'percents':percent,
	}

	return render(request, template_name, context)