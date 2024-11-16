
class Cart(object):
    def __init__(self, request):
        self.session = request.session

        # Get the session key if it exists
        cart = self.session.get('session_key')

        #if use new create sess_key
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

#       cart is avail in every page
        self.cart = cart
