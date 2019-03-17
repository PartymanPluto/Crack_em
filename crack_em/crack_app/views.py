from django.shortcuts import render
from django.http import HttpResponse
from crack_app.models import Egg, Recipe

#Basic pages
def home(request):
    #To add: cookies
    recipe_list = Recipe.objects.order_by('views')[:5]
    cd = {'recipes':recipe_list}
    
    response = render(request, 'crack_em/home.html', cd)
    return response

def about(request):
    return render(request, 'crack_em/about.html', {})

def contact(request):
    return render(request, 'crack_em/contact.html', {})
    
def FAQ(request):
    return render(request, 'crack_em/FAQ.html', {})



#Views for eggs and recipes
def eggs(request):
    #To add: cookies
    egg_list = Egg.objects.order_by('views')
    cd = {'eggs'}
    
    response = render(request, 'crack_em/egg_types.html', cd)
    return response

def show_eggs(request, egg_name_slug):
    cd = {}
    
    try:
        egg_type = Egg.objects.get(slug = egg_name_slug)
        recipes = Recipe.objects.filter(egg_type = egg_type)
        
        cd['egg'] = egg_type
        cd['recipes'] = recipes
        
    except Egg.DoesNotExist:
        cd['egg'] = None
        cd['recipes'] = None
        
    return render(request, 'crack_em/egg.html', cd)
        
def show_recipe(request, recipe_name_slug):
    try:
        recipe = Recipe.objects.get(slug = recipe_name_slug)
        cd = {'recipe': recipe}
    except Recipe.DoesNotExist:
        cd = {'recipe': None}
    
    return render(request, 'crack_em/recipe.html', cd)

def add_recipe(request, egg_name_slug):
    try:
        egg_type = Category.objects.get(slug=egg_name_slug)
    except egg_type.DoesNotExist:
        egg_type = 'other'
    
    form = RecipeForm()
    if request.method == "POST":
        form = RecipeForm(request.POST)
        
        if form.is_valid():
            recipe = form.save(commit =False)
            recipe.egg_type = egg_type
            recipe.views = 0
            recipe.average_rating = 0
            recipe.ratings = []
            return show_eggs(request, egg_name_slug)
        else:
            print(form.errors)

    cd = {'form':form, 'egg':egg_type}
    return render(request, 'crack_em/add_recipe.html', cd)
#User authentication
def register(request):

def username_present(username):
    if User.objects.filter(username=username).exists:
        return True
    return False

def user_login(request):
    
@login_required
def user_account(request):
    
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
    

#Cookie handling 
def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val

def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request, 'visits', '1'))
    last_visit_cookie = get_server_side_cookie(request,
                                               'last_visit', 
                                               str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7],
                                        '%Y-%m-%d %H:%M:%S')
    
    if(datetime.now() - last_visit_time).days > 0:
        visits += 1
        request.session['last_visit'] =  str(datetime.now())
    else:
        request.session['last_visit'] = last_visit_cookie 
        
    request.session['visits'] = visits
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    