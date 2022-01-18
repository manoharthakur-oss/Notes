# Django


## Basic

step 1
django-admin app <app name>

step 2
cd <app name>

step 3
python manage.py runserver

note1 - when we make project using step 1 django creates a project and a app in it with same name.
let us say this app the default app




## EDITING URLS.PY

- make a file views.py in default app.
- write `from django.http import HttpResponse`
- make views in views.py 
- Example:
  ```
  def index (request):
      return HttpResponse("hello")
  ```

- First of all we have to edit urls.py of default app. Add following statement in urls.py file 
`from . import views`
- Now add paths to `urlpatterns` list.
- path(arg1, arg2, arg3)
  - arg1: part of url
  - arg2: function from views
  - arg3: `name ="<custom name>"`


- s
- 

## LAYING THE PIPELINE
- in urls.py we can add custom urls  that leads to custom functions.A different function leads to a different webpage.
- tu add   pipeline first add `url path` and then `view`

## 8. Templates

- go-to settings.py add `"templates"` in `DIRS:[]`
- in views.py import `render` from `djanjo.shortcuts`.
- create a `templates` folder in folder where manage.py is present.
- NOW edit your view (function) as following
  ```
  def index (index):
      return render (request,"<name of template>")
  ```
### HOW TO SEND VARIABLES TO TEMPLATES
1.  `render(arg1, arg2, arg3)`

    - arg1: request
    - arg2: template file
    - arg3: dictionary of variables you wanna send to templates.

2. __code in template will be:__
    `{{<key of the dictionary>}}`
    
__Note:__ key, value of arg3 must be strings


## Access form data in python code.
1. create a form tag
2. write `action="<name of view>"` in form tag
3. add a `textinput` tag in `form` tag.
4. Give a name to `textarea` tag.
5. Now `request.GET.get()` will return the values entered in form.

**note:** You can use __request.GET.get()__ method in the view You are calling in action attribute of the form.
