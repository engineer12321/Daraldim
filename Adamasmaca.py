isim = input("isminizi girin: ")
print("Merhaba " + isim + " haydi oyun oynayalım :)")

gizli_kelime = "my girlfriend"

bilinmeyen_harf = ""

can = 10

while can > 0:

	karakter_left = 0

	for karakter in gizli_kelime:

		if karakter in bilinmeyen_harf:

			print(karakter)
		else:
			print("-")
			karakter_left += 1

	if karakter_left == 0:
		print("kazandın!!!")	
		break


	tahmin = input("Harf giriniz: ")
	bilinmeyen_harf += tahmin

	if tahmin not in gizli_kelime:
		can -= 1
		print("Yanlış")
		print(f"{can} canınız kaldı.")

		if can == 0:
			print("kaybettin.")
