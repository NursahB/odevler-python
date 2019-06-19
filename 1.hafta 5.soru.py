mutfak=int(input('mutfak masrafi:'))
egitim=int(input('egitim masrafi:'))
giyim=int(input('giyim masrafi:'))
ulasim=int(input('ulasim masrafi:'))
aylikg=int(input('aylik gelir:'))
atm=mutfak+egitim+giyim+ulasim
magorani=atm/aylikg

print('aylik toplam masraf tutari',atm)
print('masrafin aylik gelire orani',magorani)
