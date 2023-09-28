max_chapter = 0
max_chapter_book = ''
max_chapter_bom = 0
max_chapter_input = 0
max_chapter_book_input = ''

user_input = input('Which volume of scriptures would you like to learn about? ')

with open(r'Week 12\books_and_chapters.txt') as file:
    for line in file:
        parts = line.split(':')
        book = parts[0]
        chapter = int(parts[1])
        scripture = parts[2].strip()
        if scripture == 'Book of Mormon':
            print(f'Scripture: {scripture}, Book: {book}, Chapters {chapter}')
            if chapter > max_chapter_bom:
                max_chapter_bom = chapter
                max_chapter_book_bom = book
        if scripture.lower() == user_input.lower():
            if chapter > max_chapter_input:

                max_chapter_input = chapter
                max_chapter_book_input = book
        if chapter > max_chapter:
            max_chapter = chapter
            max_chapter_book = book
        
print()
print(f'The book that has the most chapters is {max_chapter_book} with {max_chapter} chapters.')
print()
print(f'The book in the Book of Mormon that has the most chapters is {max_chapter_book_bom} with {max_chapter_bom}')
print()
print(f'The book that has the most chapter in {user_input.title()} is {max_chapter_book_input} with {max_chapter_input}')