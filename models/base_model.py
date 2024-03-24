import uuid
from datetime import datetime

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())  # Generate unique ID
        self.created_at = datetime.now()  # Set created_at to current datetime
        self.updated_at = self.created_at  # Set updated_at to current datetime

    def save(self):
        self.updated_at = datetime.now()  # Update updated_at with current datetime

    def to_dict(self):
        obj_dict = self.__dict__.copy()  # Get dictionary representation of instance attributes
        obj_dict['__class__'] = self.__class__.__name__  # Add class name to dictionary
        obj_dict['created_at'] = self.created_at.isoformat()  # Convert created_at to ISO format string
        obj_dict['updated_at'] = self.updated_at.isoformat()  # Convert updated_at to ISO format string
        return obj_dict

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

# Example usage
if __name__ == "__main__":
    # Create an instance of BaseModel
    base_model = BaseModel()

    # Print the object as string
    print(str(base_model))

    # Save the object (update updated_at)
    base_model.save()

    # Convert object to dictionary
    base_model_dict = base_model.to_dict()
    print(base_model_dict)
