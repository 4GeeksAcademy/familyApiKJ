
# src/datastructure.py

from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = []  # Initialize an empty list for members
        # example list of members
        self._members.append({
            "first_name": "John",
            "last_name": self.last_name,
            "age": 33,
            "lucky_numbers":[7,13,22],
            "id": self._generateId()
        })
        self._members.append({
            "first_name": "Jane",
            "last_name": self.last_name,
            "age": 35 ,
            "lucky_numbers":[10, 14, 3],
            "id": self._generateId()
        })
        self._members.append({
            "first_name": "Jimmy",
            "last_name": self.last_name,
            "age": 5,
            "lucky_numbers":[1],
            "id": self._generateId()
        })

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        member["id"] = self._generateId()  # Generate ID for the new member
        self._members.append(member)

    def delete_member(self, id):
        for i, member in enumerate(self._members):
            if member["id"] == id:
                del self._members[i]  # Delete member with the given ID
                return True  # Member deleted
        return False  # Member not found

    def update_member(self, id, updated_data):
        for i, member in enumerate(self._members):
            if member["id"] == id:
                self._members[i].update(updated_data)  # Update member data
                return True  # Member updated
        return False  # Member not found

    def get_member(self, id):
        for member in self._members:
            if member["id"] == id:
                return member  # Return member with the given ID
        return None  # Member not found

    def get_all_members(self):
        return self._members  # Return all members in the family
