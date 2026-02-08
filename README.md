# lucos_loganne_pythonclient
A python client for sending events to [lucos_loganne](https://github.com/lucas42/lucos_loganne).

## Environment Variables
The following environment variables must be set for the package to function:

* `SYSTEM`: A unique identifier for the system or service sending the events. This is used as the `User-Agent` in the HTTP request and the `source` field in the loganne event.
* `LOGANNE_ENDPOINT`: The full URL of the `/events` endpoint of a running `lucos_loganne` instance.

## API
The package exposes a single function:

### `updateLoganne(type, humanReadable, url=None)`
Sends an event to the Loganne service.

* **type** (str, required): The type of event being logged.
* **humanReadable** (str, required): A description of the event that is easy for humans to understand.
* **url** (str, optional): A link to a human-readable page regarding the item the event pertains to. Defaults to `None`.

## Usage
```python
from loganne import updateLoganne

# Ensure SYSTEM and LOGANNE_ENDPOINT env vars are set
updateLoganne(
    type="contactUpdated",
    humanReadable="The Contact \"John Doe\" has been updated",
    url="https://contacts.example.com/contact/123456"
)
```

