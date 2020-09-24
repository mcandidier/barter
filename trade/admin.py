from django.contrib import admin

# Register your models here.
from .models import Trade, Photos, RequestImage, RequestTrade

class TradeAdmin(admin.ModelAdmin):
    model = Trade
    list_display = ('name', 'owner', 'requests', 'status',)

    def requests(self, obj):
        return obj.requests.all().count()

admin.site.register(Trade, TradeAdmin)
admin.site.register(Photos)
admin.site.register(RequestTrade)
admin.site.register(RequestImage)