for i in range(97, 97+26):
    print(f"""
FUNCTION PRINT_{chr(i).upper()}_LOWER
    MOVE -1
    SET {i}
    PRINT
    """)