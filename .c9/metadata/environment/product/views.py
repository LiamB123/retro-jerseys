{"changed":true,"filter":false,"title":"views.py","tooltip":"/product/views.py","value":"# -*- coding: utf-8 -*-\nfrom __future__ import unicode_literals\n\nfrom django.shortcuts import render\nfrom .models import Product\n\n# Create your views here.\n\ndef all_products(request):\n    products = Products,objects.all()\n    return render(request, 'products.html', {\"products\":products})\n\n","undoManager":{"mark":-2,"position":1,"stack":[[{"start":{"row":9,"column":37},"end":{"row":9,"column":38},"action":"insert","lines":["2"],"id":1}],[{"start":{"row":9,"column":37},"end":{"row":9,"column":38},"action":"remove","lines":["2"],"id":2}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":12,"column":0},"end":{"row":12,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1573486595362}