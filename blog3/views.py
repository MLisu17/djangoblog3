from django.shortcuts import render

#Stworzyliśmy funkcje która pobiera (request) i zwraca (return) wartość wywołaną innej funkcji (render) która złoży w całość nasz szablon HTML
def post_list(request):
    return render(request,'blog3/post_list.html',{})


