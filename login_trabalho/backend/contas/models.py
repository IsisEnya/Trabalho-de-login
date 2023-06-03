from django.db import models


# Create your models here.

class UserManager(BaseUserManager):


    use_in_migrations = True

    def _create_user(self, email, senha, **aquivos_extras):
        
        print(senha)
        if not email:
            raise ValueError('o email ja esta em uso')
        email = self.normalize_email(email)
        user = self.model(email=email, **aquivos_extras)
        user.set_password(senha)
        user.save(using=self._db)
        print(user)
        print(senha)
        return user

    def create_user(self, email, senha=None, **aquivos_extras):
        print(senha)
      
        aquivos_extras.setdefault('is_staff', False)
        aquivos_extras.setdefault('is_superuser', False)
       
        print(senha)
        return self._create_user(email, senha, **aquivos_extras)

    def create_superuser(self, email, senha, **aquivos_extras):
        
        aquivos_extras.setdefault('is_staff', True)
        aquivos_extras.setdefault('is_superuser', True)

        if aquivos_extras.get('is_staff') is not True:
            raise ValueError('Superuser deve ter is_staff=True.')
        if aquivos_extras.get('is_superuser') is not True:
            raise ValueError('Superuser deve ter is_superuser=True.')

        return self._create_user(email, senha, **aquivos_extras)



class User(AbstractUser):
    cep = models.CharField(max_length=9, blank=True,verbose_name="CEP")
    location = models.CharField(max_length=50, verbose_name="Localidade", blank=True)
    email = models.EmailField(('email '), unique=True,)
    senha = models.CharField(max_length=50, blank=False, null=False, verbose_name="Senha")

    def __str__(self):
        return self.email