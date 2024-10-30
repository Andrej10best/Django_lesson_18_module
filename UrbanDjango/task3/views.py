from django.shortcuts import render

# Create your views here.
def platform(request):
    return render(request, 'third_task\\platform.html')

def games(request):
    game_1 = 'Atomic Heart'
    game_2 = 'Cyberpunk 2077'
    game_3 = 'PayDay 2'
    context = {
        'game_1': game_1,
        'game_2': game_2,
        'game_3': game_3
    }
    return render(request, 'third_task\\games.html', context)

def cart(request):
    return render(request, 'third_task\\cart.html')
