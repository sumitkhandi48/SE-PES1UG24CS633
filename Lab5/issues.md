# Lab 5 - Static Code Analysis

## Issues I Found and Fixed

| Issue | Type | Line(s) | What I noticed | How I fixed it |
|---|---|---|---|---|
| SQL injection | Security - Medium | 11 | The query was made using `.format()`. Putting input directly into a query can cause problems. | I changed it to use `?` placeholders and pass the values separately. |
| MD5 hashing | Security - High | 16 | The program was using MD5 to create the farmer's token. | I changed MD5 to SHA-256. |
| `os.system()` | Security - High | 31 | The program was using a shell command just to print a message. | I removed it and used Python's `print()` instead. |
| Missing docstrings | Code quality | Multiple | It wasn't clear what some of the functions were supposed to do. | I added a short description for each function. |
| Function names | Code quality | Multiple | The function names were written in camelCase. | I changed them to snake_case, like `record_milk()` and `daily_total()`. |
| Unused import | Code quality | 2 | `json` was imported, but it wasn't used anywhere. | I removed that import. |
| Long lines | Formatting | 7, 11, 20, 25 | A few lines were too long and made the code harder to read. | I split those lines into smaller lines. |
| `None` comparison | Code quality | 36 | The code checked for a missing value using `fat == None`. | I changed it to `fat is None`. |
| Variable name | Readability | 26 | The variable `l` wasn't a clear name, so it was hard to understand at first. | I renamed it to `largest_farmer`. |
| Database connection name | Code quality | 10 | The function used the same name for its connection parameter as the global connection. | I renamed the parameter to `connection` and moved database setup inside `main()`. |

