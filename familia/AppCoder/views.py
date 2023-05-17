from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import familia


# Create your views here.
def templates(request):
    contexto = {
        "familiares": familia.objects.all()
    }
    http_responde = render(
        request=request,
        template_name= 'familia/index.html',
        context=contexto
    )
    return http_responde