from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
# Create your views here.
from ideas.forms import IdeasForm
from ideas.models import Ideas


def main(req):
    ideas = Ideas.objects.all()
    ctx = {'ideas': ideas}
    return render(req, 'ideas/main.html', ctx)

def create(req):
    if req.method == "GET":
        form = IdeasForm
        ctx = {'form': form}
        return render(req, 'ideas/create.html', ctx)
    form = IdeasForm(req.POST, req.FILES)
    if form.is_valid():
        print("form is valid: create")
        form.save()
    else:
        for field in form:
            print("error:", field.name, field.errors)

    return redirect("ideas:main")

def detail(req, pk):
    idea = Ideas.objects.get(id=pk)
    ctx = {'idea': idea}
    return render(req, 'ideas/detail.html', ctx)

def delete(req, pk):
    Ideas.objects.get(id=pk).delete()
    return redirect('ideas:main')

def update(req,pk):
    idea = Ideas.objects.get(id=pk)
    if req.method == "GET":
        form = IdeasForm(instance=idea)
        ctx = {'form': form, "pk": pk}
        return render(req, 'ideas/update.html', ctx)
    form = IdeasForm(req.POST, req.FILES, instance=idea)
    if form.is_valid():
        form.save()
        return redirect("ideas:detail", pk=idea.id)

def increase_interest(request, pk):
    print("incres")
    if request.method == 'POST':
        idea = get_object_or_404(Ideas, pk=pk)
        idea.interset += 1
        idea.save()
        return JsonResponse({'success': True, 'new_interest': idea.interset})
    return JsonResponse({'success': False})

def decrease_interest(request, pk):
    print("decres")
    if request.method == 'POST':
        idea = get_object_or_404(Ideas, pk=pk)
        idea.interset -= 1
        idea.save()
        return JsonResponse({'success': True, 'new_interest': idea.interset})
    return JsonResponse({'success': False})