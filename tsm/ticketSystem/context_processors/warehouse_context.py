from ticketSystem.models import Warehouse

def warehouse_accounting(request):
    equpiment = Warehouse.objects.get(owner=request.user)
    context = {'equpiment':equpiment}
    return context