def filter_messages(messages):
    filtered_messages = []
    dang_count = []
    for message in messages:
        words = message.split()
        good_words = []
        dangs = 0
        for word in words:
            if word == "dang":
                dangs += 1
            else:
                good_words.append(word)
        filtered_message = " ".join(good_words)
        filtered_messages.append(filtered_message)
        dang_count.append(dangs)
    return filtered_messages, dang_count

            
