from django.db import models
from django.core.validators import MaxValueValidator
from ckeditor.fields import RichTextField
from colorful.fields import RGBColorField


class initmes(models.Model):
	descript = RichTextField('Mensagem de Início')

	def __str__(self):
		return self.descript


	class Meta:
		verbose_name = '1 - Mensagem Inicial'
		verbose_name_plural = '1 - Mensagens Iniciais'

class mission(models.Model):

	title = models.CharField('Título', max_length=200,)
	text = RichTextField('Texto',)

	def __str__(self):
		return self.title


	class Meta:
		verbose_name = '3 - Andamento da Missão: Texto'
		verbose_name_plural = '3 - Andamento da Missão: Texto'		

class valore(models.Model):
	item = models.CharField('Missões',max_length=50,)
	valor = models.CharField('Valor', max_length=100,)
	

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
	texto = RichTextField()
	tipo = models.CharField(max_length=9, choices=APPROVAL_CHOICES, default='apollo',)
	photo = models.ImageField(upload_to='sitio/images/astronautas', verbose_name='Foto',)
	


	def __str__(self):
		return self.name


	class Meta:
		verbose_name = '5 - Astronauta'
		verbose_name_plural = '5 - Astronautas'

class portfc(models.Model):
	descript = RichTextField('Nome & Descrição da Empresa',)
	logo = models.ImageField(upload_to='sitio/images/portifolio', verbose_name='Logo',)
	
	def __str__(self):
		return self.descript


	class Meta:
		verbose_name = '6 - Portifólio - Em Construção'
		verbose_name_plural = '6 - Portifólio - Em Construção'

class portfl(models.Model):
	descript = RichTextField('Nome & Descrição da Empresa',)
	logo = models.ImageField(upload_to='sitio/images/portifolio', verbose_name='Logo',)
	
	def __str__(self):
		return self.descript
<<<<<<< HEAD


	class Meta:
		verbose_name = '7 - Portifólio - Lançado'
		verbose_name_plural = '7 - Portifólio - Lançados'

class indicador(models.Model):

	name = models.CharField('Nome', max_length=100,)
	percent = models.PositiveIntegerField(primary_key=True, validators=[MaxValueValidator(100)])
	##color = models.CharField(max_length=1, default='1')
	color= RGBColorField()

=======
>>>>>>> refs/remotes/titanshady/master

	def __str__(self):
		return self.name

		
	class Meta:
<<<<<<< HEAD
		verbose_name = '4 - Andamento da Missão: Indicador'
		verbose_name_plural = '4 - Andamento da Missão: Indicadores'
=======
		verbose_name = '7 - Portifólio - Lançado'
		verbose_name_plural = '7 - Portifólio - Lançados'
>>>>>>> refs/remotes/titanshady/master


<<<<<<< HEAD
class choicesportf(models.Model):
	APPROVAL_CHOICES = (
    ('Em Construção', 'Em Construção'),
    ('Lançadas', 'Lançadas'),
	)


	approval = models.CharField(max_length=20, choices=APPROVAL_CHOICES, default='blank',)
	

	def __str__(self):
		return self.approval

=======
	name = models.CharField('Nome', max_length=100,)
	percent = models.PositiveIntegerField(primary_key=True, validators=[MaxValueValidator(100)])
	##color = models.CharField(max_length=1, default='1')
	color= RGBColorField()


	def __str__(self):
		return self.name

		
>>>>>>> refs/remotes/titanshady/master
	class Meta:
		verbose_name = 'Classe de empresa'
		verbose_name_plural = 'Classes de empresas'

class portfcl(models.Model):
<<<<<<< HEAD

=======
>>>>>>> refs/remotes/titanshady/master
	APPROVAL_CHOICES = (
    ('Em Construção', 'Em Construção'),
    ('Lançadas', 'Lançadas'),
	)

	descript = RichTextField('Nome & Descrição da Empresa',)
	logo = models.ImageField(upload_to='sitio/images/portifolio', verbose_name='Logo',)
<<<<<<< HEAD
	andament = models.CharField(max_length=20, choices=APPROVAL_CHOICES, default='Em Construção',)
=======
	andament = models.CharField(max_length=9, choices=APPROVAL_CHOICES, default='const')
>>>>>>> refs/remotes/titanshady/master

	def __str__(self):
		return self.descript


	class Meta:
		verbose_name = '8 - Portifólio (Em Desenvolvimento)'
		verbose_name_plural = '8 - Portifólio (Em Desenvolvimento)'
<<<<<<< HEAD

=======
>>>>>>> refs/remotes/titanshady/master
