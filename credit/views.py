from django.shortcuts import render
from django.views import generic
from .models import Account, Credit, Client


class ClientView(generic.ListView):
    template_name = 'clients.html'
    context_object_name = 'clients_list'

    def get_queryset(self):
        return Client.objects.all()


class DetailAccountView(generic.DetailView):
    model = Client
    template_name = 'detail_client.html'


class DetailCreditView(generic.DetailView):
    model = Account
    template_name = 'detail_credit.html'


