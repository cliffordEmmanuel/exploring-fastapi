# exploring-fastapi

This would detail the knowledge I acquire as I work through several POCs in a bid to understand the fastapi web framework.

## POC 0: Hello world

### Environment Setup

This seems fairly straight forward. Create a virtual environment and install `fastapi` and `uvicorn`. The `uvicorn` is an ASGI server.

### Code

The bare bones code is [here](http://).

```python
@app.get('/')
```

This is the route. This tells FastAPI that the succeeding method should be run when the user requests the `/` path.

```python
async def root():
```

This is a method declaration. The `async def` means the method, in this case `root`, will be run as a Python3 coroutine.

```python
    return {'message':'Hello World!'}
```

This statement sends data to the browser which is a JSON reponse matching the dictionary above.

### The uvicorn server

```terminal
uvicorn hello_world:app --reload
```

This command starts the uvicorn server which generates a webpage on this url: *(<http://127.0.0.1:8000>)*. Which generates the following view:

![hello world](/images/hello_world.jpg)

This is really cool, fast api also generates an interactive API documentation for the api using the `/docs` path.

![interactive docs](/images/interactive_docs.jpg)

### Sources

- Explanation of concurrency and async: [https://fastapi.tiangolo.com/async/](https://fastapi.tiangolo.com/async/)
- Python3 coroutines: [https://docs.python.org/3/library/asyncio-task.html](https://docs.python.org/3/library/asyncio-task.html)

## POC 1: CodingNomads location APIs

This tool enables users to submit best remote working locations for the perusal of others. Using this [guide](https://codingnomads.co/blog/python-fastapi-tutorial).
