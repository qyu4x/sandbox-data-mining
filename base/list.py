waifu = ['Tsukasa', 'Ranko kanzaki', 'Shinna mahiru', 'Kaguya shinomiya']
for wa in waifu : 
    print(wa)



## with index
for index, value in enumerate(waifu):
    print(index , 'has value ', value)


waifu.append('Hayasaka ai')
waifu.append('Shina chan')

for index, value in enumerate(waifu):
    print(index , 'has value ', value)

waifu.remove('Ranko kanzaki')
waifu.pop(4)

for index, value in enumerate(waifu):
    print(index , 'has value ', value)