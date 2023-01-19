from django.shortcuts import render, redirect

from src.app.form.input_form import InputForm


def input(request):

    return render(request, template_name="input.html", context={'ranges': range(0, 7)})

def register(request):

    form = InputForm(request.POST)
    if not form.is_valid():
        return render(request, template_name="input.html", context={'form': form, 'ranges': range(0, 7)})

    return redirect("/input/")
