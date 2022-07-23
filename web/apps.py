from django.apps import AppConfig
import imp


import os
from multiprocessing import context
from django.shortcuts import render
from django.http import JsonResponse
from nevise.main import spell_checking_on_sents,load_pre_model
from hazm import Normalizer
from django.views.decorators.csrf import csrf_exempt

class WebConfig(AppConfig):
    name = 'web'
    vocab_path = os.path.join('nevise/model', 'vocab.pkl')
    model_checkpoint_path = os.path.join('nevise/model', 'model.pth.tar')
    predictor= load_pre_model(vocab_path=vocab_path, model_checkpoint_path=model_checkpoint_path)