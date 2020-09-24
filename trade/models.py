from django.db import models

from django.conf import settings


OPEN = '0'
CLOSED = '1'
DECLINED = '2'
ACCEPTED = '3'

STATUS_TYPE = (
    (OPEN, 'Open'),
    (CLOSED, 'Closed'),
)

REQUEST_TYPE  = (
    (OPEN, 'Open'),
    (CLOSED, 'Closed'),
    (DECLINED, 'Declined'),
    (ACCEPTED, 'Accepted'),
)

class Trade(models.Model):
    """ Trade model
    """ 
    name = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    photos = models.ManyToManyField('Photos')
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_TYPE, default=OPEN)

    def __str__(self):
        return f'{self.name}'

def upload_to(self):
    return 
class Photos(models.Model):
    """ Trade item images
    """

    image = models.ImageField(upload_to='images/')
    timestamp = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = 'Photos'


class RequestTrade(models.Model):
    """ Trade Request model
    """ 
    trade = models.ForeignKey(Trade, on_delete=models.CASCADE, related_name='requests')
    item_name = models.CharField(max_length=256)
    message = models.TextField()
    status = models.CharField(max_length=1, choices=REQUEST_TYPE, default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.trade.name}' 


class RequestImage(models.Model):
    """ Trade Request Images
    """
    trade = models.ForeignKey(RequestTrade, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='requests_images/')
    timestamp = models.DateTimeField(auto_now_add=True)
