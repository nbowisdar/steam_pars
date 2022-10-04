from django.shortcuts import render
from django.http import HttpResponse
from tables.models import *

def main(request):
    lootfarm = LootfarmModel.objects.all() #:TODO create good query to db. Watch about django ORM.
    tradegg = TradeggModel.objects.all()
    context = {'lootfarm': lootfarm}
    return render(request, 'main.html', context)
