from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class UsuarioManager(BaseUserManager):
    def create_user(self, email, nome, sobrenome, rg, cpf, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            nome=nome,
            sobrenome=sobrenome,
            rg=rg,
            cpf=cpf
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nome, sobrenome, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email,
            password=password,
            date_of_birth=date_of_birth
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Usuario(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='endereço de email',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_medico = models.BooleanField(default=False)
    is_cliente = models.BooleanField(default=False)

    rg = models.CharField(max_length=15)
    cpf = models.CharField(max_length=15)

    nome = models.CharField(max_length=60)
    sobrenome = models.CharField(max_length=60)

    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=120)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']

    def get_full_name(self):
        # The user is identified by their email address
        return self.nome + ' ' + self.sobrenome

    def get_short_name(self):
        # The user is identified by their email address
        return self.nome

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    @property
    def is_medico(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_medico

    @property
    def is_cliente(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_cliente


class Cliente(models.Model):
    usuario = models.OneToOneField(User, null=True)

    def __unicode__(self):
        return self.usuario.email

class Medico(models.Model):
    usuario = models.OneToOneField(User, null=True)
    crm = models.CharField(max_length=16)
	duracao_consulta = models.PositiveSmallIntegerField(max_length=15)

    def __unicode__(self):
        return self.usuario.email

class Especializacao(models.Model):
	nome = models.CharField(max_length=60)

	def __unicode__(self):
        return self.nome

class Horario(models.Model):
	medico = models.ForeignKey('Medico')

    dia = models.PositiveSmallIntegerField(blank=False)
    hora_inicio = models.TimeField(blank=False)
    hora_final = models.TimeField(blank=False)

	def __unicode__(self):
        return self.dia + ': ' + hora_inicio + ' - ' + hora_final

class Convenio(models.Model):
	"""docstring for Convenio"""
	cnpj = models.CharField(max_length=16, primary_key=True)
	razao_social = models.CharField(max_length=80)

	def __unicode__(self):
        return self.razao_social

class Consulta(models.Model):
	"""docstring for Convenio"""
    id = UUIDField(primary_key=True, auto=True)

	cliente = models.ForeignKey('Cliente')
	medico = models.ForeignKey('Medico')
	data_hora = models.DateTimeField(blank=False)
	checkin = models.BooleanField(default=False)

	def __unicode__(self):
        return self.cliente + ' ' + self.medico	
