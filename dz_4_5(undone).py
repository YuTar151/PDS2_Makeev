# 5. Напишіть функцію, яка приймає рядок та повертає літеру, яка зустрічається В ньому найчастіше.

text = "Привет, я дома сейчас...!"
text = text.replace(" ", "")
text = text.replace(",", "")
text = text.replace(".", "")
text = text.replace("!", "")
stat = {}
for ltr in text:
    if ltr in stat:
        stat[ltr] += 1
    else:
        stat[ltr] = 1

revers_stat = {}
a = 0
for k, v in stat.items():
    a = {v: k}
    revers_stat = [revers_stat, a]



stat_dict = stat.items()
stat_dict_values = stat.values()
sorted_key = sorted(stat_dict_values)
sorted_key[-1]

# stat.get(max_key)

print(sorted_key)
print(stat)

# for i in range(len(stat_dict_values)):
#
#
# print(stat_dict_values)

stat_dict_keys = stat.keys()
for i in stat_dict_keys:
    print(i, type(i))

for ltr in stat_dict:
    print(ltr, ":", stat[ltr])
