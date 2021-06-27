from django.http import HttpResponse
from django.shortcuts import render
from .models import UspsServices

def hello(request):

   #These objects will be created from Database
   ''' service1 = UspsServices()
   service1.serviceName = "Freight Auction"
   service1.serviceDescription = "Suppliers have the ability to accept or decline transportation based on a set rate."
   service1.accessFlag = True
   service1.id = 1

   service2 = UspsServices()
   service2.serviceName = "Contract Services"
   service2.serviceDescription = "Suppliers have the ability to manage their contractual relationship with the US Postal Service including manifests (schedule), invoice and payment status."
   service2.accessFlag = False
   service2.id = 2

   service3 = UspsServices()
   service3.serviceName = "Transportation Procurement Services"
   service3.serviceDescription = "Supplier has the ability to manage Transportation Procurement Services here"
   service3.accessFlag = False
   service3.id = 3

   service4 = UspsServices()
   service4.serviceName = "Automated Forms"
   service4.serviceDescription = "Supplier has the ability to manage . Automated Forms (Surface Transportation Automated Forms) here"
   service4.accessFlag = False
   service4.id = 4

   service5 = UspsServices()
   service5.serviceName = "Transportation Visibility & Performance"
   service5.serviceDescription = "Supplier has the ability to manage Transportation Visibility &amp; Performance here... (refine description)."
   service5.accessFlag = False
   service5.id = 5
'''
   serviceList = UspsServices.objects.all()
   #[service1, service2, service3, service4, service5]
 
   return render(request, 'bpgtemplate.html',{"serviceList":serviceList})
