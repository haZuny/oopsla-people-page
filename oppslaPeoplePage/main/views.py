from django.shortcuts import render, redirect
from . import models
import os

currentDir = str(os.path.abspath(__file__))[:-8]

# Create your views here.

# 기본 페이지
def peoplePage(request, name):
    urlName = name
    # Get people info
    peopleDir = currentDir + 'peoples\\' + urlName + "\\"
    file = open(peopleDir + "profile.txt", "r", encoding='UTF-8')
    
    name = file.readline().split('//')[0].strip()
    position = file.readline().split('//')[0].strip()
    gitId = file.readline().split('//')[0].strip()
    gitUrl = file.readline().split('//')[0].strip()
    imgPath = 'assets/profileImg/' + file.readline().split('//')[0].strip()
    
    pptList = models.SeminarPPT.objects.all()
    if len(pptList) > 5:
        pptList = pptList[::-1]
        pptList = pptList[0:5]
    
    return render(request, "people-page.html", {'urlName': urlName, 'name':name, 'position': position, 'gitId':gitId, 'gitUrl': gitUrl, 'imgPath': imgPath, 'pptList':pptList})

# ppt 목록 페이지
def pptIndexPage(request, name):
    urlName = name
    # Get people info
    peopleDir = currentDir + 'peoples\\' + urlName + "\\"
    file = open(peopleDir + "profile.txt", "r", encoding='UTF-8')
    
    name = file.readline().split('//')[0].strip()
    position = file.readline().split('//')[0].strip()
    gitId = file.readline().split('//')[0].strip()
    gitUrl = file.readline().split('//')[0].strip()
    imgPath = 'assets/profileImg/' + file.readline().split('//')[0].strip()
    
    ppts = models.SeminarPPT.objects.all()
    
    return render(request,"ppt-index.html", {'urlName': urlName, 'name':name, 'position': position, 'gitId':gitId, 'gitUrl': gitUrl, 'imgPath': imgPath, 'pptList':ppts})

# ppt 업로드 페이지
def pptUploadPage(request, name):
    urlName = name
    # Get people info
    peopleDir = currentDir + 'peoples\\' + urlName + "\\"
    file = open(peopleDir + "profile.txt", "r", encoding='UTF-8')
    
    name = file.readline().split('//')[0].strip()
    position = file.readline().split('//')[0].strip()
    gitId = file.readline().split('//')[0].strip()
    gitUrl = file.readline().split('//')[0].strip()
    imgPath = 'assets/profileImg/' + file.readline().split('//')[0].strip()
    
    try:
        if request.method == 'POST':
            pptFile = request.FILES['pptFile']
            print(pptFile)
            pptFileModel = models.SeminarPPT(people = urlName, pptFile = pptFile, pptFileName=pptFile)
            pptFileModel.save()
            print('저장 완료')
            return redirect('http://127.0.0.1:8000/people/'+urlName)
    except:
        print("저장 실패")
        pass
        
    return render(request,"ppt-upload.html", {'urlName': urlName, 'name':name, 'position': position, 'gitId':gitId, 'gitUrl': gitUrl, 'imgPath': imgPath})