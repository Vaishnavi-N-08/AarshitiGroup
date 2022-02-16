from django.shortcuts import render, redirect
from scholarship.models import Scholar, counselor

def scholarship(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        email = request.POST['email']
        secemail = request.POST['secemail']
        number = request.POST['number']
        address = request.POST['address']
        collegename = request.POST['collegename']
        grno = request.POST['grno']
        marksheet = request.FILES['marksheet']
        feereceipt = request.FILES['feereceipt']
        new_scholar = Scholar(fullname=fullname, email=email, secemail=secemail, number=number,
                              address=address, collegename=collegename, grno=grno, marksheet=marksheet, feereceipt=feereceipt)
        new_scholar.save()
        return redirect('home')
    else:
        return render(request, "scholarship.html")

def counselling(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        number = request.POST['number']
        course = request.POST['course']
        proof = request.FILES['proof']
        email = request.POST['email']
        address = request.POST['address']
        new_counselor = counselor(fullname=fullname, email=email,
                                  number=number, course=course, proof=proof, address=address)
        new_counselor.save()
        return redirect('counselling')
    else:
        return render(request, "counselling.html")
