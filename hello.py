def summarize_numbers(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count if count else 0
    minimum = min(numbers) if numbers else None
    maximum = max(numbers) if numbers else None
    return {
        "total": total,
        "count": count,
        "average": average,
        "minimum": minimum,
        "maximum": maximum,
    }


if __name__ == "__main__":
    print("second commit demo")
    sample = [3, 5, 8, 13]
    result = summarize_numbers(sample)
    print("sample:", sample)
    print("summary:", result)
