# Filename: main.py (or any file of your choice)
# -----------------------------------------------------------------------------
# DISCLAIMER:
# This code is an EXAMPLE solution for reference/study purposes ONLY.
# Submitting it as your own may violate assignment rules against plagiarism
# or AI-generated solutions. Use it ethically and responsibly.
# -----------------------------------------------------------------------------

def get_f_tables(f_tables):
    """
    Level 1
    Returns a list of table IDs (or entire objects) that are currently free.
    """
    f_tables = []
    def taken_tables():
    
        if not taken_tables["occupied"]:  # occupied == False
            f_tables.append(taken_tables["table_id"])
    return f_tables
    """
    Level 2
    Returns the first table ID that can seat 'party_size' and is free,
    or None if none found.
    """
def get_full_tables(full_tables):

    for taken_table in full_tables:
        if not taken_table["occupied"] and full_tables["capacity"] >= party_size: # type: ignore
            return full_tables["table_id"]
    return None
# -----------------------------------------------------------------------------
# Example usage / testing:
if __name__ == "__main__":
    # Example data
    tables_data = [
        {"table_id": 1, "capacity": 2, "occupied": True, "neighbors": [2]},
        {"table_id": 2, "capacity": 4, "occupied": True,  "neighbors": [1, 3]},
        {"table_id": 3, "capacity": 2, "occupied": False, "neighbors": [2, 4]},
        {"table_id": 4, "capacity": 6, "occupied": False, "neighbors": [3]}
    ]

    print("LEVEL 1: Free Tables = 1,3,4", get_f_tables(tables_data))

   

    