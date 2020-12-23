is_cloudy = True
is_rainy = False

if is_cloudy:
    print("It is cloudy")
else:
    print("It's not cloudy")

if is_rainy:
    print("It is rainy")
else:
    print("It is not rainy")

if is_cloudy and is_rainy:
    print("It is cloudy and rainy")
elif is_cloudy and not(is_rainy):
    print("It is cloudy but not rainy")
elif not(is_cloudy) and is_rainy:
    print("It is not cloudy but it is rainy")
elif not(is_cloudy) and not(is_rainy):
    print("It is not cloudy nor rainy")
