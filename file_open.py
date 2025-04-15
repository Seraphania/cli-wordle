# def save_stats(guess_count):
#     if not os.path.isfile(stats):
#         with open(path + stats, 'w') as file:
#             file.write(guess_count)
#     else:
#          with open(path + stats, 'a') as file:
#             file.write(guess_count)    

path = "./resources/"
all_words = "all-words.txt"
target_words = "target-words.txt"
stats = "stat-file.txt"
attempts = 6



def save_stats(guess_count):
    with open(path + stats, 'a+') as file:
        file.write(str(guess_count))
        file.write('\n')



guess_count = 3
save_stats(guess_count)

with open (path + stats, 'r') as file:
    stat_list = []
    for line in file:
        stat_list.append(int(line.strip()))

average_stat = sum(stat_list) / len(stat_list)
print(average_stat)