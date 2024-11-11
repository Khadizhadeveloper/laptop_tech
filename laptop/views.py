from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework import generics

from .models import Laptop
from .serializers import LaptopSerializer
from .permissions import IsAdminUser


class LaptopList(generics.ListAPIView):
    queryset = Laptop.objects.all()
    serializer_class = LaptopSerializer

class LaptopDetail(generics.RetrieveAPIView):
    queryset = Laptop.objects.all()
    serializer_class = LaptopSerializer

class LaptopDelete(generics.DestroyAPIView):
    queryset = Laptop.objects.all()
    serializer_class = LaptopSerializer
    permission_classes = [IsAdminUser]

class LaptopUpdate(generics.UpdateAPIView):
    queryset = Laptop.objects.all()
    serializer_class = LaptopSerializer
    permission_classes = [IsAdminUser]





def rate_laptop(request, product_id):
    laptop = get_object_or_404(Laptop, id=product_id)
    rating = int(request.POST.get('rating'))

    # Проверка на диапазон рейтинга
    if rating < 1 or rating > 5:
        return JsonResponse({'error': 'Invalid rating'}, status=400)

    # Проверка, голосовал ли пользователь (например, по cookie)
    if request.COOKIES.get(f'rated_{product_id}'):
        return JsonResponse({'error': 'You have already rated this product'}, status=400)

    # Обновление рейтинга
    Laptop.total_rating += rating
    Laptop.rating_count += 1
    Laptop.save()

    response = JsonResponse({'average_rating': Laptop.average_rating})
    response.set_cookie(f'rated_{product_id}', 'true', max_age=60*60*24*365)  # Устанавливаем cookie на 1 год
    return response





