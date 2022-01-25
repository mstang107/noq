from django.shortcuts import render
from django.http import *
from django.template import Template, RequestContext, Context
from django.urls import include, path
from django.contrib import admin
import traceback
import json
from static import utils
from static.utils import *
from static.all_pages import * # this is where PAGES comes from

context = {'pages': PAGES}

urlpatterns = []
for page in filter(lambda p: p['app'] == 'noq', PAGES):
    # define view function
    this_context = add_dicts(context, {'this_page_name' : page['name']})
    exec(f'''def {page["name"].replace(" ", "_")}(request):
    return render(request, '{page["template_path"]}', {this_context})''')

    urlpatterns.append(
        path(
            page["address"],
            eval(page["name"].replace(" ", "_")), # the view function defined above
            name=page["name"]
        )
    )

# internal/custom views

from solvers import *
from solvers.claspy import *

def solver(request):
    try:
        reset()
        module = globals()[request.GET['puzzle_type']]
        puzzle_encoding = module.encode(request.GET['puzzle'])
        solutions_encoded = module.solve(puzzle_encoding)
        solutions_decoded = module.decode(solutions_encoded)
        return HttpResponse(solutions_decoded)
    # show error messages
    except ValueError as err:
        print(traceback.print_exc(),flush=True)
        return HttpResponseBadRequest(json.dumps({
            'message': str(err)
        }))
    except Exception as exc:
        print(traceback.print_exc(),flush=True)
        return HttpResponseServerError(json.dumps({
            'message': str(exc)
        }))

# append internal urlpatterns
urlpatterns += [
    path('admin/', admin.site.urls),
    path('solver', solver, name='solver'),
]