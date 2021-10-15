
import random



def get_lottery_numbers():
    numbers1_50 = [str(random.randint(1,50)) for x in range(0,5)]
    numbers1_10 = [str(random.randint(1,10)) for x in range(0,2)]
    return "Lottery Numbers\n+--------------------+\n\n" +"Numbers between 1 and 50:\n" + "   ".join(numbers1_50) + "\n" + "\nNumbers between 1 and 10:\n" + "   ".join(numbers1_10)


if __name__ == "__main__":
    print(get_lottery_numbers())