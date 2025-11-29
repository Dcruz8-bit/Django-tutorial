from django.shortcuts import render

def post_list(request):
    return render(request, 'books/post_list.html', {})

