# -*- coding: utf-8 -*-
import logging

from django.shortcuts import render

logger = logging.getLogger(__name__)


# Create your views here.
def index(request):
    return render(request, "index.html", {})
