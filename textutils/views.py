# I have created this file

from os import remove
from django.http import HttpResponse
from django.shortcuts import render

def removePunctuations(words):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^*&_~'''
    newWord = ""
    
    for letter in words:
        if letter not in punctuations:
            newWord += letter
    return newWord

def removeNewLine(words):
    newWord = ""
    for letter in words:
        if letter != '\n' and letter != '\r':
            newWord += letter
    return newWord

def removeExtraSpace(words):
    newWord = ""
    for index, letter in enumerate(words):
        if not(words[index] == ' ' and words[index+1] == ' '):
            newWord += letter
    return newWord

def index(request):
    return render(request, "index.html")
    # return HttpResponse("Home")

def analyse(request):
    # get the values of textarea
    words = request.POST.get('words', 'default')

    # checkbox values
    removePun = request.POST.get('removepun', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('spaceremover', 'off')
    charcount = request.POST.get('charcount', 'unchecked')
    
    # removePun = request.GET.get('removepun', 'off')
    # fullcaps = request.GET.get('fullcaps', 'off')
    # newlineremover = request.GET.get('newlineremover', 'off')
    # extraspaceremover = request.GET.get('spaceremover', 'off')
    # charcount = request.GET.get('charcount', 'off')
    
    originalWord = words
    charCounter = ""
    if removePun == 'on':
        words = removePunctuations(words)
    if fullcaps == 'on':
        words = words.upper()
    if newlineremover == 'on':
        words = removeNewLine(words)
    if extraspaceremover == 'on':
        words = removeExtraSpace(words)
    if charcount == 'on':
        charCounter = "Characters: " + str(len(words))
        

    value = {'purpose': 'Remove Punctuations', 'analysed_text': words, 'numOfChar': charCounter}
    # Analyse the text
    return render(request, "analyse.html", value)











'''def index(request):
    value = {'name': "Amit", 'place': "Moon"}
    return render(request, "index.html", value)
    return HttpResponse("""<h1> Hello </h1> <a href="https://www.youtube.com" target="_blank"> Youtube </a>""")

 def about(request):
    return HttpResponse("About this website")

def removePun(request):
    # Get the text
    words = request.GET.get("words", "default")
    # Analyse the text
    return HttpResponse("""<a href='/' style='text-decoration:none'> <button> Back </button> </a> Remove Punctuation""")

def capitalFirst(request):
    return HttpResponse("""<a href='removepun' style='text-decoration:none'> <button> Back </button> </a> Capitalize First""")
    
def newLineRemove(request):
    return HttpResponse("""<a href='capitalizefirst' style='text-decoration:none'> <button> Back </button> </a> New Line Remover""")

def spaceRemover(request):
    return HttpResponse("""<a href='newlineremove' style='text-decoration:none'> <button> Back </button> </a> Space Remover""")

def charCount(request):
    return HttpResponse("""<a href='spaceremover' style='text-decoration:none'> <button> Back </button> </a> Character Counter""") '''