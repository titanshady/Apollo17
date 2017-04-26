from django.db import models

class initmes(models.Model):
	descript = models.TextField('Mensagem de Início')

	def __str__(self):
		return self.descript


	class Meta:
		verbose_name = 'Mensagem Inicial'
		verbose_name_plural = 'Mensagens Iniciais'

class mission(models.Model):
	title = models.TextField('Mensagem Principal',)
	text = models.TextField('Texto',)

	def __str__(self):
		return self.title


	class Meta:
		verbose_name = 'Texto: Andamento da Missão'
		verbose_name_plural = 'Texto: Andamento da Missão'		

class valore(models.Model):
	item = models.TextField('Missões',)
	valor = models.CharField('Valor', max_length=100,)

	def __str__(self):
		return self.item


	class Meta:
		verbose_name = 'Conquista da Empresa'
		verbose_name_plural = 'Conquistas da Empresa'

class apollo(models.Model):
	name = models.CharField('Nome', max_length=100,)
	text = models.TextField('Texto',)
	photo = models.ImageField(upload_to='sitio/images/astronautas', verbose_name='Foto',)

	def __str__(self):
		return self.name


	class Meta:
		verbose_name = 'Astronauta Apollo'
		verbose_name_plural = 'Astronautas Apollo'

class gemini(models.Model):
	name = models.CharField('Nome', max_length=100,)
	text = models.TextField('Texto',)
	photo = models.ImageField(upload_to='sitio/images/astronautas', verbose_name='Foto',)

	def __str__(self):
		return self.name


	class Meta:
		verbose_name = 'Astronauta Gemini'
		verbose_name_plural = 'Astronautas Gemini'

class mercury(models.Model):
	name = models.CharField('Nome', max_length=100,)
	text = models.TextField('Texto',)
	photo = models.ImageField(upload_to='sitio/images/astronautas', verbose_name='Foto',)

	def __str__(self):
		return self.name


	class Meta:
		verbose_name = 'Astronauta Mercury'
		verbose_name_plural = 'Astronautas Mercury'

class portfc(models.Model):
	descript = models.TextField('Nome & Descrição da Empresa',)
	logo = models.ImageField(upload_to='sitio/images/portifolio', verbose_name='Logo',)
	
	def __str__(self):
		return self.descript


	class Meta:
		verbose_name = 'Portifólio - Em Construção'
		verbose_name_plural = 'Portifólio - Em Construção'

class portfl(models.Model):
	descript = models.TextField('Nome & Descrição da Empresa',)
	logo = models.ImageField(upload_to='sitio/images/portifolio', verbose_name='Logo',)
	
	def __str__(self):
		return self.descript


	class Meta:
		verbose_name = 'Portifólio - Lançado'
		verbose_name_plural = 'Portifólio - Lançados'
