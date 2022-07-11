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

Syntax is:

```terminal
uvicorn <script-name>:<fastapi-object> --reload

For eg:
uvicorn hello_world:app --reload
```

This command starts the uvicorn server which generates a webpage on this url: *(<http://127.0.0.1:8000>)*. Which generates the following view:

![hello world](/images/hello_world.jpg)

This is really cool, fast api also generates an interactive API documentation for the api using the `/docs` path.

![interactive docs](/images/interactive_docs.jpg)

### Issues

Had a `[Errno 98] error while attempting to bind on address ('127.0.0.1', 8000): address already in use` error when sometime, to fix I needed to kill the service that was using the same url:

```terminal
lsof -i :8000
To view all the services using the 8000 port, this will show the process id (pid) of the services too

kill -9 pid
To terminate the guilty process
```

### Sources

- Explanation of concurrency and async: [https://fastapi.tiangolo.com/async/](https://fastapi.tiangolo.com/async/)
- Python3 coroutines: [https://docs.python.org/3/library/asyncio-task.html](https://docs.python.org/3/library/asyncio-task.html)
- [Already in use error](https://www.codegrepper.com/code-examples/shell/uvicorn+ERROR%3A+%5BErrno+98%5D+Address+already+in+use)

## POC 1: CodingNomads location APIs

This tool enables users to submit best remote working locations for the perusal of others. Using this [guide](https://codingnomads.co/blog/python-fastapi-tutorial).

It achieves 2 things:

- creates an API for users to submit locations.
- save the app's data to a database using an ORM.

### Models

Model are created using Pydantic. Pydantic is a data validation library that heavily relies on the python3 type hints, to validate incoming data and serialize outgoing data.

### Configuring a database

Install `sqlalchemy` to help interact with a db.

Seems you have to create 2 models to represent a python object:

- a Pydantic model essentially the "schema" representation. For receiving data from the user as well as sending data to the user.
- a SQLAlchemy model which is the database representation. Used when fetching and inserting records into the database.

Not yet entirely sure why the decoupling is needed.

For methods that interact with the Database objects such as: insert, get etc,, the first parameter should be the SQL Alchemy session.

### Source

- Pydantic [https://pydantic-docs.helpmanual.io/](https://pydantic-docs.helpmanual.io/)
