def task_9():

    words = ["яблоко", "груша", "банан", "киви", "апельсин", "ананас"]
    result = {}

    for word in words:

        first_letter = word[0]

        if first_letter not in result:

            result[first_letter] = []
    
        result[first_letter].append(word)

    print(result)