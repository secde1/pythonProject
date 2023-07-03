# a = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
# result = []
# for j in a:
#     for r in j:
#         result.append(r)

# print(tuple(result))
# a = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
# print(tuple([j for i in a for j in i]))

# def Tuple_(a: tuple):
#     for j in a:
#         yield tuple(j)
#
# a = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
# print(Tuple_([j for i in a for j in i]))

# def Tuple_(a):
#     for j in a:
#         yield j
#
# a = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
# print(tuple(Tuple_(j for i in a for j in i)))





# k = [1, 2, 2, 3, 3, 3]
# count = 0
# res = []
# for i in k:
#     if i == i+1:
#
#         res.append({
#             'number' : i,
#             'count' : count
#
#         })
# print(res)
# arr = [1, 2, 2, 3, 3, 3]
#
# result = {}
# for i in a:
#     if i in result:
#         result[i] += 1
#     else:
#         result[i] = 1
#
# for i, count in result.items():
#     print(f"{i}: {count}")




# arr = list(map(int, input("massiv elemenlarini kiriting: ").split()))
# for i in set(arr):
#     print(f"{i} son {arr.count(i)} martta takrorlangan ")


# arr = [3, 4, 6, 2, 1, 9]
# print(sorted(arr[len(arr)//2:], reverse=True) + sorted(arr[:len(arr)//2]))



# nums = [1,2,3,4,5,6,7,8]
# array1 = []
# array2 = []
# for i, v in enumerate(nums):
#     if i & 1:
#         array2.append(v)
#     else:
#         array1.append(v)
# print('array1', array1)
# print('array2', array2)

nums = [1,2,3,4,5,6,7,8]



# import statistics
# nums = [3,1]
# print(statistics.mean(nums))

from colorama import init,Fore
if __name__ == '__main__':
    init()

    # print(Fore.RED + """
    # ▄▄▄▄    ██▓    ▄▄▄       ▄████▄   ██ ▄█▀ ▄▄▄▄    ██▓ ██▀███  ▓█████▄
    # ▓█████▄ ▓██▒   ▒████▄    ▒██▀ ▀█   ██▄█▒ ▓█████▄ ▓██▒▓██ ▒ ██▒▒██▀ ██▌
    # ▒██▒ ▄██▒██░   ▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▒██▒ ▄██▒██▒▓██ ░▄█ ▒░██   █▌
    # ▒██░█▀  ▒██░   ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ▒██░█▀  ░██░▒██▀▀█▄  ░▓█▄   ▌
    # ░▓█  ▀█▓░██████▒▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄░▓█  ▀█▓░██░░██▓ ▒██▒░▒████▓
    # ░▒▓███▀▒░ ▒░▓  ░▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒░▒▓███▀▒░▓  ░ ▒▓ ░▒▓░ ▒▒▓  ▒
    # ▒░▒   ░ ░ ░ ▒  ░ ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░▒░▒   ░  ▒ ░  ░▒ ░ ▒░ ░ ▒  ▒
    # ░    ░   ░ ░    ░   ▒   ░        ░ ░░ ░  ░    ░  ▒ ░  ░░   ░  ░ ░  ░
    # ░          ░  ░     ░  ░░ ░      ░  ░    ░       ░     ░        ░
    #     ░                  ░                     ░               ░
    #                                     """ )
    print(Fore.RED + """

SECDETSECDETSECDETSECDETSECDETSECDETSECDETSECDETSECDET
 ██████╗███████╗  ██████╗ █████▄  ███████╗ █████████╗
██╔════╝██╔════╝ ██╔════╝ ██╔═╗█▄ ██╔════╝    ███╔══╝ 
██║     █████╗   ██║      ██║  ║█ █████╗      ███║
██║     ██╔══╝   ██║      ██╚═╝█▀ ██╔══╝      ███║
 ██████╗███████╗  ██████╗ █████▀╔ ███████╗    ███║
 ╚═════╝ ╚═════╝  ╚═════╝ ╚═════╝ ╚══════╝    ╚══╝
SECDETSECDETSECDETSECDETSECDETSECDETSECDETSECDETSECDET
    """)


'''

 ██████╗███████╗  ██████╗ █████▄   ███████╗ █████████╗
██╔════╝██╔════╝ ██╔════╝ ██╔══╗█▄ ██╔════╝    ███╔══╝ 
██║     █████╗   ██║      ██║  ║██ █████╗      ███║
██║     ██╔══╝   ██║      ██╚══╝█▀ ██╔══╝      ███║
 ██████╗███████╗  ██████╗ █████▀╔╝ ███████╗    ███║
 ╚═════╝ ╚═════╝  ╚═════╝ ╚═════╝  ╚══════╝    ╚══╝
                          '''

'''
   ▄▄▄▄▄▄
    ▓███████▄
    ▓███
    ▓███
    ▓███
    ▓███
    ░▒▓█████▀
    '''













