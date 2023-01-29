from django.shortcuts import render
from django.views import View

# Create your views here.
class indexView(View):
    template_name="students/index.html"

    def get(self, request):
        return render(request, self.template_name)
