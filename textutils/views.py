# I hve created this File - Tilak Dave

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    djtext = request.GET.get('text', 'No Text Entered')
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    spacerem = request.GET.get('spacerem', 'off')
    charcount = request.GET.get('charcount', 'off')
    remlines = request.GET.get('remlines', 'off')
    analyzed = ""
    if(removepunc != "on" and fullcaps != "on" and spacerem != "on" and charcount != "on"):
        err = {'purpose': 'Purpose Not Found',
               'analyzed_text': f'An error occurred. Your text was: {djtext}'}
        return render(request, 'analyze.html', err)
    else:
        params = {'purpose': 'Purpose Not Found',
                  'analyzed_text': f'An error occurred. Your text was: {djtext}'}
        if removepunc == "on":
            analyzed = ""
            punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~`'''
            for char in djtext:
                if char not in punctuations:
                    analyzed = analyzed + char
            params = {'purpose': 'Removes Punctuations',
                      'analyzed_text': analyzed}
            djtext = analyzed
        if fullcaps == "on":
            analyzed = ""
            for char in djtext:
                analyzed = analyzed + char.upper()
            params = {'purpose': 'Capitalize Whole Text',
                      'analyzed_text': analyzed}
            djtext = analyzed
        if spacerem == "on":
            analyzed = ""
            for index, char in enumerate(djtext):
                if not (djtext[index] == " " and djtext[index + 1] == " "):
                    analyzed = analyzed + char
            params = {'purpose': 'Remove Spaces', 'analyzed_text': analyzed}
            djtext = analyzed
        if charcount == "on":
            chrcount = ""
            chrcount = len(djtext)
            params = {'purpose': 'Character Count', 'analyzed_text': djtext,
                      'chrcount': f'Total Number of characters are {chrcount}'}
        return render(request, 'analyze.html', params)
