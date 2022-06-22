from cobe.brain import Brain
import ingest

data = ingest.ingest_langs()
for lang in data :
    for author in lang['poetry'] :
        name = author['name']
        print(f'Training {name} . . .')
        author_brain = Brain(name)
        for poem in author['poetry'] :
            for line in poem['corpus'] :
                author_brain.learn(line)