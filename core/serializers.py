from rest_framework.serializers import ModelSerializer
from .models import User

class UserSerializer(ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'first_name', 'last_name', 'email', 'password'] # '__all__'
    extra_kwargs = {
      'password': { 'write_only': True }
    }

  def create(self, d):
    password = d.pop('password', None)
    instance = self.Meta.model(**d)
    if password is not None:
      instance.set_password(password)

    instance.save()
    return instance