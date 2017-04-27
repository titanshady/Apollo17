from django.db import models
from django.core.validators import MaxValueValidator
from ckeditor.fields import RichTextField

class initmes(models.Model):
	descript = models.TextField('Mensagem de Início')
	content = RichTextField(blank=True, null=True)

	def __str__(self):
		return self.descript


	class Meta:
		verbose_name = '1 - Mensagem Inicial'
		verbose_name_plural = '1 - Mensagens Iniciais'

class mission(models.Model):
	title = models.TextField('Mensagem Principal',)
	text = models.TextField('Texto',)
	content = RichTextField(blank=True, null=True)

	def __str__(self):
		return self.title


	class Meta:
		verbose_name = '3 - Andamento da Missão: Texto'
		verbose_name_plural = '3 - Andamento da Missão: Texto'		

class valore(models.Model):
	item = models.TextField('Missões',)
	valor = models.CharField('Valor', max_length=100,)
	content = RichTextField(blank=True, null=True)

	def __str__(self):
		return self.item


	class Meta:
		verbose_name = '2 - Conquista da Empresa'
		verbose_name_plural = '2 - Conquistas da Empresa'

class astronauta(models.Model):
	APPROVAL_CHOICES = (
    ('apollo', 'Apollo'),
    ('gemini', 'Gemini'),
    ('mercury', 'Mercury'),
	)

	name = models.CharField('Nome', max_length=100,)
	text = models.TextField('Texto',)
	tipo = models.CharField(max_length=9, choices=APPROVAL_CHOICES, default='apollo')
	photo = models.ImageField(upload_to='sitio/images/astronautas', verbose_name='Foto',)
	content = RichTextField(blank=True, null=True)

	def __str__(self):
		return self.name


	class Meta:
		verbose_name = '5 - Astronauta'
		verbose_name_plural = '5 - Astronautas'

class portfc(models.Model):
	descript = models.TextField('Nome & Descrição da Empresa',)
	logo = models.ImageField(upload_to='sitio/images/portifolio', verbose_name='Logo',)
	content = RichTextField(blank=True, null=True)
	
	def __str__(self):
		return self.descript


	class Meta:
		verbose_name = '6 - Portifólio - Em Construção'
		verbose_name_plural = '6 - Portifólio - Em Construção'

class portfl(models.Model):
	descript = models.TextField('Nome & Descrição da Empresa',)
	logo = models.ImageField(upload_to='sitio/images/portifolio', verbose_name='Logo',)
	content = RichTextField(blank=True, null=True)
	
	def __str__(self):
		return self.descript


	class Meta:
		verbose_name = '7 - Portifólio - Lançado'
		verbose_name_plural = '7 - Portifólio - Lançados'

class indicador(models.Model):

	APPROVAL_CHOICES = (
    ('1', 'Azul'),
    ('2', 'Laranja'),
    ('3', 'Amarelo'),
    ('4', 'Marrom'),
	)

	name = models.CharField('Nome', max_length=100,)
	percent = models.PositiveIntegerField(primary_key=True, validators=[MaxValueValidator(100)])
	color = models.CharField(max_length=1, choices=APPROVAL_CHOICES, default='1')
	content = RichTextField(blank=True, null=True)

	def __str__(self):
		return self.name


	class Meta:
		verbose_name = '4 - Andamento da Missão: Indicador'
		verbose_name_plural = '4 - Andamento da Missão: Indicadores'


class portfcl(models.Model):

	APPROVAL_CHOICES = (
    ('const', 'Em Construção'),
    ('lanc', 'Lançados'),
	)

	descript = models.TextField('Nome & Descrição da Empresa',)
	logo = models.ImageField(upload_to='sitio/images/portifolio', verbose_name='Logo',)
	andament = models.CharField(max_length=9, choices=APPROVAL_CHOICES, default='const')
	content = RichTextField(blank=True, null=True)

	def __str__(self):
		return self.descript


	class Meta:
		verbose_name = '8 - Portifólio (Em Desenvolvimento)'
		verbose_name_plural = '8 - Portifólio (Em Desenvolvimento)'
