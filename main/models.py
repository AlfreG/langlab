from django.db import models


class Locations(models.Model):

    '''
    Index page contents locations
    '''
    location = models.CharField(max_length=15, primary_key=True)

    def __str__(self):
        return self.location


class Languages(models.Model):
    '''
    '''
    language = models.CharField(max_length=2, primary_key=True)

    def __str__(self):
        return self.language


class Menus(models.Model):
    '''
    Menu: label
    path: url
    '''
    menu = models.CharField(max_length=15)
    urlpath = models.CharField(max_length=15)
    # field order should respect the sequentiality given in Languages
    # en = models.CharField(max_length=15)
    # it = models.CharField(max_length=15)
    # es = models.CharField(max_length=15)
    # fr = models.CharField(max_length=15)
    # It’s suggested, but not required, that the name of a ForeignKey field
    # be the name of the model, lowercase
    location = models.ForeignKey(Locations, on_delete=models.CASCADE)
    language = models.ForeignKey(Languages, on_delete=models.CASCADE)

    def __str__(self):
        return self.menu


class Disclaimers(models.Model):
    '''
    '''
    disclaimer = models.CharField(max_length=50, primary_key=True)
    # en = models.CharField(max_length=50)
    # it = models.CharField(max_length=50)
    # es = models.CharField(max_length=50)
    # fr = models.CharField(max_length=50)
    # It’s suggested, but not required, that the name of a ForeignKey field
    # be the name of the model, lowercase
    location = models.ForeignKey(Locations, on_delete=models.CASCADE)
    language = models.ForeignKey(Languages, on_delete=models.CASCADE)

    def __str__(self):
        return self.disclaimer
