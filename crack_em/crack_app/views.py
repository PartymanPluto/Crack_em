from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from crack_app.models import Egg, Recipe, Comment, UserProfile, Rating
from crack_app.forms import RecipeForm, CommentForm, UserProfileForm, RatingForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from registration.backends.simple.views import RegistrationView
from datetime import datetime

#Basic pages
def home(request):
    omlettes = Recipe.objects.filter(egg_type=Egg.objects.get(title='Omlette')).order_by('views')[:2]
    fried = Recipe.objects.filter(egg_type=Egg.objects.get(title='Fried')).order_by('views')[:1]
    scrambled = Recipe.objects.filter(egg_type=Egg.objects.get(title='Scrambled')).order_by('views')[:1]
    poached = Recipe.objects.filter(egg_type=Egg.objects.get(title='Poached')).order_by('views')[:1]
    sf = Recipe.objects.filter(egg_type=Egg.objects.get(title='Sauces/Fillings')).order_by('views')[:1]
    other = Recipe.objects.filter(egg_type=Egg.objects.get(title='Other')).order_by('views')[:1]
    recipes = {'Omlettes': omlettes, 'Fried': fried, 'Scrambled': scrambled, 'Poached': poached, 'Sauces & Fillings': sf, 'other': other}
    cd = {'recipes': recipes }
    
    response = render(request, 'crack_app/home.html', cd)
    return response

def about(request):
    return render(request, 'crack_app/about.html', {})

def contact(request):
    return render(request, 'crack_app/contact.html', {})
    
def FAQ(request):
    return render(request, 'crack_app/FAQ.html', {})



#Views for eggs and recipes
def eggs(request):
    #To add: cookies
    egg_list = Egg.objects.order_by('title')
    cd = {'eggs': egg_list}
    
    response = render(request, 'crack_app/egg_types.html', cd)
    return response

def show_egg(request, egg_slug):
    cd = {}
    
    try:
        egg_type = Egg.objects.get(slug = egg_slug)
        recipes = Recipe.objects.filter(egg_type = egg_type)
        
        cd['egg'] = egg_type
        cd['recipes'] = recipes
        
    except Egg.DoesNotExist:
        cd['egg'] = None
        cd['recipes'] = None
        
    return render(request, 'crack_app/egg.html', cd)
        
def show_recipe(request, recipe_slug):
    try:
        recipe = Recipe.objects.get(slug = recipe_slug)
        comments = Comment.objects.filter(recipe = recipe)
        ing = recipe.ingrediants.split(',')
        inst = recipe.instructions.split(';')
        inst_dict = {}
        j = 1
        for i in inst:
            print(i)
            inst_dict[str(j)] = i
            j += 1
        print(inst_dict)
        cd = {'recipe': recipe, 'ingrediants':ing, 'instructions':inst_dict, 'comments':comments}
        request.session.set_test_cookie()
        visitor_cookie_handler(request)
        recipe.views += request.session['visits']
        recipe.average_ratings = ratings_sum(recipe)
        try:
            user_profile = UserProfile.objects.get(user = request.user)
        except UserProfile.DoesNotExist:
            user_profile = None
        formR = RatingForm()
        formC = CommentForm()
        if request.method == "POST":
            if request.user.is_authenticated():
                data = request.POST
                if 'submit_comment' in data:
                    formC = CommentForm(data)
                    if formC.is_valid():
                        formC.save(commit = True)
                        return redirect('recipe', recipe_slug)
                    else:
                        print(formC.errors)
                elif 'submit_rating' in data:
                    if recipe.user_profile_set.filter(pk=user_profile.pk).exists():
                        rating = Rating.object.filter(user=request.user, recipe=recipe)
                        formR = RatingForm(data, instance = rating)
                        if formR.is_valid():
                            formR.save(commit=True)
                            return redirect('recipe', recipe_slug)
                        else:
                            print(formR.errors)
                    else:
                        formR = RatingForm(data)
                        if formR.is_valid():
                            formR.save(commit=False)
                            formR.user = request.user
                            formR.recipe = recipe
                            UserProfile.add(formR)
                            return redirect('recipe', recipe_slug)
                        else:
                            print(formR.errors)
            else:
                return redirect('login')
        cd['formC'] = formC
        cd['formR'] = formR
    except Recipe.DoesNotExist:
        cd = {'recipe': None,'ingrediants': None, 'instructions': None, 'comments':None, 'formC': None, 'formR': None}
    return render(request, 'crack_app/recipe.html', cd)

def add_recipe(request):
    form = RecipeForm()
    if request.method == "POST":
        form = RecipeForm(request.POST)
        
        if form.is_valid():
            recipe = form.save(commit =False)
            recipe.author = request.user
            recipe.views = 0
            recipe.average_rating = 0
            return show_recipe(request, recipe.slug)
        else:
            print(form.errors)

    cd = {'form':form}
    return render(request, 'crack_app/add_recipe.html', cd)

#def add_comment(request):

def ratings_sum(recipe):
    ratings = Rating.objects.filter(recipe=recipe)
    if len(ratings) < 5:
        return 0
    else:
        sum = 0
        for r in ratings:
            sum+= r
        return sum/len(ratings)

#View for showing a user's account page    
@login_required
def user_account_page(request, username):
    cd = {}
    
    try:
        user = User.objects.get(username=username)
        if request.user == user:
            profile = UserProfile.objects.filter(user=User.objects.get(username=username))[0]
            form = UserProfileForm(
                    {'picture': profile.picture})
            if request.method == "POST":
                form = UserProfileForm(
                        request.FILES, instance=profile)
                if form.is_valid():
                    form.save(commit=True)
                    return redirect('profile', user.username)
                else:
                    print(form.errors)
            cd['selected_user'] = user
            cd['selected_profile'] = profile
            cd['form'] = form
        else:
            return redirect('login')
            
    except User.DoesNotExist:
        cd['selected_user'] = None
        cd['selected_profile'] = None
        cd['form'] = None
    
    return render(request, 'crack_app/profile.html', cd)

#User authentication
class MyRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return reverse('register_profile')

def register_profile(request):
    form = UserProfileForm
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            return redirect('home')
        else:
            print(form.errors)
        
    cd = {'form':form}
    return render(request, 'crack_app/profile_registration.html', cd)

#Views for liking and commenting
@login_required
def like_user(request):
    profile_id = None
    if request.method == 'GET':
        profile_id  =request.GET['selected_profile_id']
        likes = 0
    if profile_id:
        profile = UserProfile.objects.get(id=profile_id)
        if profile:
            likes = profile.likes +1
            profile.likes = likes
            profile.save()
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

def like_user(request):
    profile_id = None
    if request.method == 'GET':
        profile_id  =request.GET['selected_profile_id']
        likes = 0
    if profile_id:
        profile = UserProfile.objects.get(id=profile_id)
        if profile:
            likes = profile.likes +1
            profile.likes = likes
            profile.save()
    return HttpResponse(likes)
    
    
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
    

 
    