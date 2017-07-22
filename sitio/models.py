from django.db import models
from django.core.validators import MaxValueValidator
from colorful.fields import RGBColorField


class initmes(models.Model):
	descript = models.TextField('Texto')

	def __str__(self):
		return self.descript


	class Meta:
		verbose_name = '1 - Mensagem Inicial'
		verbose_name_plural = '1 - Mensagens Iniciais'

class mission(models.Model):

	title = models.CharField('Título', max_length=200,)
	text = models.TextField('Texto')

	skills = 'ski' 
	objective = 'mis'
	portifolio = 'por'

	Tipo = (
		(skills, 'Astronautas'),
		(objective, 'Missão'),
		(portifolio, 'Portifólio'),
	)
	tipo = models.CharField(max_length = 3, choices = Tipo, default = skills)

	def is_upperclass(self):
		return self.tipo in (self.skills,self.objective,self.portifolio)

	def __str__(self):
		return self.title


	class Meta:
		verbose_name = '3 - Texto do Site'
		verbose_name_plural = '3 - Textos do Site'		

class valore(models.Model):
	item = models.CharField('Missões',max_length=50,)
	valor = models.CharField('Valor', max_length=100,)
	

	def __str__(self):
		return self.item


	class Meta:
		verbose_name = '2 - Meta da Missão'
		verbose_name_plural = '2 - Metas da Missão'

class astronauta(models.Model):
	APPROVAL_CHOICES = (
    ('apollo', 'Apollo'),
    ('gemini', 'Gemini'),
    ('mercury', 'Mercury'),
	)

	name = models.CharField('Nome', max_length=100,)
	texto = models.TextField('Texto')
	tipo = models.CharField(max_length=9, choices=APPROVAL_CHOICES, default='apollo',)
	photo = models.ImageField(upload_to='sitio/images/astronautas', verbose_name='Foto',)
	


	def __str__(self):
		return self.name


	class Meta:
		verbose_name = '5 - Astronauta'
		verbose_name_plural = '5 - Astronautas'

class portfc(models.Model):
	descript = models.TextField('Nome & Descrição da Empresa',)
	logo = models.ImageField(upload_to='sitio/images/portifolio', verbose_name='Logo',)
	
	def __str__(self):
		return self.descript


	class Meta:
		verbose_name = '6 - Portifólio - Em Construção'
		verbose_name_plural = '6 - Portifólio - Em Construção'

class portfl(models.Model):
	descript = models.TextField('Nome & Descrição da Empresa',)
	logo = models.ImageField(upload_to='sitio/images/portifolio', verbose_name='Logo',)
	
	def __str__(self):
		return self.descript


	class Meta:
		verbose_name = '7 - Portifólio - Lançado'
		verbose_name_plural = '7 - Portifólio - Lançados'

class indicador(models.Model):

	name = models.CharField('Nome', max_length=100,)
	meta2 = models.PositiveIntegerField('Meta')
	atual2 = models.PositiveIntegerField('Atual')
	color= RGBColorField()


	def __str__(self):
		return self.name

		
	class Meta:
		verbose_name = '4 - Andamento da Missão: Indicador'
		verbose_name_plural = '4 - Andamento da Missão: Indicadores'




