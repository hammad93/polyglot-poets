# polyglot-poets
A multilingual database of poets aiming to capture every language

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