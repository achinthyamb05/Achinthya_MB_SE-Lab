# Lab 5: Reflection

### 1. Why are mutable default arguments problematic in Python?
When a function is defined, Python evaluates default argument expressions only once at import/definition time, not upon each call. If a mutable object (like a list `[]` or dict `{}`) is used as a default, every invocation that omits the argument operates on the exact same shared instance in memory. This causes side effects where state accumulates across unrelated calls. The safe pattern is setting default to `None` and instantiating the mutable collection inside the function if the argument is `None`.

### 2. What security danger was present in the grant query, and how was it mitigated?
The original SQL query formatted user-supplied strings directly into the query string using `%s` and `%d`. This enabled SQL Injection: an attacker providing malicious text could break out of quotes and execute arbitrary database commands. This was mitigated by using parameterized queries with `?` placeholders, passing variables separately as a tuple to SQLite DB-API. The database engine then treats values strictly as data literals, neutralizing injection.

### 3. Why should catching `Exception` with `pass` be avoided?
Using `except Exception: pass` silently swallows all non-fatal exceptions, masking critical syntax errors, logic flaws, missing files, or runtime failures. It prevents proper debugging, damages system observability, and leaves the application running in an unverified state. Code should catch narrow, explicit exception types and appropriately handle or log them.

### 4. How did Bandit, Pylint, and Flake8 complement each other during static analysis?
- **Bandit** focused on security auditing by analyzing the AST for known vulnerability patterns such as insecure subprocesses, weak exceptions, and SQL injections.
- **Flake8** acted as the syntax and PEP 8 style enforcer, catching formatting inconsistencies, singleton comparison mistakes (`== None`), and line length issues.
- **Pylint** served as the comprehensive code quality and design reviewer, identifying logical traps (mutable defaults), enforcing naming conventions, and demanding complete docstrings.
Together, they ensure security, maintainability, and clean code hygiene without executing the program.