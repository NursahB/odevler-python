og_a=input('ogrencinin adi:')
og_s=input('ogrencinin soyadi:')
g_ders=int(input('girmedigi ders sayisi:'))

vize=int(input('vize notu:'))
final=int(input('final notu:'))
derst=100-(5*g_ders)


vizeort=vize*30/100
finalort=final*50/100
derstort=derst*20/100
yilsonpuan=vizeort+finalort+derstort

print('girilen ogrenci adi:',og_a)
print('girilen ogrenci soyadi:',og_s)
print('girilen girilmeyen ders sayisi:',g_ders)
print('vize notu:',vize)
print('final notu:',final)
print('ders takip notu:',derst)
print('vize ort:',vizeort)
print('final ort:',finalort)
print('derst ort:',derstort)
print('yil sonu puani:',yilsonpuan)
dosya=open('ogrenci Not Hesaplama.txt','w')
print(og_a,og_s,vize,final,derst,yilsonpuan,file=dosya)
dosya.close()
