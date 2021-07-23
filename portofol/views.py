from django.shortcuts import render
from xhtml2pdf import pisa
from django.template.loader import render_to_string, get_template
from django.template import loader,Context
from django.http import HttpResponse
# Create your views here.
def generate_cv(request):
    template = get_template('cv.html')
    html = template.render()

    file = open('cv.pdf', "w+b")
    pisaStatus = pisa.CreatePDF(html.encode('utf-8'), dest=file,encoding='utf-8')

    file.seek(0)
    pdf = file.read()
    file.close()
    return HttpResponse(pdf, 'application/pdf')

def generate_resume(request):
    template = get_template('resume.html')
    html = template.render()

    file = open('resume.pdf', "w+b")
    pisaStatus = pisa.CreatePDF(html.encode('utf-8'), dest=file,encoding='utf-8')

    file.seek(0)
    pdf = file.read()
    file.close()
    return HttpResponse(pdf, 'application/pdf')

def mycv (request):

    return render(request, 'curiculum.html')