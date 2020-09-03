# I have created this file Abhi

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')


def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    capfirst = request.POST.get('capfirst', 'off')
    linerem = request.POST.get('newlinerv', 'off')
    sprem = request.POST.get('sprem', 'off')
    charcount = request.POST.get('charcount', 'off')

    if removepunc=="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if (linerem == "on"):
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
        params = {'purpose': 'New Line Remover', 'analyzed_text': analyzed}
        djtext = analyzed

    if (sprem == "on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose': 'Extra Soace Remover', 'analyzed_text': analyzed}
        djtext = analyzed

    if (charcount == "on"):
        count = 0
        for char in djtext:
            if not(char == " "):
                count +=1
        params = {'purpose': 'Number of Character', 'analyzed_text': count}


    if(capfirst=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}

    if (removepunc != "on" and linerem != "on" and sprem != "on" and capfirst != "on" and charcount != "on"):
        return HttpResponse("please select any operation and try again")


    return render(request, 'analyze.html', params)


