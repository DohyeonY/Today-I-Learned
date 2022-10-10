from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe

from .models import Question, Comment
from .forms import QuestionForm, CommentForm
import random

# Create your views here.
@require_safe
def index(request):
    eithers = Question.objects.order_by('-pk')
    context = {
        'eithers': eithers,
    }
    return render(request, 'eithers/index.html', context)

@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            either = form.save()
            return redirect('eithers:detail', either.pk)
    else:
        form = QuestionForm()
    context = {
        'form': form,
    }
    return render(request, 'eithers/create.html', context)


@require_safe
def detail(request, pk):
    either = get_object_or_404(Question, pk=pk)
    comment_form = CommentForm()
    comments = either.comment_set.all()

    questions = Question.objects.get(pk=pk)
    comm = questions.comment_set.all()

    red_num = comm.filter(pick=1).count()
    blue_num = comm.filter(pick=0).count()

    # print(red_num)
    # print(blue_num)
    
    if red_num + blue_num == 0 :
        redper = 0.0
        bluper = 0.0
    else :
        redper = round(100 * (red_num / (red_num + blue_num)), 1)
        bluper = round(100 * (blue_num / (red_num + blue_num)), 1)
    context = {
        'either': either,
        'comment_form': comment_form,
        'comments': comments,
        'red_num' : red_num,
        'blue_num' : blue_num,
        'redper' : redper,
        'bluper' : bluper,
    }
    return render(request, 'eithers/detail.html', context)


@require_POST
def delete(request, pk):
    either = get_object_or_404(Question, pk=pk)
    either.delete()
    return redirect('eithers:index')


@require_POST
def comments_create(request, pk):
    either = Question.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        # comment.user = request.user
        comment.question_id = either
        comment.save()
    return redirect('eithers:detail', either.pk)

def random_page(request):
    entries = list(Question.objects.all())
    selected_page = random.choice(entries)
    return redirect('eithers:detail', selected_page.pk)

@require_POST
def comments_delete(request, question_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('eithers:detail', question_pk)

@require_http_methods(['GET', 'POST'])
def update(request, pk):
    either = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=either)
        if form.is_valid():
            form.save()
            return redirect('eithers:detail', either.pk)
    else :
        form = QuestionForm(instance=either)
    context = {
        'either': either,
        'form': form,
    }
    return render(request, 'eithers/update.html', context)