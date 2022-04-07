from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class SearchByGenreMixin:
    def search_by_genre(self, request, pk):
        instance = self.queryset.filter(genres__in={pk})

        serialized_movies = self.get_serializer(instance, many=True)

        return Response(serialized_movies.data, status=200)


class CreateReviewMixin:
    def create_review(self, request, *args, **kwargs):
        cinema = self.get_object()
        instance_data = {
            'text': request.data['text'],
            'movie': cinema.id,
            'author': request.user.id
        }

        serializer = self.get_serializer(data=instance_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=200)


class ReadAllReviewsMixin:
    def get_all_reviews(self, request):
        cinema = self.get_object()
        reviews = cinema.reviews.all().select_related('author').order_by('date_of_creation')

        serializer = self.get_serializer(reviews, many=True)

        return Response(serializer.data)


class UpdateReviewMixin:
    def update_review(self, request, id):
        review = get_object_or_404(self.queryset, id=id, author=request.user)

        review.text = request.data.get('text')
        review.save(update_fields=['text'])

        return Response(status=200)


class DeleteReviewMixin:
    def delete_review(self, request, id):
        review = get_object_or_404(self.queryset, id=id, author=request.user)
        review.delete()

        return Response(status=200)


class CinemaMixin(SearchByGenreMixin, CreateReviewMixin,
                ReadAllReviewsMixin, UpdateReviewMixin, DeleteReviewMixin):
    '''Класс, который просто объединяет все примеси'''
    pass