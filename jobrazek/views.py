from django.shortcuts import render, redirect, reverse
from django.views import View
from .models import Jobrazek
from .forms import ObrazkowyForm
# Create your views here.

class JobrazkowyView(View):
    def get(self, request):
        ctx = {"Jobrazki": Jobrazek.objects.all(), 'form': ObrazkowyForm()}
        return render(request, "jobrazek.html", context=ctx)
    def post(self, request):
        form = ObrazkowyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect(reverse('main'))
