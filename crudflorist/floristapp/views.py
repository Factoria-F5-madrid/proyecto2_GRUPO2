from django.shortcuts import render


# Create your views here.
def mi_error_404(request, exception):
    return render(request, "404.html", status=404)
