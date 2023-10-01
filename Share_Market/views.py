from django.shortcuts import render
# Create your views here.

def stocks(request):
    return render(request,"Share_Market/Stocks.html")

def company(request):
    return render(request,'Share_Market/company.html')