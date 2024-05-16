from django.contrib import messages
from django.shortcuts import render

def my_view(request):
    # Your view logic here
    messages.success(request, 'This is a success message!')
    return render(request, 'template_name.html')
