print("hello world")
# tuple are immutable de matlab change bapaki na kigi aw duplication kole che
ali = (' musa','shayan','hammad','king')
print(type(ali))
print(ali[1])
ali = ('musa','shayan','hammad','king')
x = list(ali)
y = x.insert(5,'musssa')
print(x)
ali = ('musa','shayan','hammad','king')
y = ('khan',)
ali +=y
print(ali)
ali = ('musa','shayan','hammad','king')
y = ('khan',)
ali +=y
print(ali+y)
#unpaking multiple value che har yo value yar eyotha asing kam
ali = ('musa','shayan','hammad','king')
(khan,hmm,khani,pirate,) = ali
print('musa',khan)
print('shayan',hmm)
print(khan)
ali = ('musa','shayan','hammad','king')
for i in range(len(ali)):
    print(ali[i])
ali = ('musa','shayan','hammad','king')
for i in range(len(ali)):
    print([i])
ali = ('musa','shayan','hammad','king')
print(ali*2)
print(ali.count('musa'))
ali = ('musa','shayan','hammad','king')
print(ali.index('musa'))
# set use to store multiplle itam set is unchangable
ali = {'musa','shayan','hammad','king'}
ali.add('lion')
print(ali)
ali = {'musa','shayan','hammad','king'}
ali.remove('king')
print(ali)
# this a decitnaories
ali = {'st_name':'shayan','class':'5th'}
print(ali)
ali = {'st_name':'shayan','class':'5th'}
print(ali['st_name'])
print(ali.get('class'))
print(ali.keys())
print(ali.values())
ali = {'st_name':'shayan','class':'5th'}
print(ali.keys())
print(ali.values())
print(len(ali))
ali = {'st_name':'shayan','class':'5th'}
ali['addrease']= 'pirqalla'
print(ali)
ali = {'st_name':'shayan','class':'5th'} # pa dec ki index keys de
ali = {'st_1':{'name':khan},'st_2':{'ahmadali':'khan'}}
print(ali) #this is nesteads dec khai
ali = {'st_1':{'name':khan},'st_2':{'ahmadali':'khan'}}
print(ali['st_1']['name'])
ali = {'st_1':{'name':khan},' st_2':{'ahmadali':'khan'}}
print(ali['st_2']['ahmadali'])
