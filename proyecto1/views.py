from django.http import HttpResponse
from django.template import Template, Context, loader

def saludo(request):
	return HttpResponse("Hola Django - Coder")
def segunda_vista(request):
	return HttpResponse("ta ez")
def probando_template(request):
	diccionario = {
		"nombre": "Lionel",
		"apellido": "Messi",
		"notas": [4,6,2,10,9]
	}
	mi_html = open("./proyecto1/templates/template1.html")
	plantilla = Template(mi_html.read())
	mi_html.close()
	mi_contexto = Context(diccionario)
	documento = plantilla.render(mi_contexto)
	return HttpResponse(documento)
def probando_template2(request):
	diccionario = {
		"nombre": "Lionel",
		"apellido": "Messi",
		"notas": [4,6,2,10,9]
	}

	plantilla = loader.get_template("template1.html")
	documento = plantilla.render(diccionario)

	return HttpResponse(documento)