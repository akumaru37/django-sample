from django.contrib.auth.decorators import user_passes_test, login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect

from src.app.form.input_form import InputForm


def check(user):
    if user.is_superuser:
        return True
    else:
        raise PermissionDenied


def login_required_403():
    return user_passes_test(check)


# NG @login_required(check)
# OK @login_required_403(check)
@user_passes_test(check)
def input(request):

    return render(request, template_name="input.html", context={'ranges': range(0, 7)})


def register(request):

    if request.POST:
        form = InputForm(request.POST)
        if not form.is_valid():
            return render(request, template_name="input.html", context={'form': form, 'ranges': range(0, 7)})

        for i in range(0, 7):
            print(form.cleaned_data["d[" + str(i)+"]"])

    return redirect("/input/")
