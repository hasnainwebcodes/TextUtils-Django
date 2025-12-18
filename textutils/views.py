## I created this File- Hasnain
from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request,'index.html')
def analyze(request):
    first= request.GET.get('text', 'default')
    removepunc= request.GET.get('removepunc','off')
    fullcap= request.GET.get('fullcap','off')
    nline= request.GET.get('nline','off')
    space= request.GET.get('space','off')
    count= request.GET.get('count','off')
    analyzed= first
    purpose= "No actions selected"
    if removepunc == "on" :
        puncs= '''!@#$%^&*()-_+=|[]{};:'"\,<>./?~`'''
        analyzed= ""
        purpose= "Removed Punctuation"
        for char in first:
            if char not in puncs :
                analyzed= analyzed +char
    elif (fullcap == "on"):
        analyzed= ""
        purpose= "Uppercase All"
        for char in first:
            analyzed= analyzed + char.upper()
    elif (nline == "on"):
        analyzed= ""
        purpose= "Remove new lines"
        for char in first:
            if char != "\n":
                analyzed= analyzed + char
    elif (space == "on"):
        analyzed= ""
        purpose= "Remove extra spaces"
        try:
            for index, char in enumerate(first):
                if not(first[index] == " " and first[index+1] == " "):
                    analyzed= analyzed + char
        except Exception as e:
            analyzed= "Something bad happen"
    elif (count == "on"):
        analyzed= ""
        purpose= "Count the characters"
        try:
                analyzed= "Your Characters are "+len(first)
        except Exception as e:
            analyzed= "Something bad happen"
    params= {'purpose': purpose, 'analyzed_text': analyzed}
    return render(request, 'analyzed.html', params)

