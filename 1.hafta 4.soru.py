ap=int(input('ana para:'))
fs=int(input('faiz suresi:'))
fo=int(input('faiz orani:'))
ft=ap*fs*fo/100
tp=ap+ft
gs=fs*365
ays=fs*12
gft=ft/gs
aft=ft/ays

print('girilen ana para:',ap)
print('girilen faiz suresi:',fs)
print('faiz orani:',fo)
print('faiz tutari:',ft)
print('toplam para miktari:',tp)
print('gunluk faiz tutari:',gft)
print('aylik faiz tutari:',aft)




