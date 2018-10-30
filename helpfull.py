#delete Methode

"""
1- define get_object


"""


def get_object(self, id=None):
    try:
        obj = Choice.objects.get(id=id)
    except Choice.DoesNotExist:
        obj = None
    return obj