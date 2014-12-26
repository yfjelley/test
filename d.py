#!/usr/bin/env python
#
# -*- coding : utf-8 -*-

d ={'a':{'x':[[11,2],[11,2],[12,2],[13,1]],'y':[[9,2],[8,1],[7,1],[6,1]]},'c':{'x':[[10.1,2],[11.1,2],[12.1,2],[13.1,1]],'y':[[9.2,1.3],[8.2,1],[7.2,1],[6.2,1]]},'b':{'x':[[10.2,2],[11.2,2],[12.2,2],[13.2,1]],'y':[[9.1,1.4],[8.1,1],[7.1,1],[6.1,1]]}}
print d
for k,v in d.iteritems():
    print k,v['y']
    print "xxxxxxxxxxxxx"
s =[{k:v['y']} for k, v in d.iteritems()]
print "s:%s" % s
btc_amount = {}
for key in d:
    count = 0
    for i in d[key]['y']:
        count += i[1]*i[0]
        if count >4:
            btc_amount[key] = float(count)/i[1]
            break

s = [v['y'] for v in d.itervalues()]
for f in s:
    count = 0
    for i in f:
        count += i[0] * i[1]
        if count >4 :
            print key, i, count
    print "f:%s" % f
print s
s = [{k:v['y']} for k, v in d.iteritems() ]
l = map(lambda x:[{k:v[0]} for k,v in x.iteritems()] ,a)
for i in s:
    for k,v in i.iteritems():
        l.append()
l = [{k:v[0]} for k,v in s[0].iteritems()]
print '********** l:%s' % l
amount = 0
while True:
    m = max(l)
    amount += m[1]
    l.remove(m)
    print 'tm',m
    for o in s:
        if m in o:
            l.append(o[o.index(m)+1])
    if amount > 7:
        break
print l,amount

