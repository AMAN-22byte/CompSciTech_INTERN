# from django.http import HttpResponse
# from django.shortcuts import render

# def calculate(request):
    # c=''
    # if request.method == "POST":
    #     try:
    #         if request.method=="POST":
    #             n1=float(request.POST.get('num1'))
    #             n2=float(request.POST.get('num2'))
    #             opr=request.POST.get('opr')
    #             if(opr=="+"):
    #                 c=n1+n2
    #             elif opr=="-":
    #                 c=n1-n2
    #             elif opr=="*":
    #                 c=n1*n2
    #             elif opr=="/":
    #                 c=n1/n2

    #     except:
    #         c="invalid.."
    # return render(request,"index.html",{'c':c})

from django.shortcuts import render

def calculator(request):
    c=''
    if request.method == "POST":
        try:
            if request.method=="POST":
                n1=float(request.POST.get('num1'))
                n2=float(request.POST.get('num2'))
                opr=request.POST.get('opr')
                if(opr=="+"):
                    c=n1+n2
                elif opr=="-":
                    c=n1-n2
                elif opr=="*":
                    c=n1*n2
                elif opr=="/":
                    c=n1/n2

        except:
            c="invalid.."
    return render(request,"index.html",{'c':c})
