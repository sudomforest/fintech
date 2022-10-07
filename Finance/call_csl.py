# -------------------------------
# call.py
# -------------------------------

# from pkg.mypkg import child_module as cm
# cm.myprint("a")
# cm.myprint2("b")
# print( cm.point )
# # -------------------------------
# from pkg.mypkg.child_module import myprint, myprint2, point
# myprint("cc")
# myprint2("dd")
# print(point)
# # -------------------------------
# from pkg.mypkg.child2_module import Child2Class
# Child2Class.pay(55)
# obj = Child2Class()
# obj.ins_pay()
# # -------------------------------
# from pkg.mypkg.child2_module import Child2Class
# obj = Child2Class()
#       #obj.__init__()
# print(obj)
#
# obj.ins_pay()
# obj.ins_num_pay(99)
# # # -------------------------------
# from pkg.mypkg.child2_module import Child2Class, ParentClass
# obj1 = Child2Class('아무개')
# obj2 = Child2Class('홍길동')

# print(obj1.point, obj2.point, Child2Class.point)
# obj1.point = 500
# Child2Class.point = 50000
#
# print(obj2.point)  #10000
# print(Child2Class.point )  #50000


# # -------------------------------
# from pkg.mypkg.child2_module import ParentClass
# p = ParentClass()
# p.auth("kim")

from pkg.mypkg.child2_module import Child2Class
obj1 = Child2Class('아무개', 1000, 'silver')
obj2 = Child2Class('홍길동', 1000, 'silver')

obj1.auth("lee")
obj1.auth22("lee")
Child2Class.pay(55,"2022")





