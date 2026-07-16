A web server access log is saved at /app/access.log in your working directory. Each line is a standard Apache/Nginx combined-format entry: it begins with the client IP address and contains a quoted request line such as "GET /index.html HTTP/1.1".

Parse the log and write a summary report as a single JSON object to the absolute path /app/report.json. The object must contain exactly these three keys:

- total_requests: integer — the number of non-empty log lines (one request per line).
- unique_ips: integer — the number of distinct client IP addresses (the first whitespace-separated field on each line).
- top_path: string — the request path that appears most frequently across all requests.

Success criteria:
1. /app/report.json exists and contains a single valid JSON object whose keys are exactly total_requests, unique_ips, and top_path.
2. total_requests equals the number of requests in the log.
3. unique_ips equals the number of distinct client IP addresses in the log.
4. top_path equals the most frequently requested path.
