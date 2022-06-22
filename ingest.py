import glob

def ingest_lang(dir = ''): 
    '''
    Ingests the following,
    - README.md
    - All Poetry for all authors in README.md

    - Each language has 15 authors
    '''
    # open file and read contents
    with open(f'{dir}README.md') as file :
        readme = file.readlines()
    
    # read in authors
    authors = [' '.join(line.split(' ')[1:]).split(' (')[0] for line in readme[1:]]

    # grab each corpus
    lang = []
    for author in authors :
        print(f'Ingesting {author} . . .')
        # list all poems by author
        poems = glob.glob(f'{dir}{author}/*.txt')
        print(poems)
        # read in poetry
        poetry = []
        for poem_path in poems :
            # get title from path
            title = poem_path.split('/')[-1].split('.')[0]
            print(f'Ingesting {title}')
            with open(poem_path, encoding = 'utf-8-sig') as poem :
                poetry.append({
                    'title' : title,
                    'corpus' : poem.read().splitlines()
                })
        # append author and corpus to language
        lang.append({
            'name' : author,
            'poetry' : poetry
        })
    
    return lang