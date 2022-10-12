# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
text = 'aaasssddFFsd'
lst = [text[i] for i in range(len(text))]
print (lst)

# def encode_mess(lst):
#     encode_lst = ""
#     i = 0
#     while (i <= len(lst)-1):
#         count =1
#         ch = lst[i]
#         j=i
#         while (j < len(lst)-1):
#             if (lst[j] == lst[j+1]):
#                 count= count + 1
#                 j = j+1
#             else:
#                 break
#         encode_lst = encode_lst + str(count) + ch
#         i = j+1
        

#     return encode_lst

# text = 'aaasssddFFsd'
# lst = [text[i] for i in range(len(text))]
# print (lst)

# lst1 = encode_mess(lst)
# lst2 = lst1.replace("1", "")
# print(lst2)