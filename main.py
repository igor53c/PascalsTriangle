def get_pascals_triangle_row(row_number: int) -> list:
    if row_number == 0:
        return [1]
    elif row_number == 1:
        return [1, 1]
    else:
        previous_row = get_pascals_triangle_row(row_number - 1)
        current_row = [1]
        for i in range(len(previous_row) - 1):
            current_row.append(previous_row[i] + previous_row[i + 1])
        current_row.append(1)
        return current_row


assert get_pascals_triangle_row(0) == [1], "Test case 1 failed"
assert get_pascals_triangle_row(1) == [1, 1], "Test case 2 failed"
assert get_pascals_triangle_row(2) == [1, 2, 1], "Test case 3 failed"
assert get_pascals_triangle_row(3) == [1, 3, 3, 1], "Test case 4 failed"
assert get_pascals_triangle_row(12) == [1, 12, 66, 220, 495, 792, 924, 792, 495, 220, 66, 12, 1], "Test case 4 failed"

print("All test cases passed successfully!")
