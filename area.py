def calculate_area(length, width):
    """Calculate the area of a rectangle."""
    return length * width


def main():
    """Main function to demonstrate calculate_area."""
    length = 5
    width = 10
    area = calculate_area(length, width)
    print(f"The area of the rectangle is: {area}")


if __name__ == "__main__":
    main()