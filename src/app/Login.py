from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView


class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['placeholder'] = field.label#全てのフォームの部品にplaceholderを定義して、入力フォームにフォーム名が表示されるように指定する


class Login(LoginView):
    template_name = 'login.html'
    form_class = LoginForm

class Logout(LogoutView):
    template_name = 'logout.html'