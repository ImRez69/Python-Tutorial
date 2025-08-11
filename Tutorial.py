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
