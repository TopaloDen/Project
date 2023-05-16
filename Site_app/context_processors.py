def custom_user(request):
    if request.user.is_anonymous:
        return {'User ': 'Користувач анонімний'}
    else:
        return {'User ': request.user}
