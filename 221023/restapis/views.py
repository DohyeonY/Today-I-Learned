from django.shortcuts import render

# Create your views here.


def apilist(request) :
    apis = Api.objects.all()
    context = {
        'apis' : apis,
    }
    return render(request, 'restapis/apilist.html', context)


