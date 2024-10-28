with open("./story.txt", "r") as story:
    pairs = []
    for content in story.readlines():
        content = content.strip()
        if len(content) > 0:
            start_index = 0
            while True:
                start_index = content.find("<", start_index)
                if start_index == -1:
                    break
                end_index = content.find(">", start_index)
                if end_index == -1:
                    break
                pairs.append((start_index, end_index))
                start_index = end_index + 1
