from django.shortcuts import render


def mainpage(request):
    data = {
        "data": [
            {
                "button_link": "admin",
                "name": "Заявки",
                "overview": "Работа с заявками на оборудование",
                "img_src": "{% static '1.png' %}"
            },
            {
                "button_link": "#",
                "name": "Персонал",
                "overview": "Работа с базами персонала",
                "img_src": "{% static '2.png' %}"
            },
            {
                "button_link": "#",
                "name": "Финансы",
                "overview": "Работа с базами финансов",
                "img_src": "{% static '3.png' %}"
            },
            {
                "button_link": "#",
                "name": "База знаний",
                "overview": "Работа с базами знаний",
                "img_src": "{% static '4.png' %}"
            },
        ]
    }
    return render(request, "orders_app/mainpage.html", data)
