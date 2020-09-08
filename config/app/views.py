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