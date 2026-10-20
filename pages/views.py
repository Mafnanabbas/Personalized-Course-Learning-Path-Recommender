from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html')
def create_account(request):
    return render(request, 'create_account.html')