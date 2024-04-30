## Memory script

This script will send alarm on API address if memory usage higher than some level.

Call this script with arguments:

1. limit - limit of memory usage in percent.
2. address - API address to send alarm.
3. time - period of scaning in seconds.

### Example

Here's an example of how to run the script:

```bash
python memory.py 88 http://127.0.0.1:5000/ 60
```

It will send alarm on localhost every 60 seconds if memory usage higher than 88 percent.
