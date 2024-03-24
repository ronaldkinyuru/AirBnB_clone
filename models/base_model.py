import uuid

class BaseModel:
    def __init__(self):
        """ Generate a unique ID and convert it to a string """
        self.id = str(uuid.uuid4())

# Example usage
if __name__ == "__main__":
    """ Create a new instance of BaseModel """
    model = BaseModel()

    # Print the generated ID
    print("Generated ID:", model.id)