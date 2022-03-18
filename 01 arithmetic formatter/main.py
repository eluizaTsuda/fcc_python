# This entrypoint file to be used in development. Start by reading README.md
# from pytest import main

from arithmetic_arranger import arithmetic_arranger


#print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49", "1 + 1000", "1000-10"]))
print(arithmetic_arranger(["9a99+9999", "10 -1269", "3801 + 2", "45 + 43", "123 - 9994"],True))
#print(arithmetic_arranger(["9999+9999", "10 -126983"]))


# Run unit tests automatically
# main()