from django.shortcuts import render_to_response
from django.template import RequestContext

def thankyou( request ):
   return render_to_response( 'thankyou.html', { }, context_instance=RequestContext( request ) )
