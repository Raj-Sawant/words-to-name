def words_to_number(s):
    word_to_num = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        'ten': 10,
        'eleven': 11,
        'twelve': 12,
        'thirteen': 13,
        'fourteen': 14,
        'fifteen': 15,
        'sixteen': 16,
        'seventeen': 17,
        'eighteen': 18,
        'nineteen': 19,
        'twenty': 20,
        'thirty': 30,
        'forty': 40,
        'fifty': 50,
        'sixty': 60,
        'seventy': 70,
        'eighty': 80,
        'ninety': 90,
        'hundred': 100,
        'thousand': 1000,
        'million': 1000000,
        'billion': 1000000000
    }
    
    words = s.lower().replace('-', ' ').replace(' and ', ' ').split()
    current = 0
    total = 0
    
    for word in words:
        num = word_to_num.get(word, 0)
        if num == 100:
            current *= num
        elif num in [1000, 1000000, 1000000000]:
            current *= num
            total += current
            current = 0
        else:
            current += num
    
    total += current
    return total

def format_with_commas(number):
    return "{:,}".format(number)

def main():
    print("Word to Number Converter")
    print("Type 'quit' to exit\n")
    
    while True:
        user_input = input("Enter number in words: ").strip()
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        
        else:
            print("Invalid input. Please try again.\n")

if __name__ == "__main__":
    main()