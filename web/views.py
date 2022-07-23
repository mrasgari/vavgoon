import imp


import os
from multiprocessing import context
from django.shortcuts import render
from django.http import JsonResponse
from nevise.main import spell_checking_on_sents,load_pre_model
from hazm import Normalizer
from django.views.decorators.csrf import csrf_exempt
from .apps import WebConfig
# Create your views here.

def index(request):
    context={}
  
    
    return render(request,'index.html',context)

@csrf_exempt
def normalize(request):
    if request.method == "POST":
        data = request.POST
        text = data.get("text")
        
        normalizer = Normalizer(punctuation_spacing=False, remove_extra_spaces=False)
        normalizer2 = Normalizer(punctuation_spacing=True, remove_extra_spaces=True)
        
        model, vocab, device  = WebConfig.predictor

        new_out,splitters,greedy_results = spell_checking_on_sents(model, vocab, device, normalizer, text)   
        out_text=normalizer2.normalize(greedy_results)
        return JsonResponse(out_text, safe=False)
    