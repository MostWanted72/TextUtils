#I have created this file - pagidi
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    student = {
        "name": "Nina",
        "place": "Moon"
    }
    return render(request, 'index2.html', student)

def home(request):
    return HttpResponse("""about pagidi bhai <br/> <a href = "/">back </a>""")

def navigation(request):
    return render(request, 'navigation.html')

def Analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcapital = request.POST.get('fullcapital', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    chartercounter = request.POST.get('chartercounter', 'off')

    if removepunc == "on":
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {
            'purpose': 'Remove Punctuations',
            'Analyzed_text' : analyzed,
            "char_count": ''
        }
        djtext = analyzed

    if fullcapital == "on":
        analyzed = djtext.upper() 
        params = {
            'purpose': 'changed to uppercase',
            'Analyzed_text' : analyzed,
            "char_count": ''
        }
        djtext = analyzed

    if newlineremover == "on":
        analyzed = ''
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        params = {
            'purpose': 'newline has been removed',
            'Analyzed_text' : analyzed,
            "char_count": ''
        }
        djtext = analyzed

    if extraspaceremover == "on":
        analyzed = ''
        for index, char in  enumerate(djtext):
            if djtext[index] == " " and djtext[index + 1] == " ":
                pass
            else:
                analyzed = analyzed + char
        params = {
            'purpose': 'spaces has been removed ',
            'Analyzed_text' : analyzed,
            "char_count": ""
        }

        djtext = analyzed

    if chartercounter == "on":
        charcout = len(djtext)
        params = {
            'purpose': 'the number of characters ',
            'Analyzed_text' : analyzed,
            "char_count": charcout
        }
    
    if removepunc =="off" and fullcapital =="off" and newlineremover == "off" and extraspaceremover == "off" and chartercounter  == "off":
        return HttpResponse("Error")

    return render(request, 'Analyze2.html', params)