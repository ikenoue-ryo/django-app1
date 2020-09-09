from django.shortcuts import render

def indexfunc(request):
    context = {
        'hello': 'こんにちは'
    }
    return render(request, 'app/index.html', context)



def profilefunc(request):
    context = {
        'hello': 'こんにちは'
    }
    return render(request, 'app/create_profile.html', context)




def post(request):
    context = {
        'hello': 'こんにちは'
    }
    return render(request, 'app/post.html', context)


def new(request):
    context = {
        'hello': 'こんにちは'
    }
    return render(request, 'app/new.html', context)


def listfunc(request):
    context = {
        'hello': 'こんにちは'
    }
    return render(request, 'app/car_list.html', context)


def detailfunc(request, pk):
    context = {
        'hello': 'こんにちは'
    }
    return render(request, 'app/car_detail.html', context)