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
