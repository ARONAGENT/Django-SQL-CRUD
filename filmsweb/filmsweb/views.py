from django.shortcuts import render
from .services import FilmsOperations
def home(request):
    return render(request,"index.html")
    
def adminpage(request):
    return render(request,"DoneAdmin.html")


def admin(request):
    if request.method=="POST":
        id=request.POST.get("userid")
        ps=request.POST.get("password")
        if ps=="admin@123":
            page="DoneAdmin.html"
        else:
            page="FailAdmin.html"
    return render(request,page)

def allfilms(request):
    obj=FilmsOperations()
    data=obj.reportFilms()
    return render(request,"Allfilms.html",{"filmsdata":data})

def addFilmsform(request):
    return render(request,"FilmsForm.html")

def addfilmdata(request):
    if request.method=="POST":
        nm=request.POST.get("filmnm")
        gen=request.POST.get("genre")
        lang=request.POST.get("language")
        relyr=request.POST.get("relyr")
        rate=request.POST.get("rating")
        desc=request.POST.get("desc")
        obj=FilmsOperations()
        obj.addnewfilm(nm,gen,lang,relyr,rate,desc)
        page="Success.html"
    else:
        page="Failure.html"
    return render(request,page)

def searchlangform(request):
    return render(request,"SearchLanguage.html")

def searchlang(request,lang):    
    obj=FilmsOperations()
    dic=obj.retrivelangfilms(lang)
    return render(request,"LangResult.html",dic)

def searchgenform(request):
    return render(request,"SearchGenre.html")

def searchgen(request,gen):
    obj=FilmsOperations()
    dic=obj.retrivegenfilms(gen)
    return render(request,"GenResult.html",dic)

def updaterating(request):
    return render(request,"UpRatingForm.html")

def updateratingstat(request):
    if request.method=="POST":
        id=int(request.POST.get("filmid"))
        uprate=request.POST.get("rating")
        obj=FilmsOperations()
        obj.updateRatingFilms(id,uprate)
    return render(request,"SuccessUpdateRate.html")

def delfilmform(request):
    return render(request,"DeleteFilmForm.html")

def donedeletefilm(request):
    if request.method=="POST":
        id=int(request.POST.get("filmid"))
        obj=FilmsOperations()
        obj.deleteFilmById(id)
    return render(request,"SuccessDelete.html")    
