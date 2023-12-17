# format is used for combine different variables types, strings with integer value

# we can use format() with some {} in variable we want combine

age = 21
txt = "dan kemarin aku berumur {} kamu lupa mengatakannya kepadaku?"
print(txt.format(age))

# format() is unlimited number of arguments

months = 5
hours = 24
yo = 21
x = "bukankah {} bulan lalu menanyakannya? dan kemarin aku menungggu hampir {} jam, saat aku telah berusia {} tahun"
print(x.format(months, hours, yo))

# format() is unlimited number of arguments, but with index number

one = 1
years = 2023
month = 12
y = "sudah {2} bulan dan tahun ini {1} hampir habis, membuatku belajar lebih dari {0} hal"
print(y.format(one, years, month))
