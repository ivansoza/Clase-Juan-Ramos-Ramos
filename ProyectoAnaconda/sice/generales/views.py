from django.shortcuts import render, HttpResponse

# Create your views here.


def hola_mundo(request):
    return HttpResponse("""
                             <h1 style="color: aquamarine;"> Hola BEBE </h1>
                             <p style="color: brown;">Lorem ipsum dolor sit amet consectetur adipisicing elit. Aspernatur beatae, quidem minima rerum tenetur tempore est sit, molestias nostrum voluptatibus nulla. Inventore corporis consequatur expedita, amet sunt aut sint minus?</p>
                        """)

def index(request):
    return HttpResponse("""<h1 style="color: blue;">ola</h1>""")