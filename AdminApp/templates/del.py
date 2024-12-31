def update(request,id):
    if request.method == 'POST':
        Name1 = request.POST['hotelName']
        Description1 = request.POST.get('hotelDescription')
        Price1 = request.POST.get('bookingPrice')
        try:
            img_c = request.FILES['hotelImage']
            fs = FileSystemStorage()
            file = fs.save(img_c.name, img_c)
        except MultiValueDictKeyError:
            file = Hotel.objects.get(id=id).hotelImage

        Hotel.objects.filter(id=id).update(hotelName=Name1,hotelDescription=Description1,bookingPrice=Price1,hotelImage=file)

    return redirect("View Table")



movieName1 = request.POST['movieName']
		movieGenre1 = request.POST['movieGenre']
		movieLanguage1 = request.POST['movieLanguage']
		movieDescription1 = request.POST['movieDescription']

			img_c = request.FILES['movieImage']
			fs = FileSystemStorage()
			file = fs.save(img_c.name, img_c)
        except MultiValueDictKeyError:
			file = Movie.objects.get(id=id).movieImage
		
		Movie.objects.filter(id=id).update(movieName=movieName1,movieImage=file,movieGenre=movieGenre1,movieLanguage=movieLanguage1,movieDescription=movieDescription1)
	
	return redirect("view")