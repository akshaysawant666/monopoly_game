from django.contrib import admin

# Register your models here.
from blockchain.models import *

# Register your models here.
admin.site.register(Block)
admin.site.register(Chain)
admin.site.register(Peer)
admin.site.register(Transactions)