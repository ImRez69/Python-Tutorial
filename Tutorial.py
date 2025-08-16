# ----- Part 5 (  Data Types ) -----
# Text Type : str
# Numeric Types: int, float, complex

# ---

# print("Alireza") # String # str
# print(type("alireza")) # Get Type

# print("-----------------------------")

# print(20) # Integer # int
# print(type(20)) # Get Type
# print(-20) # Integer # int
# print(type(-20)) # Get Type

# print("-----------------------------")

# print(20.2) # Float # float
# print(type(20.2)) # Get Type

# print("-----------------------------")

# print(20j) # Complex # complex
# print(type(20j)) # Get Type

# ----- Part 6 ( Operators ) -----

# print(2 + 2)  #  4 // جمع
# print(2 - 2)  # 0  // تفریق
# print(2 * 2)  #  4 // ضرب
# print(4 / 2)  #  2.0 // تقسیم ( همیشه عدد اعضاری یا فلوت بر میگردونه )
# print(3 / 2)  #  1.5  // تقسیم ( همیشه عدد اعضاری یا فلوت بر میگردونه
# print(3 // 2)  #  1 // تقسیم اما نتیجه رو به پایین گرد میکند
# print(8 % 3)  # 2  //  باقیمانده
# print(3 ** 2)  #  9 // توان

# ----- Part 7 ( Variable ) -----

#  For Assign Can't User { Character , Number }

# x = 5
# print(x)  # 5

# y = 6
# print(y)  # 6

# print("-----------------------------")

# print(x + y)  # 11

# ---

# Variable Name Role

# myVariableName = "John" # Camel Case
# MyVariableName = "John" # Pascal Case
# my_variable_name = "John" # Snake Case

# ----- Part 8 ( Casting ) -----

#  int() || ( عدد صحیح ) || میتواند عدد صحیح مد نظر یا موجود در "استرینگ" را به عدد صحیح تبدیل کند

# a = int(5) # "تبدیل مقدار مد نظر به یک "اینتیجر
# print(a) # 5
# print(type(a)) # int

# b = int("5") # محتوایت درون "استرینگ" رو به  "اینتیجر"  تبدیل میکند اگر که "اینتیجر" باشد
# print(b) # 5
# print(type(b)) # int

# c = int(5.6) # از اعشار به بعد را حذف میکند
# print(c) # 5
# print(type(c)) # int

# d = int("5.6") # Value Error

# e = int("Amir") # Value Error

# ---

#  float() || ( عدد اعشاری ) || میتواند عدد صحیح و اعشاری مد نظر یا موجود در "استرینگ" را به عدد اعشاری تبدیل کند

# a = float(5)  # "تبدیل مقدار مد نظر به یک "فلوت
# print(a) # 5.0
# print(type(a)) # float

# b = float("5")  # محتوایت درون "استرینگ" رو به  "فلوت"  تبدیل میکند اگر که "اینتیجر یا فلوت" باشد
# print(b) # 5.0
# print(type(b)) # float

# c = float(5.5)
# print(c) # 5.5
# print(type(c)) # float

# c = float("5.5")
# print(c)  # 5.5
# print(type(c))  # float

# e = float("Amir") # Value Error

# ---

#  str() || ( رشته ) || میتواند "استرینگ" مد نظر را به "استرینگ" تبدیل کند

# a = str(5)  # "تبدیل مقدار مد نظر به یک "استرینگ
# print(a) # "5"
# print(type(a)) # str

# b = str("5")  # محتوایت درون "استرینگ" رو به  "استرینگ"  تبدیل میکند
# print(b) # "5"
# print(type(b)) # str

# c = str(5.5)
# print(c) # "5.5"
# print(type(c)) # str

# c = str("5.5")
# print(c)  # "5.5"
# print(type(c))  # str

# e = str("Amir")
# print(e)  # "Amir"
# print(type(e))  # str

# ----- Part 9 ( Strings ) -----

# my_name = "My Name is Amir"
# print(my_name)

# ---

# my_name = "My Name is 'Amir' "
# print(my_name)

# my_name = 'My Name is "Amir" '
# print(my_name)

# ---

# my_name = 'My Name is "Amir" '
# print(my_name)

# my_name = "My Name is 'Amir' "
# print(my_name)

# ---
# \n  - \t - \b

# my_name = "My Name is \nAmir" # \n ( New Line )
# print(my_name)

# my_name = "My Name is \tAmir" # \t ( Tab )
# print(my_name)

# my_name = "My Name is \bAmir" # \b ( Backspace )
# print(my_name)

# ---
# """ """ ( Triple Double Quotation )

# my_name = """My Name is Amir
# My Name is Amir
# My Name is Amir
# My Name is Amir
# """
# print(my_name)

# my_name = ''''
# My Name is Amir
# My Name is Amir
# My Name is Amir
# My Name is Amir
# '''
# print(my_name)

# ---
# ''' ''' ( Triple Quotation )


# my_name = '''My Name is Amir
# My Name is Amir
# My Name is Amir
# My Name is Amir
# '''
# print(my_name)

# my_name = '''
# My Name is Amir
# My Name is Amir
# My Name is Amir
# My Name is Amir
# '''
# print(my_name)

# ----- Part 10 ( Slicing Strings ) -----

# x = "probe"
# print(x[0])  # p
# print(x[2])  # o
# print(x[4])  # e
# print(x[-1])  # e
# print(x[-5])  # p

# ---

# x = "Hello, World"
# print(x[2:5])  # llo // از اندیس 2 تا قبل از اندیس 5 ( تا قبل از اندیس دوم برگردانده میشود )
# print(x[-5:-2])  # llo // از اندیس -5  تا -2 p

# print(x[:5])  # llo // از ابتدا تا اندیس 5
# print(x[2:])  # llo // از اندیس 2 تا آخر

# ----- Part 11 ( Concatenate & Format Strings ) -----

# Concatenate

# String + String
# firstName = "Amir"
# lastName = " Amiri"
# city = " Ahwas"
# me = firstName + lastName  + city
# print(me)  #Amir Amiri Ahwas

# String + " " + String
# firstName = "Amir"
# lastName = "Amiri"
# city = "Ahwas"
# me = firstName + " " + lastName + " " + city
# print(me)  # Amir Amiri Ahwas

# ---

# Format Strings || خودکار تایپ همه را رشته میکند

#  f"{}'
# firstName = "Amir"
# lastName = "Amiri"
# city = "Ahwas"
# me = f" my name is {firstName} and my last name is {lastName} and my city is {city}"
# print(me)  #  my name is Amir and my last name is Amiri and my city is Ahwas

# String + Integer
# age = 30
# txt = "My Age is :" + age
# print(txt)  # Type Error

# String + str( Integer )
# age = 30
# txt = "My Age is : " + str(age)
# print(txt)  # My Age is : 30

#  f"{}'
# age = 30
# txt = f"My Age is : {age}"
# print(txt)  # My Age is : 30

# ----- Part 12 ( Concatenate & Format Strings ) -----

# capitalize()
# txt = "my name is amir"
# print(txt) # my name is amir
# # print(txt.capitalize()) # My name is amir // حرف اول "استرینگ" رو "آپر کیس" یا بزرگ میکنه

# ---

# casefold()
# txt = "My Name is Amir"
# print(txt) # My Name is Amir
# print(txt.casefold()) # my name is amir // تمام حرف های "استرینگ" رو "لور کیس" یا کوچیک  میکنه

# ---

# count(" ")
# txt = "My Name is Amir"
# print(txt) # My Name is Amir
# print(txt.count("m")) # 2 // تعداد استفاده شده ورودی در "استرینگ" را بر میگرداند // به حروف بزرگ و کوچک حساس است
# print(txt.count(" ")) # 3

# ---

# find(" ")
# txt = "My Name is Amir"
# print(txt) # My Name is Amir
# print(txt.find("N")) # 3 // ایندکس" اولین مقدار مطابق با ورودی در "استرینگ" را بر میگرداند"
# print(txt.find("Name")) # 3 // ایندکس اولین مقدار با آن شروع شده است را بر میگرداند

# ---

# format(" ")
# txt = "My Name is Amir {} {}"
# print(txt) # My Name is Amir {} {}
# print(txt.format("Bruh","Bruh2")) # My Name is Amir Bruh Bruh2 // به ترتیب در آکولاد های موجود در "استرینگ" ورودی ها را تنظیم میکند

# ---

# strip()
# txt = "       My Name is Amir     "
# print(txt) # "       My Name is Amir     "
# print(txt.strip()) # My Name is Amir // فاصله های ابتدا و انتها "استرینگ" را حذف میکند

# ---

# title()
# txt = "my name is amir"
# print(txt) # my name is amir
# print(txt.title()) # My Name Is Amir // حروف اول تمامی کلمات "استرینگ" را "آپر کیس" یا بزرگ  میکند )

# ---

# upper()
# txt = "my name is amir"
# print(txt) # my name is amir
# print(txt.upper()) # MY NAME IS AMIR // تمامی حروف "استرینگ" را "آپر کیس" یا بزرگ میکند )

# ---

# lower()
# txt = "MY NAME IS AMIR"
# print(txt) # MY NAME IS AMIR
# print(txt.lower()) # my name is amir // تمامی حروف "استرینگ" را "لور کیس" یا کوچک میکند )

# ---

# len()
# txt = "MY NAME IS AMIR"
# print(txt) # MY NAME IS AMIR
# print(len(txt)) # 15 // طول "استرینگ" را برمیگرداند

# ----- Part 13 ( Booleans ) -----

# True
# print(bool(True)) # True
# print(type(bool(True))) # <class 'bool'>

# print(bool("Bruh")) # True
# print(type(bool("Bruh"))) # <class 'bool'>

# print(bool(" "))  # True
# print(type(bool(" ")))  # <class 'bool'>

# print(bool(20)) # True
# print(type(bool(20))) # <class 'bool'>

# ---

# False
# print(bool(False))  # False
# print(type(bool(False)))  # <class 'bool'>

# print(bool(None))  # False
# print(type(bool(None)))  # <class 'bool'>

# print(bool(0))  # False
# print(type(bool(0)))  # <class 'bool'>

# print(bool(""))  # False
# print(type(bool("")))  # <class 'bool'>

# print(bool(()))  # False
# print(type(bool(())))  # <class 'bool'>

# print(bool(( )))  # False
# print(type(bool(( ))))  # <class 'bool'>

# print(bool([]))  # False
# print(type(bool([])))  # <class 'bool'>

# print(bool([ ]))  # False
# print(type(bool([ ])))  # <class 'bool'>

# print(bool({}))  # False
# print(type(bool({})))  # <class 'bool'>

# print(bool({ }))  # False
# print(type(bool({ })))  # <class 'bool'>

# ---

# Comparison Operators
# x = 20
# z = 15

# print( x == z ) # False
# print( x != z ) # True

# print( x > z ) # True
# print( x < z ) # False

# print( x >= z ) # True
# print( x <= z ) # False

# ----- Part 14 & 15 ( Review 1 & Review 2 - Assignment Operators ) -----

# Assignment Operators

# Mine Reader
#  fisrt_number = int(input("Please Enter a Number Between 1 - 9:"))
# number = fisrt_number
# number *= 2
# number += 8
# number += fisrt_number
# number -= 2
# number /= 3
# number -= fisrt_number
# number *= 4
# number = int(number)
# print(number)


# ----- Part 16 & 17 & 18 & 19 ( Lists 1 & 2 & 3 & 4 ) -----

# Part 16

# my_list = ["bruh", "bruh1", "bruh2", "bruh3"]
# print(my_list)  # ['bruh', 'bruh1', 'bruh2', 'bruh3']
# print(type(my_list))  # <class 'list'>

# print(my_list[1])  # bruh1

# print(len(my_list[1]))  # 5 // طول "ایندکس" 1
# print(len(my_list))  # 4 // "طول "لیست

# ---

# Part 17

# my_list = ["amir", "ali", 3, 5.5, True, 45j, ["d", 3, 4.6, True, 34j]]
# print(my_list) # ['amir', 'ali', 3, 5.5, True, 45j, ['d', 3, 4.6, True, 34j]]
# print(my_list[-1]) # ['d', 3, 4.6, True, 34j]
# print(my_list[-1][2]) # 4.6

# ---

# Part 18

# my_list = ["amir", "ali", "mamad", "morteza", "reza"]
# print(my_list)  # ['amir', 'ali', 'mamad', 'morteza', 'reza']
# print(my_list[1])  # ali
# print(my_list[1:4])  # ['ali', 'mamad', 'morteza']
# print(my_list[:4])  # ['amir', 'ali', 'mamad', 'morteza']
# print(my_list[3:])  # ['morteza', 'reza']
# print(my_list[-1])  # reza
# print(my_list[-3:-1])  # ['mamad', 'morteza']

# new_list = my_list[2:4]
# print(new_list)  # ['mamad', 'morteza']

# ---

# Part 19

# وقتی یک "ایندکس" انتخاب میشود هر چه را اختصاص بدهیم آن را قرار میدهد یک "لیست" یا فقط یک رشته
# وقتی یک محدوده انتخاب میشود باید به آن یک "لیست" اختصاص داده شود در غیر این صورت "اسرتینگ" داده شده را به یک "لیست" تبدیل و دونه دونه حرف هارا در جای مربوط قرار میدهد

# my_list = ["amir", "ali", "mamad", "morteza", "reza"]
# print(my_list)  # ['amir', 'ali', 'mamad', 'morteza', 'reza']

# [1]
# my_list[1] = "BRUH"
# print(my_list)  # ['amir', 'BRUH', 'mamad', 'morteza', 'reza']

# my_list[1] = ["BRUH", "BRUH2"]
# print(my_list)  # ['amir', ['BRUH', 'BRUH2'], 'mamad', 'morteza', 'reza']

# my_list[1:] = ["BRUH"]  # توی این حالت چون انتظار یک "لیست" وجود دارد از رشته به عنوان "لیست" استفاده میشود
# print(my_list)  # ['amir', 'BRUH']

# [1:3]
# my_list[1:3] = "BRUH"  # توی این حالت چون انتظار یک "لیست" وجود دارد از رشته به عنوان "لیست" استفاده میشود
# print(my_list)  # ['amir', 'B', 'R', 'U', 'H', 'morteza', 'reza']

# my_list[1:3] = ["BRUH","BRUH2" ]
# print(my_list)  # ['amir', 'BRUH', 'BRUH2', 'morteza', 'reza']

# my_list[1:3] = ["BRUH", "BRUH2", "BRUH3", "BRUH4"] # زمانی که آیتم های اختصاص داده شده از محدوده انتخاب شده بیشتر باشد به همان اندازه طول "لیست" افزایش میابد
# print(my_list)  # ['amir', 'BRUH', 'BRUH2', 'BRUH3', 'BRUH4', 'morteza', 'reza']

# my_list[1:3] = ["BRUH"]  # اگر کمتر نیز باشد همانگونه طول "لیست" تغییر میکند
# print(my_list)  # ['amir', 'BRUH', 'morteza', 'reza']

# .insert()
# my_list.insert(1,"BRUH")  # در "ایندکس" وارد شده مقدار را اضافه میکند بدون تغییر آن "ایندکس
# print(my_list)  # ['amir', 'BRUH', 'ali', 'mamad', 'morteza', 'reza']

# ----- Part 20 ( Add List Items ) -----

# my_list = ["amir", "ali", "mamad"]
# my_list_2 = ["BRUH", "BRUH2", "BRUH3"]
# my_list_3 = ("BRUH", "BRUH2", "BRUH3")
# print(my_list)  # ['amir', 'ali', 'mamad']

# .append() # به انتهای لیست اضافه میکند
# my_list.append("BRUH")
# print(my_list)  # ['amir', 'ali', 'mamad', 'BRUH']

# my_list.append(["BRUH", "BRUH2"])
# print(my_list)  # ['amir', 'ali', 'mamad', ['BRUH', 'BRUH2']]

# my_list.append(my_list_2)
# print(my_list)  # ['amir', 'ali', 'mamad', ['BRUH', 'BRUH2', 'BRUH3']]

# .insert() به "لیست" اضافه میکند در جای دخلواه
# my_list.insert(2,"BRUH")
# print(my_list)  # ['amir', 'ali', 'BRUH', 'mamad']

# .extend() # لیست" را گسترش میدهد" // هر چیزی که آیتم هایی درون خود دارد را میتواند به لیست اضافه کند // "لیست" ، "تاپل" ، "دیکشنری" و غیره

# my_list.extend(["BRUH", "BRUH2"])
# print(my_list)  # ['amir', 'ali', 'mamad', 'BRUH', 'BRUH2']

# my_list.extend(my_list_2)
# print(my_list) # ['amir', 'ali', 'mamad', 'BRUH', 'BRUH2', 'BRUH3']

# my_list.extend(my_list_3)
# print(my_list) # ['amir', 'ali', 'mamad', 'BRUH', 'BRUH2', 'BRUH3']

# ----- Part 21 ( Remove List Items ) -----

# my_list = ["amir", "ali", "mamad"]
# print(my_list) # ['amir', 'ali', 'mamad']

# .remove()

# my_list.remove("ali") # "حذف "آیتم" دلخواه از "لیست
# print(my_list) # ['amir', 'mamad']

# ---

# .pop()

# my_list.pop(1) # با "پاپ" "ایندکس" دلخواه را حذف میکنیم
# print(my_list) # ['amir', 'mamad']

# my_list.pop() # اگر "ایندکس" ندهیم آخرین مقدار را حذف میکند
# print(my_list) # ['amir', 'ali']

# ---

# del || Keyword

# del my_list[0]# "حذف "ایندکس" دلخواه از "لیست" با کلمه کلیدی "دل
# print(my_list) # ['ali', 'mamad']

# del my_list # حذف کل لیست
# print(my_list) # NameError: name 'my_list' is not defined

# ---

# .clear()

# my_list.clear()# "حذف تمامی مقدار های درون "لیست
# print(my_list) # []

# ----- Part 22 ( Lists 7 ) -----

# .sort() || Alphabetically

# my_list = ["amir", "mamad", "farid"]
# print(my_list)  # ['amir', 'mamad', 'farid']

# my_list.sort()  # "بر اساس حروف الفبا // "اِی" تا "زی
# print(my_list)  # ['amir', 'farid', 'mamad']

# ---

# .sort() || Alphabetically || Case

# my_list = ["amir", "Mamad", "farid", "Zara"]
# print(my_list)  # ['amir', 'Mamad', 'farid', 'Zara']

# my_list.sort()  # اگر حروف بزرگ کوچیک بود اول بزرگ ها "سورت" میشن بعد کوچیک ها
# print(my_list)  # ['Mamad', 'Zara', 'amir', 'farid']

# my_list.sort(key=  str.lower)  # اینگونه تمام حروف کوچک میشوند و بعد "سورت" میشوند
# print(my_list)  # ['amir', 'farid', 'Mamad', 'Zara']

# ---

# .sort() || Alphabetically Descending ( Reverse )

# my_list = ["amir", "mamad", "farid"]
# print(my_list)  # ['amir', 'mamad', 'farid']

# my_list.sort(reverse=True)  # "بر اساس بر عکس حروف الفبا // "زی" تا "اِی
# print(my_list)  # ['mamad', 'farid', 'amir']

# ---

# .sort() || Numerically

# my_list = [100, 23, 4534, 3]
# print(my_list)  # [100, 23, 4534, 3]

# my_list.sort()  # بر اساس ترتیب عددی // کم به زیاد
# print(my_list)  # [3, 23, 100, 4534]

# ---

# .sort() || Numerically Descending ( Reverse )

# my_list = [100, 23, 4534, 3]
# print(my_list)  # [100, 23, 4534, 3]

# my_list.sort(reverse=True)  # بر اساس ترتیب عددی // زیاد به کم
# print(my_list)  # [4534, 100, 23, 3]

# ---

# .reverse()

# my_list = [100, 23, 4534, 3]
# print(my_list)  # [100, 23, 4534, 3]

# my_list.reverse() # ترتیب رو بر عکس میکند
# print(my_list)  # [3, 4534, 23, 100]

# my_list = ["amir", "mamad", "farid"]
# print(my_list)  # ["amir", "mamad", "farid"]

# my_list.reverse()  # بر اساس ترتیب عددی // زیاد به کم
# print(my_list)  # ['farid', 'mamad', 'amir']

# ---

# .copy()

# my_list = ["amir", "mamad", "farid"]
# print(my_list)  # ['amir', 'mamad', 'farid']

# my_list_2 = my_list.copy()  # از "لیست" "کپی" میگیرد
# print(my_list)  # ['amir', 'farid', 'mamad']


# ---

# list()

# my_list = ["amir", "mamad", "farid"]
# print(my_list)  # ['amir', 'mamad', 'farid']

# my_list_2 = list(my_list)  # "از "لیست" "کپی" میگیرد با استفاده از "کلس" "لیست
# print(my_list)  # ['amir', 'farid', 'mamad']

# ---

# +

# my_list = ["amir", "mamad", "farid"]
# my_list_2 = ["amir", "mamad", "farid"]

# my_list_3 = my_list + my_list_2
# print(my_list_3)  # ['amir', 'mamad', 'farid', 'amir', 'mamad', 'farid']

# ---

# extend()

# my_list = ["amir", "mamad", "farid"]
# print(my_list)  # ['amir', 'mamad', 'farid']
# my_list_2 = ["amir", "mamad", "farid"]
# print(my_list_2)  # ['amir', 'mamad', 'farid']

# my_list.extend(my_list_2)
# print(my_list)  # ['amir', 'mamad', 'farid', 'amir', 'mamad', 'farid']


# ----- Part 23 ( Lists 8 ) -----

# How To Seach

# ----- Part 24 ( Tuples ) -----

# تاپل" همان "لیست" است اما نمیتوان از آن چیزی را تغییر ، اضافه و یا کم کرد"
# تمامی "متود" های "لیست" نیز یکی است به جز آنهایی که مربوط به تغییر هستمد زیرا با "ارور" مواجه میشوید

# myTuple = ("amir", "mamad", "farid", "farbod")
# print(myTuple) # ('amir', 'mamad', 'farid', 'farbod')
# print(type(myTuple)) # ('<class 'tuple'>

# ---

# Errors When Try To Change

# myTuple.append("BRUH") # AttributeError: 'tuple' object has no attribute 'append'
# myTuple[1] = "BRUH" # TypeError: 'tuple' object does not support item assignment
# print(myTuple) # ('amir', 'mamad', 'farid', 'farbod')

# ---

# Sliceing

# print(myTuple[0]) # amir
# print(myTuple[1:3]) # ('mamad', 'farid')
# print(myTuple[:2]) # ('amir', 'mamad')
# print(myTuple[1:]) # ('mamad', 'farid')
# print(myTuple[-1]) # farid
# print(myTuple[-3:-1]) # ('amir', 'mamad')

# ---

# Methods

# print(myTuple.count("amir")) # 1
# print(myTuple.index("amir")) # 0

# ---

# Tuple Update

# print(myTuple)  # ('amir', 'mamad', 'farid', 'farbod')

# myList = list(myTuple)
# myList[1] = "BRUH"
# myTuple = tuple(myList)

# print(myTuple)  # ('amir', 'BRUH', 'farid', 'farbod')

# ---

# Tuple Update With Create New Tuple

# print(myTuple)  # ('amir', 'mamad', 'farid', 'farbod')
# newItem = ("BRUH",) # Use Comma for Python Detect That Identified a Tuple
# myTuple += newItem
# print(myTuple)  # ('amir', 'mamad', 'farid', 'farbod', 'BRUH')

# ---

# Tuple Append

# print(myTuple)  # ('amir', 'mamad', 'farid', 'farbod')

# myList = list(myTuple)
# myList.append("BRUH")
# myTuple = tuple(myList)

# print(myTuple)  #('amir', 'mamad', 'farid', 'farbod', 'BRUH')

# ---

# Tuple Remove

# print(myTuple)  # ('amir', 'mamad', 'farid', 'farbod')

# myList = list(myTuple)
# myList.remove("amir")
# myTuple = tuple(myList)

# print(myTuple)  # ('mamad', 'farid', 'farbod')

# ---

# del Tuple

# print(myTuple)  # ('amir', 'mamad', 'farid', 'farbod')
# del myTuple
# print(myTuple)  # NameError: name 'myTuple' is not defined. Did you mean: 'tuple'?

# ---

# Join Tuple

# myTuple = ("amir", "mamad", "farid", "farbod")
# myTuple_2 = ("amir", "mamad", "farid", "farbod")
# myTuple_3 = myTuple + myTuple_2
# print(myTuple_3)  # ('amir', 'mamad', 'farid', 'farbod', 'amir', 'mamad', 'farid', 'farbod')

# ----- Part 25 ( Sets 1 ) -----

# mySet = {"ali", "amir", "mamad"}
# print(mySet) # {'amir', 'mamad', 'ali'}
# print(type(mySet)) # <class 'set'>

# ---

# Unordered & Unindexed

# print(mySet) # {'mamad', 'ali', 'amir'} | {'amir', 'mamad', 'ali'} | یا با هرگونه ترتیبی
# print(mySet[0]) # TypeError: 'set' object is not subscriptable

# ---

# Can Add or Remove

# mySet.pop()
# print(mySet) # {'amir', 'ali'} | یا با هرگونه ترتیبی

# mySet.add("Bruh")
# print(mySet)  # {'ali', 'amir', 'Bruh', 'mamad'} | یا با هرگونه ترتیبی

# ---

# Duplicate Not Allowed

# mySet = {"ali", "amir", "mamad", "ali"}
# print(mySet)  # {'mamad', 'amir', 'ali'} | یا با هرگونه ترتیبی // اگر 2 تا از ی چیز باشد فقط یکی از آنها نمایش داده خواهد شد

# ---

# True & 1 | False & 0 is Same Value in Sets

# mySet = {True, 1}
# print(mySet)  # {True}

# mySet = {False, 0}
# print(mySet)  # False

# ----- Part 26 ( Sets 2 ) -----

# mySet = {"ali", "amir", "mamad"}

# in | Sets

# print("amir" in mySet)  # True
# print("Amir" in mySet)  # False

# ---

# in | List & Tuples

# print("amir" in ["amir", "ali"])  # True
# print("amir" in ("amir", "ali"))  # True

# ---

# .add()

# mySet.add("BRUH")
# print(mySet)  # {'mamad', 'amir', 'BRUH', 'ali'} | یا با هرگونه ترتیبی

# ---

# .update()

# mySet_2 = {"ALI", "MAMAD"}
# mySet.update(mySet_2)
# print(mySet)  # {'MAMAD', 'ALI', 'ali', 'amir', 'mamad'} | یا با هرگونه ترتیبی

# myList2 = ["ALI", "MAMAD"]
# mySet.update(myList2)
# print(mySet)  # {'ALI', 'ali', 'mamad', 'MAMAD', 'amir'} | یا با هرگونه ترتیبی

# myTuple2 = ("ALI", "MAMAD")
# mySet.update(myTuple2)
# print(mySet)  # {'amir', 'mamad', 'ali', 'MAMAD', 'ALI'} | یا با هرگونه ترتیبی

# ---

# .remove()

# mySet.remove("mamad")
# print(mySet) # {'amir', 'ali'}

# ---

# .discard()

# mySet.discard("mamad")
# print(mySet) # {'ali', 'amir'}

# mySet.discard("BRUH")
# print(mySet) # {'ali', 'amir'} // بر خلاف "ریموو" اگر "آیتم" وجود نداشته باشد "ارور" نمیدهد

# mySet.remove("BRUH")
# print(mySet) # KeyError: 'BRUH'

# ---

# .pop()

# mySet.pop()
# print(mySet) # {'ali', 'mamad'} |  {'amir', 'ali'} | یا هر ترتیب دیگه ای

# ---

# .clear()

# mySet.clear()
# print(mySet)  # set()

# ---

# del

# del mySet
# print(mySet)  # NameError: name 'mySet' is not defined

# ---

# .union() or |

# .union()
# mySet2 = {"BRUH", "BRUH2", "BRUH3"}
# mySet3 = mySet.union(mySet2)
# print(mySet)  # {'ali', 'mamad', 'amir'}
# print(mySet2)  # {'BRUH', 'BRUH2', 'BRUH3'}
# print(mySet3)  # {'ali', 'mamad', 'BRUH3', 'BRUH', 'BRUH2', 'amir'}
# mySet2 = {"BRUH", "BRUH2", "BRUH3"}
# mySet3 = {"BRUH4", "BRUH5", "BRUH6"}
# mySet4 = {"BRUH7", "BRUH8", "BRUH9"}
# mySet5 = mySet.union(mySet2, mySet3, mySet4)
# print(mySet5) # {'BRUH5', 'BRUH8', 'BRUH7', 'BRUH9', 'BRUH4', 'mamad', 'amir', 'BRUH', 'BRUH6', 'BRUH3', 'BRUH2', 'ali'}

# |
# mySet2 = {"BRUH", "BRUH2", "BRUH3"}
# mySet3 = mySet | mySet2
# print(mySet)  # {'amir', 'ali', 'mamad'}
# print(mySet2)  # {'BRUH3', 'BRUH', 'BRUH2'}
# print(mySet3)  # {'ali', 'BRUH', 'BRUH2', 'amir', 'BRUH3', 'mamad'}
# mySet2 = {"BRUH", "BRUH2", "BRUH3"}
# mySet3 = {"BRUH4", "BRUH5", "BRUH6"}
# mySet4 = {"BRUH7", "BRUH8", "BRUH9"}
# mySet5 = mySet | mySet2 | mySet3 | mySet4
# print(mySet5) # {'BRUH8', 'amir', 'BRUH9', 'BRUH2', 'ali', 'mamad', 'BRUH', 'BRUH3', 'BRUH4', 'BRUH6', 'BRUH7', 'BRUH5'}

# ----- Part 27 ( Sets 3 ) -----

# --- All in One ---#

# union() // |	# یکی کردن "ست" ها
# print( set1 | set2 )

# update() // |= # "آپدیت کردن "ست 

# difference() // -	# تفاوت های "ست" ها را بازمیگرداند
# print( set1 - set2 )
# difference_update() // -=	# تفاوت های "ست" ها را بازمیگرداند و در "لیست" "آپدیت" میکند
# print( set1 -= set2 )

# intersection() // & # آیتم هایی که در همه "ست" ها مشترک هست را بازمیگرداند
# print( set1 & set2 )
# intersection_update() // &= # آیتم هایی که در همه "ست" مشترک هست را بازمیگرداند و در "لیست" "آپدیت" میکند
# print( set1 &= set2 )

# symmetric_difference() // ^ # آیتم هایی که در همه "ست" ها  مشترک نیست را بازمیگرداند
# print( set1 ^ set2 )
# symmetric_difference_update()	// ^= # آیتم هایی که در همه "ست" ها مشترک نیست را بازمیگرداند و در "لیست" "آپدیت" میکند
# print( set1 ^= set2 )

# --- ---#


# .union() or |

# .union()
# mySet2 = {"BRUH", "BRUH2", "BRUH3"}
# mySet3 = mySet.union(mySet2)
# print(mySet)  # {'ali', 'mamad', 'amir'}
# print(mySet2)  # {'BRUH', 'BRUH2', 'BRUH3'}
# print(mySet3)  # {'ali', 'mamad', 'BRUH3', 'BRUH', 'BRUH2', 'amir'}
# mySet2 = {"BRUH", "BRUH2", "BRUH3"}
# mySet3 = {"BRUH4", "BRUH5", "BRUH6"}
# mySet4 = {"BRUH7", "BRUH8", "BRUH9"}
# mySet5 = mySet.union(mySet2, mySet3, mySet4)
# print(mySet5) # {'BRUH5', 'BRUH8', 'BRUH7', 'BRUH9', 'BRUH4', 'mamad', 'amir', 'BRUH', 'BRUH6', 'BRUH3', 'BRUH2', 'ali'}

# |
# mySet2 = {"BRUH", "BRUH2", "BRUH3"}
# mySet3 = mySet | mySet2
# print(mySet)  # {'amir', 'ali', 'mamad'}
# print(mySet2)  # {'BRUH3', 'BRUH', 'BRUH2'}
# print(mySet3)  # {'ali', 'BRUH', 'BRUH2', 'amir', 'BRUH3', 'mamad'}
# mySet2 = {"BRUH", "BRUH2", "BRUH3"}
# mySet3 = {"BRUH4", "BRUH5", "BRUH6"}
# mySet4 = {"BRUH7", "BRUH8", "BRUH9"}
# mySet5 = mySet | mySet2 | mySet3 | mySet4
# print(mySet5) # {'BRUH8', 'amir', 'BRUH9', 'BRUH2', 'ali', 'mamad', 'BRUH', 'BRUH3', 'BRUH4', 'BRUH6', 'BRUH7', 'BRUH5'}

# ---

# .intersection() or &

# .intersection()
# mySet = {"BRUH"}
# mySet2 = {"BRUH", "BRUH2", "BRUH3"}
# mySet3 = mySet .intersection(mySet2)
# print(mySet3)  # {'BRUH'} // فقط مقادیری که تکرار شده اند را بر میگردند

#  &
# mySet = {"BRUH"}
# mySet2 = {"BRUH", "BRUH2", "BRUH3"}
# mySet3 = mySet & mySet2
# print(mySet3)  # {'BRUH'} // فقط مقادیری که تکرار شده اند را بر میگردند
# mySet = {"BRUH4"}
# mySet2 = {"BRUH", "BRUH4", "BRUH3"}
# mySet3 = {"BRUH4", "BRUH5", "BRUH6"}
# mySet4 = {"BRUH7", "BRUH4", "BRUH9"}
# mySet5 = mySet & mySet2 & mySet3 & mySet4
# print(mySet5)  # {'BRUH4'}

# ---

# .intersection_update() or &=

# mySet = {"BRUH4"}
# mySet2 = {"BRUH", "BRUH4", "BRUH3"}

# mySet.intersection_update(mySet2)
# print(mySet) # {'BRUH4'}

# ---

# .difference() or -

# .difference()
# mySet = {"BRUH4","BRUH5"}
# mySet2 = {"BRUH", "BRUH4", "BRUH3"}
# mySet3 = mySet.difference(mySet2)
# print(mySet3) # {'BRUH5'}

# -
# mySet = {"BRUH4","BRUH5"}
# mySet2 = {"BRUH", "BRUH4", "BRUH3"}
# mySet3 = mySet - mySet2
# print(mySet3) # {'BRUH5'}

# ---

# .difference_update() or -+

# mySet = {"BRUH4", "BRUH5"}
# mySet2 = {"BRUH", "BRUH4", "BRUH3"}

# mySet.difference_update(mySet2)
# print(mySet)  # {'BRUH5'}

# ---

# .symmetric_difference() or ^

# .symmetric_difference
# mySet = {"BRUH4", "BRUH5"}
# mySet2 = {"BRUH", "BRUH4", "BRUH3"}
# mySet3 = mySet.symmetric_difference(mySet2)
# print(mySet3)  # {'BRUH3', 'BRUH', 'BRUH5'}

# ^
# mySet = {"BRUH4", "BRUH5"}
# mySet2 = {"BRUH", "BRUH4", "BRUH3"}
# mySet3 = mySet ^ mySet2
# print(mySet3)  # {'BRUH5', 'BRUH', 'BRUH3'}

# ---

# .symmetric_difference_update() or ^=

# mySet = {"BRUH4", "BRUH5"}
# mySet2 = {"BRUH", "BRUH4", "BRUH3"}
# mySet.symmetric_difference_update(mySet2)
# print(mySet)  # {'BRUH', 'BRUH3', 'BRUH5'}

# ----- Part 28 ( Dictionaries 1 ) -----
