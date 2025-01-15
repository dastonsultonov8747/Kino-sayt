import random
from django.shortcuts import render
from .models import Serial, Kinolar, Serial_item, Multfilm, Anime_item, Anime
from .serializers import SerialSerializer, KinolarSerializer, SerialItemSerializer, MultfilmSerializer, AnimeSerializer, \
    AnimeItemSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# bu yerda qiziqarli bolishi uchun random orqali kinolarni chaqiramiz
ratings = [1, 2, 3, 4, 5]


def Index(reuqest):
    kinolars = Kinolar.objects.all()
    serials = Serial.objects.all()
    animes = Anime.objects.all()
    multfilms = Multfilm.objects.all()
    random_kinolars = kinolars.order_by('?'[:2])
    random_serials = serials.order_by('?'[:1])
    random_multfilms = multfilms.order_by('?'[:1])
    random_animes = animes.order_by('?'[:1])
    random_select = random.choice([random_kinolars, random_serials, random_multfilms, random_animes])
    select_movies = random.choice(random_kinolars)

    return render(reuqest, 'index.html',
                  {'ratings': ratings, 'kinolars': kinolars, 'serials': serials,
                   'select_movies': select_movies,
                   'multfilms': multfilms})


def Kinolar_views(request):
    # top_10_cartoon = [
    #     {
    #         "name": "Spider-Man: Into the Spider-Verse",
    #         "img": "D:/Kino_sayt_media/rasm/spider-man.jpg",
    #         "video_fayl": "D:/Kino_sayt_media/kinolar/spider-man.mp4",
    #         "sight_age": 7,
    #         "reyting": 5,
    #         "genre": "Superhero, Adventure",
    #         "description": "Bir nechta Spider-Man versiyalarini birlashtirgan animatsion film. Qahramonlar kimligini va do‘stlikni kashf etadilar."
    #     },
    #     {
    #         "name": "Toy Story 4",
    #         "img": "D:/Kino_sayt_media/rasm/toy-story-4.jpg",
    #         "video_fayl": "D:/Kino_sayt_media/kinolar/toy-story-4.mp4",
    #         "sight_age": 5,
    #         "reyting": 4,
    #         "genre": "Comedy, Adventure",
    #         "description": "Woody, Buzz va boshqa o‘yinchilar Forky ismli yangi do‘stlari bilan sarguzashtga chiqishadi."
    #     },
    #     {
    #         "name": "Frozen II",
    #         "img": "D:/Kino_sayt_media/rasm/frozen-ii.jpg",
    #         "video_fayl": "D:/Kino_sayt_media/kinolar/frozen-ii.mp4",
    #         "sight_age": 6,
    #         "reyting": 4,
    #         "genre": "Fantasy, Musical",
    #         "description": "Elsa, Anna va ular bilan birga Krismof va Olaf yangi sarguzashtlarga chiqib, o‘z kuchlarini kashf etadilar."
    #     },
    #     {
    #         "name": "Zootopia",
    #         "img": "D:/Kino_sayt_media/rasm/zootopia.jpg",
    #         "video_fayl": "D:/Kino_sayt_media/kinolar/zootopia.mp4",
    #         "sight_age": 6,
    #         "reyting": 5,
    #         "genre": "Comedy, Mystery",
    #         "description": "Zootopiya shahridagi hayvonlar o‘rtasida adolatsizlikka qarshi kurash olib boruvchi jinni bir do‘stlik haqidagi hikoya."
    #     },
    #     {
    #         "name": "Coco",
    #         "img": "D:/Kino_sayt_media/rasm/coco.jpg",
    #         "video_fayl": "D:/Kino_sayt_media/kinolar/coco.mp4",
    #         "sight_age": 7,
    #         "reyting": 5,
    #         "genre": "Family, Adventure",
    #         "description": "Migel ismli bola, o‘z oilasining musiqaga nisbatan cheklovlarini kashf qilib, O‘liklar Yeriga sayohat qiladi."
    #     },
    #     {
    #         "name": "The Lion King (2019)",
    #         "img": "D:/Kino_sayt_media/rasm/lion-king-2019.jpg",
    #         "video_fayl": "D:/Kino_sayt_media/kinolar/lion-king-2019.mp4",
    #         "sight_age": 6,
    #         "reyting": 4,
    #         "genre": "Drama, Adventure",
    #         "description": "Simba ismli kichkina sherning o‘zining podsholigini qaytarish uchun kurashishidagi sarguzasht."
    #     },
    #     {
    #         "name": "How to Train Your Dragon: The Hidden World",
    #         "img": "D:/Kino_sayt_media/rasm/how-to-train-your-dragon.jpg",
    #         "video_fayl": "D:/Kino_sayt_media/kinolar/how-to-train-your-dragon.mp4",
    #         "sight_age": 7,
    #         "reyting": 5,
    #         "genre": "Fantasy, Action",
    #         "description": "Hiccup va Toothless yangi dargonlar dunyosini kashf etib, ularni saqlash uchun yomon odamga qarshi kurashishadi."
    #     },
    #     {
    #         "name": "Shrek 2",
    #         "img": "D:/Kino_sayt_media/rasm/shrek-2.jpg",
    #         "video_fayl": "D:/Kino_sayt_media/kinolar/shrek-2.mp4",
    #         "sight_age": 6,
    #         "reyting": 4,
    #         "genre": "Comedy, Fantasy",
    #         "description": "Shrek va Fiona uning ota-onasi bilan uchrashishga borishadi, Shrek esa yangi oilasiga moslashishga harakat qiladi."
    #     },
    #     {
    #         "name": "The Incredibles 2",
    #         "img": "D:/Kino_sayt_media/rasm/incredibles-2.jpg",
    #         "video_fayl": "D:/Kino_sayt_media/kinolar/incredibles-2.mp4",
    #         "sight_age": 6,
    #         "reyting": 5,
    #         "genre": "Superhero, Action",
    #         "description": "Elastigirl jinoyatchilarni ushlashda davom etadi, Mr. Incredibles esa uyda farzandlari bilan vaqt o‘tkazadi."
    #     },
    #     {
    #         "name": "Minions: The Rise of Gru",
    #         "img": "D:/Kino_sayt_media/rasm/minions-rise-of-gru.jpg",
    #         "video_fayl": "D:/Kino_sayt_media/kinolar/minions-rise-of-gru.mp4",
    #         "sight_age": 5,
    #         "reyting": 4,
    #         "genre": "Comedy, Adventure",
    #         "description": "Gru o‘zining super yovuzlikni amalga oshirish orzusini ro‘yobga chiqarishga intiladi, Minionlar esa unga yordam beradi."
    #     }
    # ]

    # top_4_serial = [
    #     {
    #         "name": "Stranger Things",
    #         "img": "D:/Kino_sayt_media/rasm/stranger-things.jpg",
    #         "video_fayl": "D:/Kino_sayt_media/kinolar/stranger-things.mp4",
    #         "sight_age": 16,
    #         "genre": "Sci-Fi, Drama, Horror",
    #         "reyting": 5,
    #         "description": "Hawkins shahrida sirli voqealar sodir bo‘ladi, do‘stlar guruhi g‘ayritabiiy kuchlarga qarshi kurashadi."
    #     },
    #     {
    #         "name": "Game of Thrones",
    #         "img": "D:/Kino_sayt_media/rasm/game-of-thrones.jpg",
    #         "video_fayl": "D:/Kino_sayt_media/kinolar/game-of-thrones.mp4",
    #         "sight_age": 18,
    #         "genre": "Fantasy, Drama, Action",
    #         "reyting": 5,
    #         "description": "Taxt uchun kurashayotgan oila va qirolliklarning epik hikoyasi."
    #     },
    #     {
    #         "name": "The Witcher",
    #         "img": "D:/Kino_sayt_media/rasm/the-witcher.jpg",
    #         "video_fayl": "D:/Kino_sayt_media/kinolar/the-witcher.mp4",
    #         "sight_age": 18,
    #         "genre": "Fantasy, Action, Adventure",
    #         "reyting": 4,
    #         "description": "Geralt ismli yovuzlikni yo‘q qiluvchi Witcherning sarguzashtlari haqida hikoya."
    #     },
    #     {
    #         "name": "Breaking Bad",
    #         "img": "D:/Kino_sayt_media/rasm/breaking-bad.jpg",
    #         "video_fayl": "D:/Kino_sayt_media/kinolar/breaking-bad.mp4",
    #         "sight_age": 18,
    #         "genre": "Crime, Drama, Thriller",
    #         "reyting": 5,
    #         "description": "Kimyo o‘qituvchisi Walter White o‘zining hayoti uchun xavfli jinoyat yo‘liga kiradi."
    #     }
    # ]

    # serial_items = [
    #     {
    #         "serial_name": "Stranger Things",  # 1-serial nomi
    #         "name": "Stranger Things: Qism 1",
    #         "part": 1,
    #         "img": "D:/Kino_sayt_media/rasm/stranger-things-qism1.jpg",
    #         "video_fayl": "D:/Kino_sayt_media/kinolar/stranger-things-qism1.mp4",
    #         "description": "Stranger Things 1-qismi: sirli yo'qolish va g‘ayritabiiy hodisalar boshlanishi."
    #     },
    #     {
    #         "serial_name": "Stranger Things",
    #         "name": "Stranger Things: Qism 2",
    #         "part": 2,
    #         "img": "D:/Kino_sayt_media/rasm/stranger-things-qism2.jpg",
    #         "video_fayl": "D:/Kino_sayt_media/kinolar/stranger-things-qism2.mp4",
    #         "description": "Stranger Things 2-qismi: do'stlar izlanishlarini davom ettirishmoqda."
    #     },
    #     {
    #         "serial_name": "Stranger Things",
    #         "name": "Stranger Things: Qism 3",
    #         "part": 3,
    #         "img": "D:/Kino_sayt_media/rasm/stranger-things-qism3.jpg",
    #         "video_fayl": "D:/Kino_sayt_media/kinolar/stranger-things-qism3.mp4",
    #         "description": "Stranger Things 3-qismi: g‘ayritabiiy kuchlarning yangi belgilari ko'rinmoqda."
    #     },
    #     {
    #         "serial_name": "Stranger Things",
    #         "name": "Stranger Things: Qism 4",
    #         "part": 4,
    #         "img": "D:/Kino_sayt_media/rasm/stranger-things-qism4.jpg",
    #         "video_fayl": "D:/Kino_sayt_media/kinolar/stranger-things-qism4.mp4",
    #         "description": "Stranger Things 4-qismi: do'stlar jamoasi kuchli qarshiliklarga duch kelishmoqda."
    #     }
    # ]
    # game_of_thrones_items = [
    #     {
    #         "serial_name": "Game of Thrones",  # Serial nomi
    #         "name": "Game of Thrones: Qism 1",
    #         "part": 1,
    #         "img": "D:/Kino_sayt_media/rasm/got-qism1.jpeg",
    #         "video_fayl": "D:/Kino_sayt_media/kinolar/got-qism1.mp4",
    #         "description": "Game of Thrones 1-qismi: Starklar oilasining hayotiga ta'sir qiluvchi sirlar ochiladi."
    #     },
    #     {
    #         "serial_name": "Game of Thrones",
    #         "name": "Game of Thrones: Qism 2",
    #         "part": 2,
    #         "img": "D:/Kino_sayt_media/rasm/got-qism2.jpg",
    #         "video_fayl": "D:/Kino_sayt_media/kinolar/got-qism2.mp4",
    #         "description": "Game of Thrones 2-qismi: Qirollik taxtini egallash uchun kurash boshlanadi."
    #     },
    #     {
    #         "serial_name": "Game of Thrones",
    #         "name": "Game of Thrones: Qism 3",
    #         "part": 3,
    #         "img": "D:/Kino_sayt_media/rasm/got-qism3.jpg",
    #         "video_fayl": "D:/Kino_sayt_media/kinolar/got-qism3.mp4",
    #         "description": "Game of Thrones 3-qismi: Daenerys o‘z kuchlarini yig‘ishni boshlaydi."
    #     }
    # ]
    # the_witcher_items = [
    #     {
    #         "serial_name": "The Witcher",  # Serial nomi
    #         "name": "The Witcher: Qism 1",
    #         "part": 1,
    #         "img": "D:/Kino_sayt_media/rasm/witcher-qism1.jpg",
    #         "video_fayl": "D:/Kino_sayt_media/kinolar/witcher-qism1.mp4",
    #         "description": "The Witcher 1-qismi: Geralt birinchi marta Nilfgaard istilosi ostida qolgan joyga yetib keladi."
    #     },
    #     {
    #         "serial_name": "The Witcher",
    #         "name": "The Witcher: Qism 2",
    #         "part": 2,
    #         "img": "D:/Kino_sayt_media/rasm/witcher-qism2.jpg",
    #         "video_fayl": "D:/Kino_sayt_media/kinolar/witcher-qism2.mp4",
    #         "description": "The Witcher 2-qismi: Geralt Cirini qidirishda xavfli mavjudotlar bilan to‘qnashadi."
    #     },
    #     {
    #         "serial_name": "The Witcher",
    #         "name": "The Witcher: Qism 3",
    #         "part": 3,
    #         "img": "D:/Kino_sayt_media/rasm/witcher-qism3.jpg",
    #         "video_fayl": "D:/Kino_sayt_media/kinolar/witcher-qism3.mp4",
    #         "description": "The Witcher 3-qismi: Yennefer sehrgarlik maktabida o‘zining kuchlarini boshqarishni o‘rganadi."
    #     },
    #     {
    #         "serial_name": "The Witcher",
    #         "name": "The Witcher: Qism 4",
    #         "part": 4,
    #         "img": "D:/Kino_sayt_media/rasm/witcher-qism4.jpg",
    #         "video_fayl": "D:/Kino_sayt_media/kinolar/witcher-qism4.mp4",
    #         "description": "The Witcher 4-qismi: Geralt va Ciri taqdirlarini bog‘lovchi sirli kuchlar haqida bilib oladi."
    #     }
    # ]
    #
    # from .upload_files_github import GitHubStorage
    # from django.core.files.base import File
    # #
    # # for data in top_4_serial:
    # #     with open(data['img'], 'rb') as img_file, open(data['video_fayl'], 'rb') as video_file:
    # #         img_saved = GitHubStorage().save(data['img'], File(img_file))
    # #         video_saved = GitHubStorage().save(data['video_fayl'], File(video_file))
    # #
    # #         Serial.objects.create(
    # #             name=data['name'],
    # #             img=img_saved,
    # #             video_fayl=video_saved,
    # #             sight_age=data['sight_age'],
    # #             reyting=data['reyting'],
    # #             description=data['description']
    # #         )
    #
    # for item in the_witcher_items:
    #     serial_instance = Serial.objects.get(name=item['serial_name'])  # Serialni olish
    #
    #     with open(item['img'], 'rb') as img_file, open(item['video_fayl'], 'rb') as video_file:
    #         img_saved = GitHubStorage().save(item['img'], File(img_file))
    #         video_saved = GitHubStorage().save(item['video_fayl'], File(video_file))
    #
    #         Serial_item.objects.create(
    #             serial=serial_instance,
    #             name=item['name'],
    #             part=item['part'],
    #             img=img_saved,
    #             video_fayl=video_saved,
    #             description=item['description']
    #         )

    kinolars = Kinolar.objects.all()
    random_kinolars = kinolars.order_by('?'[:2])
    select_movies = random.choice(random_kinolars)

    return render(request, 'kino.html', {'kinolars': kinolars, 'select_movies': select_movies, 'ratings': ratings})


def Multfilimlar_views(request):
    multfilms = Multfilm.objects.all()
    random_multfilms = multfilms.order_by('?'[:2])
    select_movies = random.choice(random_multfilms)
    return render(request, 'multfilm.html',
                  {'multfilims': multfilms, 'select_movies': select_movies, 'ratings': ratings})


def Seriallar_views(request):
    serials = Serial.objects.all()
    serial_items = Serial_item.objects.all()
    random_serials = serials.order_by('?'[:2])
    select_movies = random.choice(random_serials)
    return render(request, 'serial.html', {'serials': serials,
                                           'select_movies': select_movies,
                                           'serial_items': serial_items,
                                           'ratings': ratings})


def Animelar_views(request):
    animes = Anime.objects.all()
    anime_item = Anime_item.objects.all()
    random_anime = animes.order_by('?'[:2])
    select_movies = random.choice(random_anime)
    return render(request, 'anime.html',
                  {'animes': animes,
                   'anime_item': anime_item,
                   'select_movies': select_movies,
                   'ratings': ratings})


class KinoListApi(APIView):
    def get(self, request):
        kino = Kinolar.objects.all()
        serializer = KinolarSerializer(kino, many=True)
        return Response(serializer.data)  # Response qoidaga muvofiq

    def post(self, request):
        serializer = KinolarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)  # Response qoidaga muvofiq
        return Response(serializer.errors, status=400)  # Errorni 400 status bilan qaytarish


class KinoDetailApi(APIView):
    def get(self, request, pk):
        try:
            kino = Kinolar.objects.get(id=pk)
        except Kinolar.DoesNotExist:
            return Response({'error': 'Kino not found'}, status=404)
        serializer = KinolarSerializer(kino)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            kino = Kinolar.objects.get(id=pk)
        except Kinolar.DoesNotExist:
            return Response({'error': 'Kino not found'}, status=404)
        serializer = KinolarSerializer(instance=kino, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        try:
            kino = Kinolar.objects.get(id=pk)
            kino.delete()
            return Response({'deleted': True})
        except Kinolar.DoesNotExist:
            return Response({'error': 'Kino not found'}, status=404)


class SerialListApi(APIView):
    def get(self, request):
        serial = Serial.objects.all()
        serializer = SerialSerializer(serial, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SerialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class SerialDetailApi(APIView):
    def get(self, request, pk):
        try:
            serial = Serial.objects.get(id=pk)
        except Serial.DoesNotExist:
            return Response({'error': 'Serial not found'}, status=404)
        serializer = SerialSerializer(serial)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            serial = Serial.objects.get(id=pk)
        except Serial.DoesNotExist:
            return Response({'error': 'Serial not found'}, status=404)
        serializer = SerialSerializer(instance=serial, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        try:
            serial = Serial.objects.get(id=pk)
            serial.delete()
            return Response({'deleted': True})
        except Serial.DoesNotExist:
            return Response({'error': 'Serial not found'}, status=404)


class SerialItemApi(APIView):
    def get(self, request, pk):
        serial_items = Serial_item.objects.filter(serial_id=pk)
        serializer = SerialItemSerializer(serial_items, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        serializer = SerialItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class SerialItemDetailApi(APIView):
    def get(self, request, pk):
        try:
            serial_item = Serial_item.objects.get(id=pk)
        except Serial_item.DoesNotExist:
            return Response({'error': 'Serial item not found'}, status=404)
        serializer = SerialItemSerializer(serial_item)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            serial_item = Serial_item.objects.get(id=pk)
        except Serial_item.DoesNotExist:
            return Response({'error': 'Serial item not found'}, status=404)
        serializer = SerialItemSerializer(instance=serial_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        try:
            serial_item = Serial_item.objects.get(id=pk)
            serial_item.delete()
            return Response({'deleted': True})
        except Serial_item.DoesNotExist:
            return Response({'error': 'Serial item not found'}, status=404)


class MultfilmListApi(APIView):
    def get(self, request):
        multfilm = Multfilm.objects.all()
        serializer = MultfilmSerializer(multfilm, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MultfilmSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class MultfilmDetailApi(APIView):
    def get(self, request, pk):
        try:
            multfilm = Multfilm.objects.get(id=pk)
        except Multfilm.DoesNotExist:
            return Response({'error': 'Multfilm not found'}, status=404)
        serializer = MultfilmSerializer(multfilm)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            multfilm = Multfilm.objects.get(id=pk)
        except Multfilm.DoesNotExist:
            return Response({'error': 'Multfilm not found'}, status=404)
        serializer = MultfilmSerializer(instance=multfilm, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        try:
            multfilm = Multfilm.objects.get(id=pk)
            multfilm.delete()
            return Response({'deleted': True})
        except Multfilm.DoesNotExist:
            return Response({'error': 'Multfilm not found'}, status=404)


class AnimeListApi(APIView):
    def get(self, request):
        anime = Anime.objects.all()
        serializer = AnimeSerializer(anime, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AnimeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class AnimeDetailApi(APIView):
    def get(self, request, pk):
        try:
            anime = Anime.objects.get(id=pk)
        except Anime.DoesNotExist:
            return Response({'error': 'Anime not found'}, status=404)
        serializer = AnimeSerializer(anime)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            anime = Anime.objects.get(id=pk)
        except Anime.DoesNotExist:
            return Response({'error': 'Anime not found'}, status=404)
        serializer = AnimeSerializer(instance=anime, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        try:
            anime = Anime.objects.get(id=pk)
            anime.delete()
            return Response({'deleted': True})
        except Anime.DoesNotExist:
            return Response({'error': 'Anime not found'}, status=404)


class AnimeItemApi(APIView):
    def get(self, request, pk):
        anime_items = Anime_item.objects.filter(anime_id=pk)
        serializer = AnimeItemSerializer(anime_items, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        serializer = AnimeItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class AnimeItemDetailApi(APIView):
    def get(self, request, pk):
        try:
            anime_item = Anime_item.objects.get(id=pk)
        except Anime_item.DoesNotExist:
            return Response({'error': 'Anime item not found'}, status=404)
        serializer = AnimeItemSerializer(anime_item)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            anime_item = Anime_item.objects.get(id=pk)
        except Anime_item.DoesNotExist:
            return Response({'error': 'Anime item not found'}, status=404)
        serializer = AnimeItemSerializer(instance=anime_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        try:
            anime_item = Anime_item.objects.get(id=pk)
            anime_item.delete()
            return Response({'deleted': True})
        except Anime_item.DoesNotExist:
            return Response({'error': 'Anime item not found'}, status=404)
