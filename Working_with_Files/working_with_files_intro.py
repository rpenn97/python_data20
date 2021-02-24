# #File doesn't exist: file = open("order.txt")
# def open_and_print_file(file):
#     try:
#         #if you open a file, you MUST CLOSE IT!
#         opened_file = open(file, "r")
#         file_line_list = opened_file.readlines()
#
#         print(file_line_list)
#         for i in file_line_list:
#             print (i)
#
#         opened_file.close()
#
#     except FileNotFoundError as msg:
#         print("There is an error! Panic!")
#         print(msg)
#     finally:
#         print("Execution complete")
#
# open_and_print_file("order.txt")

# #Another way to open files without needing to CLOSE
# def open_and_print_file(file):
#     try:
#         with open(file,"r") as file:
#             file_line_list = file.read()
#             print(file_line_list)
#
#     except FileNotFoundError as msg:
#         print("There is an error! Panic!")
#         print(msg)
#     finally:
#         print("Execution complete")
#
# open_and_print_file("order.txt")

# adding items to a file
def writing_to_file(file, order_item):
    try:
        with open(file, "a") as file:
            file.write(order_item + "\n")
    except FileNotFoundError:
        print("Not found!")

writing_to_file("order.txt", "gyoza dumplings")
