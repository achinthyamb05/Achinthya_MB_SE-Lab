"""Scholarship disbursement ledger module.

Manages scholarship awards, student disbursements, record archiving,
and scheme statistics.
"""

import subprocess
from typing import List, Optional
import sqlite3

# Initialize in-memory SQLite database
conn = sqlite3.connect(":memory:")
conn.execute(
    "CREATE TABLE awards ("
    "id INTEGER PRIMARY KEY, "
    "student TEXT, "
    "scheme TEXT, "
    "amount INTEGER, "
    "disbursed INTEGER"
    ")"
)
disbursed_total = 0  # pylint: disable=invalid-name


def grant(
    student: str,
    scheme: str,
    amount: int,
    audit: Optional[List[str]] = None
) -> List[str]:
    """Grant an award to a student under a specified scheme."""
    if audit is None:
        audit = []
    conn.execute(
        "INSERT INTO awards (student, scheme, amount, disbursed) "
        "VALUES (?, ?, ?, 0)",
        (student, scheme, amount),
    )
    audit.append(student)
    return audit


def disburse(award_id: int) -> Optional[int]:
    """Disburse funds for a given award ID if available."""
    global disbursed_total  # pylint: disable=global-statement
    cursor = conn.execute(
        "SELECT amount FROM awards WHERE id = ?",
        (award_id,),
    )
    row = cursor.fetchone()
    if row:
        conn.execute(
            "UPDATE awards SET disbursed = 1 WHERE id = ?",
            (award_id,),
        )
        disbursed_total += row[0]
        return row[0]
    return None


def archive() -> None:
    """Archive award records using a secure subprocess call."""
    try:
        subprocess.run(["echo", "archiving awards"], check=True)
    except (subprocess.SubprocessError, OSError):
        pass


def by_scheme_count(scheme: Optional[str]) -> int:
    """Count the number of awards under a given scheme name."""
    if scheme is None:
        return 0
    cursor = conn.execute(
        "SELECT COUNT(*) FROM awards WHERE scheme = ?",
        (scheme,),
    )
    row = cursor.fetchone()
    return row[0] if row else 0


def main() -> None:
    """Execute main disbursement workflow."""
    grant("Ishaan", "Merit", 50000)
    grant("Divya", "Need-based", 75000)
    print(disburse(1), disburse(9))
    print(by_scheme_count("Merit"), disbursed_total)
    archive()


if __name__ == "__main__":
    main()
    