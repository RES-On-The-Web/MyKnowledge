    # 5. Data Structures
    # 5.1. More on Lists
#
# l = []
# for i in range(5):
#     l.append(i)
#     print(l)
#
# # #
#
# l = []
# for i in range(5):
#     l.extend([i])
#     print(l)
#
# # #
#
# l1 = [0,1,2,3,4]
# l1.insert(0,10)
# print(l1)
#
# # #
#
# l2 = [0,1,2,3,4]
# l2.remove(4)
# print(l2)
#
# # #
#
# l3 = [0,1,2,3,4]
# print(l3.pop())
# print(l3)
# print(l3.pop(2))
# print(l3)
#
# # #
#
# l4 = [0,1,2,3,4]
# l4.clear()
# print(l4)
#
# # #
#
# l5 = [0,1,2,3,2]
# print(l5.index(2))
#
# # #
#
# l6 = [0,1,2,3,2,2]
# print(l6.count(2))
#
# # #
#
# l7 = [0,1,2,3,2]
# l7.sort()
# print(l7)
#
# # #
#
# l8 = [0,1,2,3,2]
# l8.reverse()
# print(l8)
#
# # #
#
# l9 = [0,1,2,3,2]
# l10 = l9.copy()
# l11 = l9
# # l10.pop()
# l11.pop()
# print(l9,l10,l11)


    # 5.1.1. Using Lists as Stacks
    # 5.1.2. Using Lists as Queues
#
# from collections import deque
# q = deque([0,1,2,3,4,5])
# q.append(6)
# q.append(7)
# print(q)
# print(q.popleft())
# print(q)


    # 5.1.3. List Comprehensions
#
# lc1 = [i for i in range(10)]
# print(lc1)
#
# # #
#
# lc2= [x*y for x in [1,2,3] for y in [1,2,3] if x!=y]
# print(lc2)
#
# # #
#
# vec_1 = [-4,-2,0,2,4]
# vec2 = [x*2 for x in vec_1]
# print(vec2)
# vec3 = [x for x in vec_1 if x>=0]
# print(vec3)
# vec4 = [abs(x) for x in vec_1]
# print(vec4)
# vec_2 = ['   hamed  ','mamad   ','    hasan' ]
# vec5 = [name.strip() for name in vec_2]
# print(vec5)
# vec6 = [(x,x**2) for x in vec_1]
# print(vec6)
# vec_3 = [[1,2,3],[1,2,3],[1,2,3]]
# vec7 = [item for Ld in vec_3 for item in Ld]
# print(vec7)


    # 5.2. The del statement
#
# ll = [1,2,3,4,5,6]
# del ll[0]
# print(ll)


    # 5.3. Tuples and Sequences
# 
# empty = ()
# atuple = ('hello',) #or 'hello',
# print(empty,atuple)


    # 5.4. Sets
#
# # NOT in order
#
# emptySet = set(()) #or set()
# print(emptySet)
# 
# # # 
# 
# users = {'hamed','mamad','hasan','hamed'} # =set(('hamed','mamad','hasam')) !=set('hamed','mamad','hasam')
# print(users)
# print('hamed' in users)
# print('hosain' in users)
# 
# # #
# 
# a = set('hamed') # =set(('hamed')) !=set(('hasan'),)
# b = set('hasan')
# print(a,b)
# print(a - b)  # letters in a but not in b
# print(a | b)  # letters in a or b or both
# print(a & b)  # letters in both a and b
# print(a ^ b)  # letters in a or b but not both
# print({x for x in a for y in b if x!=y})


    # 5.5. Dictionaries
#
# tel = {"hamed":2312,"hasan":2343,"hosain":3221}
# print(tel["hamed"])
# # print(tel["mamadqholi"]) #KeyError
# print(tel.get("mamadqholi"))
# del tel["hosain"]
# print(tel)
# print(list(tel))
# print(sorted(tel))
# print("hasan" in tel)
# print("hosainqholi" in tel)
# example1 = dict([("hamed",1232),("mamad",34234),("hasan",23321)])
# print(example1)
# example2 = dict(hamed=23423,mamad=3242,hasan=34234)
# print(example2)
#
# #
#
# print({x: x**2 for x in range(0,5)})


    # 5.6. Looping Techniques
#
# tel = {"hamed":2312,"hasan":2343,"hosain":3221}
# for k,v in tel.items():
#     print(k,v)
#
# #
#
# listi = [23423,234,234,234]
# for i,v in enumerate(listi):
#     print(i,v)
#
# #
#
# listi1 = [23423,234,2344,234]
# listi2 = [12312,123,12,1,23]
# print(zip(listi1,listi2))
# for it in zip(listi1,listi2):
#     print(it)
#
# #
#
# for i in reversed(range(0,6)):
#     print(i)
#
# #
#
# listi2 = [12312,123,12,1,23,23]
# for i in sorted(set(listi2)):
#     print(i)


    # 5.7. More on Conditions
    # 5.8. Comparing Sequences and Other Types