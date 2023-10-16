# Log Parsing Script

## Overview
This project entails the development of a log parsing script that reads input data from the standard input (stdin) line by line and computes various metrics from the log entries. The script's primary purpose is to extract and analyze information from log entries conforming to a specific format. It calculates total file size and counts the occurrences of various HTTP status codes within the log data. The script also provides an option to print these statistics at specific intervals or upon user interruption (CTRL + C).

## Project Components
The project consists of the following key components:

1. **Log Entry Format**: The script expects input data in the following format:
   ```
   <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
   ```
   If a line does not adhere to this format, it is skipped.

2. **Metrics Computation**: The script computes the following metrics:
   - **Total File Size**: The sum of all file sizes encountered in the log entries.
   - **Number of Lines by Status Code**: Counts the occurrences of HTTP status codes (200, 301, 400, 401, 403, 404, 405, and 500) and presents the results in ascending order.

3. **Interval Printing**: The script prints the metrics after every 10 lines have been processed or in response to a keyboard interruption (CTRL + C).

## Usage
To use the log parsing script, follow these steps:

1. Ensure you have Python installed on your system.
2. Execute the script and redirect log data to its standard input, for example:
   ```
   cat logfile.txt | python log_parser.py
   ```

## Output
The script generates the following output:

- After processing every 10 lines or upon interruption, it will print the following statistics:
   ```
   Total File Size: <total size>
   ```
   where `<total size>` represents the cumulative file size encountered in the log entries.

- For each HTTP status code (200, 301, 400, 401, 403, 404, 405, and 500) found in the log entries, the script prints the count in ascending order:
   ```
   <status code>: <number>
   ```

## Example Output
Here's an example of what the output might look like (actual values may vary):

```
Total File Size: 1234567
200: 20
301: 5
403: 2
404: 10
```

## Error Handling
The script is designed to skip lines that do not match the expected log entry format. If any status code is not an integer or if a status code does not appear in the log entries, it will not be included in the status code count.

## Dependencies
The script has no external dependencies. It requires a Python interpreter to run.

## Conclusion
The log parsing script is a useful tool for analyzing log data in a specific format, providing insights into the total file size and the distribution of HTTP status codes. This README provides an overview of the project, its components, usage, and expected output. Users can adapt the script to their specific log data and requirements.