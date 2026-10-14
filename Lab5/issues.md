# Issues Identified and Resolved

| Issue | Type | Line(s) | Description | Fix Approach |
| :--- | :--- | :--- | :--- | :--- |
| SQL Injection | Security (Bandit B608) | 10 | String interpolation formatting (`%s`, `%d`) used directly in an SQL query string allows arbitrary SQL injection. | Replaced string formatting with parameterized query placeholders (`?`) and passed values as a tuple. |
| Insecure Process Call | Security (Bandit B605, B607) | 27 | Using `os.system()` to invoke a shell command introduces shell injection vulnerabilities and depends on shell resolution. | Replaced `os.system` with `subprocess.run(["echo", "archiving awards"], check=True)`. |
| Broad Exception Clause | Quality / Security (Bandit B110 / Pylint W0703) | 28–29 | `except Exception: pass` silently suppresses all non-system exceptions without handling or logging. | Caught specific exceptions (`subprocess.SubprocessError`, `OSError`) rather than standard broad exceptions. |
| Mutable Default Argument | Bug / Quality (Pylint W0102 / Flake8 B006) | 9 | `audit=[]` creates a mutable list evaluated once at definition, sharing state across independent function calls. | Changed default parameter to `None` and initialized `audit = []` inside the function body. |
| Singleton Comparison | Style (Flake8 E711 / Pylint C0121) | 33 | Comparisons to `None` must be done using identity comparison (`is`), not equality (`==`). | Replaced `if scheme == None:` with `if scheme is None:`. |
| Naming Convention | Style (Pylint C0103) | 32 | Function name `bySchemeCount` does not follow PEP 8 snake_case style naming standards. | Renamed function to `by_scheme_count`. |
| Missing Docstrings | Documentation (Pylint C0114, C0116) | 1, 9, 15, 25, 32, 38 | Missing module and function docstrings reduces code maintainability and documentation score. | Added descriptive docstrings to the module and all function definitions. |