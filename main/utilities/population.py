"""
SCRIPT: populate db
CONSOLE: exec(open("main/utilities/population.py").read())

alfre.guarnieri@gmail.com
"""

from main.models import Languages, Locations, Menus


Languages.objects.filter().delete()
Locations.objects.filter().delete()
Menus.objects.filter().delete()


en = Languages.objects.create(language="en")
it = Languages.objects.create(language="it")
es = Languages.objects.create(language="es")
fr = Languages.objects.create(language="fr")

navbar= Locations.objects.create(location="navbar")
lsb = Locations.objects.create(location="left-sidebar")
rsb = Locations.objects.create(location="right-sidebar")
body = Locations.objects.create(location="body")
title = Locations.objects.create(location="title")
footer = Locations.objects.create(location="footer")

#TBD home this menu shouldn't change
Menus.objects.create(menu="home",urlpath="home",language=en,location=navbar)
Menus.objects.create(menu="home",urlpath="home",language=it,location=navbar)
Menus.objects.create(menu="home",urlpath="home",language=es,location=navbar)
Menus.objects.create(menu="home",urlpath="home",language=fr,location=navbar)
#
Menus.objects.create(menu="services",urlpath="services",language=en,location=navbar)
Menus.objects.create(menu="servizi",urlpath="services",language=it,location=navbar)
Menus.objects.create(menu="servicios",urlpath="services",language=es,location=navbar)
Menus.objects.create(menu="services",urlpath="services",language=fr,location=navbar)
#
Menus.objects.create(menu="contacts us",urlpath="contactus",language=en,location=navbar)
Menus.objects.create(menu="contattaci",urlpath="contactus",language=it,location=navbar)
Menus.objects.create(menu="contactanos",urlpath="contactus",language=es,location=navbar)
Menus.objects.create(menu="contactez nous",urlpath="contactus",language=fr,location=navbar)
#
Menus.objects.create(menu="about us",urlpath="aboutus",language=en,location=navbar)
Menus.objects.create(menu="su di noi",urlpath="aboutus",language=it,location=navbar)
Menus.objects.create(menu="de nosotros",urlpath="aboutus",language=es,location=navbar)
Menus.objects.create(menu="sur nous",urlpath="aboutus",language=es,location=navbar)

# Query example
Menus.objects.filter(location__exact='navbar')

'''
<ul>
    {% for langvar in lang_list %}
    <li><a href="{% url 'main:index' langvar section %}">{{ langvar }}</a></li>
    {% endfor %}
</ul>

<ul>
    {% for menuvar in navbar_list %}
    <li><a href="{% url 'main:index' lang menunvar %}">{{ menuvar.menu }}</a></li>
    {% endfor %}
</ul>

 <div class="col">

    </div>
    
'''
