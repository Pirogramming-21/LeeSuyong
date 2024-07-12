from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm
# Create your views here.


def review_list(request):
    print("list")
    reviews = Review.objects.all()
    context = {
        'reviews': reviews
    }
    return render(request, 'review_list.html', context)


def review_create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('review_list')  # 리뷰 목록 페이지로 리다이렉트

    return render(request, 'review_create.html')

def review_detail(request, pk):
    review = Review.objects.get(id=pk)
    context = {
        'review' : review
    }
    return render(request, 'review_detail.html', context)

def review_edit(request, pk):
    review = Review.objects.get(id=pk)
    if request.method == "POST":
        print("값을 저장합니다.")

        # form = ReviewForm(request.POST, instance=review)
        # print(form)
        # if form.is_valid():
        print("form == vaild")
        # review_new = form.save()
        # review_new.save()
        review.title = request.POST["title"]
        review.openingDate=request.POST["openingDate"]
        review.genre=request.POST["genre"]
        review.score=request.POST["score"]
        review.runningtime=request.POST["runningtime"]
        review.text=request.POST["text"]
        review.director=request.POST["director"]
        review.actor=request.POST["actor"]
        review.save()

        return redirect('review_detail', pk=review.pk)
    # else:
    #     form = ReviewForm(instance=review)
    return render(request, 'review_edit.html', {'form': review})

def review_delete(request, pk):
    if request.method == "POST":
        print("delete this content")
        review = Review.objects.get(id=pk)
        review.delete()
    return redirect("/")
