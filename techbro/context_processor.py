from cart.models import Shopcart
from techbro.models import Category, Dish




def cartcount(request):
    count = Shopcart.objects.filter(user__username = request.user.username, paid=False)

    itemcount = 0

    for item in count:
        itemcount += int(item.user.id)
    
    context = {
        'itemcount' : itemcount
    }
    return context

