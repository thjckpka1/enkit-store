from django.shortcuts import render, get_object_or_404
from .models import Software

def home(request):
    softwares = Software.objects.all()  # Lấy tất cả thay vì [:5]
    return render(request, 'store/home.html', {'softwares': softwares})

def software_detail(request, pk):
    software = get_object_or_404(Software, pk=pk)
    return render(request, 'store/detail.html', {'software': software})