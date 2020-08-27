from django.shortcuts import render

def indexfunc(request):
    context = {
        'hello': 'こんにちは'
    }
    return render(request, 'app/index.html', context)