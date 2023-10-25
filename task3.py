# ДЗ 3. Необхідно "перевернути" 5-ти значне число
num = int(input('Type num: '))
num1 = (int(num / 10000))
num2 = (int((num-num1*10000)/1000))
num3 = (int((num-num1*10000-num2*1000)/100))
num4 = (int((num-num1*10000-num2*1000-num3*100)/10))
num5 = (num % 10)
num_reversed = (int(num5*10000+num4*1000+num3*100+num2*10+num1))
print(num_reversed)
