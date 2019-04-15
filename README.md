# polyglot-poets
A multilingual database of poets for the most popular languages. This repository aims to provide a programmable interface for natural language processing (NLP).

# License
MIT License (https://opensource.org/licenses/MIT)

# REST API
The REST API uses Swagger UI and flask.

# Data Structure

## Language
```python
class language:

    def __init__(self, name):
        self.name = name
```

### Poet

#### Poem