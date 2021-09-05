# WARP: Wrapper around Replicated Processes

WARP is a light-weight weight manager for background processes.

Functionality
* Easily spawn any process as a managed subprocess
* Automatic recover from failed process
* Runs completely async
* Cleanly exits in a safe order (subprocess, WARP manager, then main process)

### Overview
So you need to run a subprocess in the background of your Python application. How do you do it?
* If you simply start the process in an async way, how can you ensure that the process can is restarted if it exits?
* If you start the process in a synchronous way, how do you ensure that the rest of your program continues to execute?
* If you use `supervisord`, how do you ensure that all your users have `supervisord` installed ahead of time?
* If you use `celery` or some kind of heavy weight solution, you now need standalone infra and need to manage a lot of complexity

WARP makes it very simple to manage a background process in a self-healing way. The subprocess runs in a background
thread that continually monitors the health of the subprocess. WARP is also able to intelligently support interrupt
signals.

### Installation

`pip install warp`

### Usage

Import WARP
```python
from warp import Warp
```

Create a WARP object
```python
wp = Warp(command="dummy_server.py")
```

Start the WARP process

```python
wp.start()
```

The process will automatically be killed (cleanly) when the main process exits

Alternatively you may also forcefully stop this background process

```python
wp.stop()
```

### Testing

Run the following command from the repo root
```bash
pytest
```

### Python Compatibility

WARP only supports the following Python versions
* 3.7
* 3.8
* 3.9

### Contributing

WARP is a community project. Feel free to submit a PR and/or an issue if you are looking for more functionality or found a bug!
