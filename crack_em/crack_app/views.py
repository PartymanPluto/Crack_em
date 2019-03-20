from django.shortcuts import render
from django.http import HttpResponse
from crack_app.models import Egg, Recipe, Comment, UserProfile
from crack_app.forms import RecipeForm, CommentForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from registration.backends.simple.views import RegistrationView

#Basic pages
def home(request):
    recipe_list = Recipe.objects.order_by('views')[:5]
    cd = {'recipes':recipe_list}
    
    #visitor_cookie_handler(request)
    #cd['visit'] = request.session['visits']
    
    response = render(request, 'crack_app/home.html', cd)
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
    egg_list = Egg.objects.order_by(len('recipes'))
    cd = {'eggs': egg_list}
    
    response = render(request, 'crack_em/egg_types.html', cd)
    return response

def show_eggs(request, egg_slug):
    cd = {}
    
    try:
        egg_type = Egg.objects.get(slug = egg_slug)
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
        comments = Comment.objects.filter(recipe = recipe)
        cd = {'recipe': recipe, 'comments':comments}
    except Recipe.DoesNotExist:
        cd = {'recipe': None, 'comments':None}
    if recipe:
        formC = CommentForm()
        #formR = RatingForm()
        if request.method == "POST":
            data = request.POST
            if 'submit_comment' in data:
                formC = CommentForm(data)
                if formC.is_valid():
                    comment = formC.save(commit = False)
                    recipe.comments.append(comment)
                    return show_recipe(request, recipe_name_slug)
                else:
                    print(formC.errors)
            '''elif 'submit_rating' in data:
                formR = RatingForm(data)
                if formC.is_valid():
                    comment = formC.save(commit = False)
                    recipe.comments.append(comment)
                    return show_recipe(request, recipe_name_slug)
                else:
                    print(form.errors)'''
    return render(request, 'crack_em/recipe.html', cd)

def add_recipe(request):
    form = RecipeForm()
    if request.method == "POST":
        form = RecipeForm(request.POST)
        
        if form.is_valid():
            recipe = form.save(commit =False)
            recipe.views = 0
            recipe.average_rating = 0
            recipe.ratings = []
            return show_recipe(request, recipe.slug)
        else:
            print(form.errors)

    cd = {'form':form}
    return render(request, 'crack_em/add_recipe.html', cd)



#View for showing a user's account page    
@login_required
def user_account_page(request, account_name_slug):
    cd = {}
    
    try:
        user = User.objects.get(username=account_name_slug)
        if request.user == user or request.user.is_authenticated():
            profile = UserProfile.objects.filter(user=account_name_slug)
        
            cd['User'] = user
            cd['Profile'] = profile
        else:
            return render(request, 'crack_em/not_authenticated.html', cd)
            
    except User.DoesNotExist:
        cd['User'] = None
        cd['Profile'] = None
    
    return render(request, 'crack_em/account_page.html', cd)

#Class for handling user authentication
class MyRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return '/crack_em/'

#Views for liking and commenting
@login_required
def like_recipe(request):
    rec_id = None
    if request.method == 'GET':
        rec_id = request.GET['recipe_id']
    likes = 0
    if rec_id:
        rec = Recipe.objects.get(id=int(rec_id))
        if rec:
            likes = rec.likes + 1
            rec.save()
    return HttpResponse(likes)

@login_required
def rate_recipe(request):
    rec_id = None
    if request.method == 'POST':
        rec_id = request.POST['recipe_id']
    ratings = []
    average_rating = 0
    if rec_id:
        rec = Recipe.objects.get(id=int(rec_id))
        if rec:
            rec.ratings.append(request.POST)

#!-----WIP functions------!
'''@login_required
def add_comment(request):
    rec_id = None
    if request.method == 'GET':
        rec_id = request.GET['recipe_id']
    comments = []
    if rec_id:
        rec = Recipe.objects.get(id=int(rec_id))
        if rec:
            comments = rec.comments + '''
            
#!-----------------!

#Cookie handling 
"""def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val"""

"""def visitor_cookie_handler(request):
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
        
    request.session['visits'] = visits"""
    
    
    
    
#!!!----OLD USER AUTHENTICATION CODE----!!!
"""def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("Your account has been disabled.")
    
        else:
            if username_present(username) == True:
                print("Invalid login details: {0}, {1}".format(username, password))
                return HttpResponse("You have entered an invalid username/password combination.")
            else:
                print("Invalid login details: {0}, {1}".format(username, password))
                return HttpResponse("No such user exists with that username.")  
    else:
           return render(request, 'crack_em/login.html', {})"""
           
"""def register(request):
    r = False
    
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.date_joined = str(now.strftime("%Y-%m-%d")
            
            if'picture' in request.FILES:
                profile.picture = request.FILES['picture']
                
            profile.save()
            r = True
            
        else:
            print(user_form.errors, profile_form.errors)
        
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
        
    return render(request, 'crack_em.register.html', 
                  {'user_form':user_form,
                   'profile_form':profile_form,
                   'registered':r})"""
    
"""@login_required
    def user_logout(request):
        logout(request)
        return HttpResponseRedirect(reverse('home'))"""
        
"""def username_present(username):
    if User.objects.filter(username=username).exists:
        return True
    return False  """
    

 
    