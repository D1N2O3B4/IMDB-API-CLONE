# from django.shortcuts import render
# from .models import Movie
# from django.http import JsonResponse
# from django.shortcuts import get_object_or_404

# # Create your views here.
# def movie_list(request):
#     movies = Movie.objects.all()
#     data = {
#         'movies': list(movies.values())
#     }

#     return JsonResponse(data)

# def movie_details(request, pk):
#     movie = get_object_or_404(Movie, pk=pk)
#     data = {
#         "title": movie.title,
#         "description": movie.description,
#         "active": movie.active
#     }

#     return JsonResponse(data)
    