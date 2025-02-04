# pet_adoption_and_care
# Pet Care and Adoption API

This RESTful API provides endpoints for managing pets, users, and adoptions. It is built using Flask (Python) and stores data in a JSON file (`data.json`).

## Getting Started

### Prerequisites

*   Python 3.x
*   Flask: `pip install Flask`

### Running the API

1.  Clone the repository (or download the files).
2.  Ensure `data.json` exists in the same directory.  Populate `data.json` with initial data if needed (see the example structure below).
3.  Navigate to the project directory in your terminal.
4.  Run the Flask app: `python app.py`

The API will be accessible at `http://127.0.0.1:5000/` (or the address and port shown in your terminal output).

## API Endpoints

The following endpoints are available:

### Pets

*   **GET /pets:** Retrieves a list of all pets.
*   **GET /pets/<int:pet_id>:** Retrieves a specific pet by ID.
*   **POST /pets:** Adds a new pet.
*   **PUT /pets/<int:pet_id>:** Updates an existing pet.
*   **DELETE /pets/<int:pet_id>:** Deletes a specific pet by ID.
*   **GET /pets/available:** Retrieves a list of all available pets.
*   **GET /pets/species/<string:species>:** Retrieves a list of pets by species.

### Users

*   **GET /users:** Retrieves a list of all users.
*   **GET /users/<int:user_id>:** Retrieves a specific user by ID.
*   **POST /users:** Adds a new user.
*   **PUT /users/<int:user_id>:** Updates an existing user.
*   **DELETE /users/<int:user_id>:** Deletes a specific user by ID.
*   **GET /users/<int:user_id>/pets:** Retrieves a list of pets adopted by a specific user.

### Adoptions

*   **GET /adoptions:** Retrieves a list of all adoptions.
*   **GET /adoptions/<int:adoption_id>:** Retrieves a specific adoption by ID.
*   **POST /adoptions:** Creates a new adoption application.
*   **PUT /adoptions/<int:adoption_id>:** Updates an existing adoption.
*   **DELETE /adoptions/<int:adoption_id>:** Deletes a specific adoption by ID.
*   **GET /pets/<int:pet_id>/applications:** Retrieves a list of applications for a specific pet.
*   **GET /users/<int:user_id>/applications:** Retrieves a list of applications by a specific user.
*   **POST /pets/<int:pet_id>/apply:** Allows a user to apply for a pet.
*   **PUT /adoptions/<int:adoption_id>/approve:** Approves a specific adoption.
*   **PUT /adoptions/<int:adoption_id>/reject:** Rejects a specific adoption.
*   **GET /pets/<int:pet_id>/adopters:** Retrieves a list of users who applied for a specific pet.
*   **GET /adoptions/pending:** Retrieves a list of all pending adoptions.

## Data Structure (data.json)

```json
{
  "pets": [
    {
      "id": 1,
      "name": "Buddy",
      "species": "Dog",
      "breed": "Golden Retriever",
      "age": 3,
      "available": true,
      "description": "Friendly and playful dog."
    },
    
  ],
  "users": [
    {
      "id": 1,
      "name": "P1",
      "email": "p1@example.com",
      "address": "123 any St"
    },

  ],
  "adoptions": [
    {
      "id": 1,
      "pet_id": 3,
      "user_id": 1,
      "application_date": "2024-07-26",
      "status": "approved" 
    },

  ]
}
