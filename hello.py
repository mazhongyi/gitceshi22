def summarize_numbers(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count if count else 0
    return {
        "total": total,
        "count": count,
        "average": average,
    }


if __name__ == "__main__":
    sample = [3, 5, 8, 13]
    result = summarize_numbers(sample)
    print("sample:", sample)
    print("summary:", result)
