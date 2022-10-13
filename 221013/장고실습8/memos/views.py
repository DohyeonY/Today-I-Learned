from django.shortcuts import redirect, render, get_object_or_404
from .models import Travel
from .forms import TravelForm
from django.views.decorators.http import require_POST, require_http_methods, require_safe
# Create your views here.

@require_safe
def index(request):
    memos = Travel.objects.all()
    context = {
        "memos" : memos,
    }
    return render(request,"memos/index.html",context)


@require_http_methods(["GET","POST"])
def create(request):
    if request.method == "POST":
        form = TravelForm(request.POST, request.FILES)
        if form.is_valid():
            memo = form.save()
            return redirect("memos:detail", memo.pk)
    else:
        form = TravelForm()
    context = {
        'form' : form,
    }
    return render(request,'memos/create.html',context)

@require_safe
def detail(request,pk):
    memo = get_object_or_404(Travel,pk=pk)
    context = {
        'memo':memo,
    }
    return render(request,'memos/detail.html',context)

@require_POST
def delete(rquest,pk):
    memo = get_object_or_404(Travel,pk=pk)
    memo.delete()
    return redirect("memos:index")    



@require_http_methods(["GET","POST"])
def update(request,pk):
    memo = get_object_or_404(Travel,pk=pk)
    if request.method == "POST":
        form = TravelForm(request.POST, request.FILES, instance = memo)
        if form.is_valid:
            form.save()
            return redirect("memos:detail",memo.pk)
    else:
        form = TravelForm(instance=memo)
    context = {
        'memo':memo,
        'form':form,
    }
    return render(request,"memos/update.html",context)
