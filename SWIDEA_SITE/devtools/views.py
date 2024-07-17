from django.shortcuts import render, redirect

# Create your views here.
import devtools
from devtools.forms import DevtoolsForm
from devtools.models import Devtools
from ideas.models import Ideas


def main(req):
    devtools = Devtools.objects.all()
    ctx = {'devtools': devtools}
    return render(req, 'devtools/list.html', ctx)

def create(req):
    print("This is devtools create")
    if req.method == "GET":
        print("This is devtools create <<get>>")

        form = DevtoolsForm
        ctx = {'form': form}
        return render(req, 'devtools/create.html', ctx)
    form = DevtoolsForm(req.POST, req.FILES)
    if form.is_valid():
        print("form is valid: create")
        form.save()
    else:
        for field in form:
            print("error:", field.name, field.errors)

    return redirect("devtools:main")

def detail(req, pk):
    devtool = Devtools.objects.get(id=pk)

    ideas = Ideas.objects.filter(devtool_id=pk)
    print(ideas)

    ctx = {'devtool': devtool, 'ideas': ideas}
    return render(req, 'devtools/detail.html', ctx)

def details(req, pk):
    idea = Ideas.objects.get(id=pk)
    pk = idea.devtool.id
    devtool = Devtools.objects.get(pk)
    ctx = {'devtool': devtool}
    return render(req, 'devtools/detail.html', ctx)

def delete(req, pk):
    Devtools.objects.get(id=pk).delete()
    return redirect('devtools:main')

def update(req,pk):
    idea = Devtools.objects.get(id=pk)
    if req.method == "GET":
        form = DevtoolsForm(instance=idea)
        ctx = {'form': form, "pk": pk}
        print(pk)
        return render(req, 'devtools/update.html', ctx)
    form = DevtoolsForm(req.POST, req.FILES, instance=idea)
    if form.is_valid():
        print(pk)
        form.save()
        return redirect("devtools:detail", pk=idea.id)

