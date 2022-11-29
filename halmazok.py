reggeli = {'tea', 'vaj', 'pirítós'}
ebed = set()
ebed = set(['halászlé', 'kenyér', True])
print(ebed)

wr=open('H:\iras\ebed.txt','w')
wr.write('[halászlé, kenyér, True]')
wr.close

reggeli.add('lekvár')
reggeli.pop()
#reggeli.remove('sajt')
reggeli.discard('sajt')
reggeli={'víz', 'tea', 'vaj', 'pirítós'}
ebed={'víz', 'halászlé', 'kenyér'}
print(reggeli & ebed)
print(reggeli | ebed)
print(reggeli - ebed)
print(reggeli ^ ebed)

wr=open('H:\iras\reggeli.txt','w')
wr.write('{víz, tea, vaj, pirítós}')
wr.close