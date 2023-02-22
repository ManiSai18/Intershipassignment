import logging
import os
from django.http import HttpResponseRedirect
from django.shortcuts import render
import csv
import io
from django.contrib import messages
from django.urls import reverse
from django.views import View
from .models import Trading 
from .forms import uploadform

# Create your views here.

class IndexView(View):
    def get(self, request):
        data = uploadform()
        return render(request, "mainApp/index.html", {'data': data})

    def post(self,request):


        #get the csv file from input form
        data = uploadform(request.POST, request.FILES)
        dic={}
        finadic=[]
        maindic=[]
        if data.is_valid():


            #save the csv file in data base
            csvfile = Trading(csvfile=request.FILES["csv_file"])
            csvfile.save()
            timeframe = request.POST["time"]
            

            #porcessing the file according to the requirements
            reader = request.FILES["csv_file"].read().decode("utf-8")
            lines = reader.split("\n")
            head = lines[0].split(',')
            lines.pop(0)
            for i in lines:
                lst = i.split(",")
                for j in head:
                    indx = head.index(j)
                    dic.update({j : lst[indx]})
                maindic.append(dic)
            lst = []
            finadic = []
            for i in maindic:
                indx = maindic.index(i)
                if indx % int(timeframe) == 0:
                    lst.append(i)
                    bnk = lst[0][head[0]]
                    date = lst[0][head[1]]
                    tim = lst[0][head[2]]
                    high = max(lst, key=lambda x:float(x[head[4]]))
                    low = min(lst, key=lambda x:float(x[head[5]]))
                    open = lst[0][head[3]]
                    close = lst[-1][head[6]]
                    vol = lst[-1][head[7]]
                    finadic.append({'BANKNIFTY' : bnk, 'DATE': date, 'TIME' : tim, 'OPEN' : open, 'HIGH': high, "LOW": low, 'CLOSE': close, "VOLUME" : vol})
                    lst.clear()
                else:
                    lst.append(i)

        #returning the final output
        return render(request, "mainApp/index.html", {'data': data, 'dic': finadic})
