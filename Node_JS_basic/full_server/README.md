# full_server/full_server/README.md

# Full Server Project

This project is an Express server that serves student data from a CSV database file. It provides endpoints to retrieve a list of all students and to filter students by their major.

## Project Structure

```
full_server
├── controllers
│   ├── AppController.js
│   └── StudentsController.js
├── routes
│   └── index.js
├── utils
│   └── readDatabase.js
├── dev.js
├── server.js
├── .babelrc
├── package.json
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd full_server
   ```

2. Install the dependencies:
   ```
   npm install
   ```

## Usage

To start the server, run the following command:
```
npm run dev
```

The server will listen on port 1245.

## Endpoints

- `GET /` - Returns a welcome message.
- `GET /students` - Returns a list of all students grouped by their fields.
- `GET /students/:major` - Returns a list of students for the specified major (CS or SWE).

## Error Handling

- If the database cannot be loaded, a 500 status code will be returned with the message "Cannot load the database".
- If an invalid major is provided, a 500 status code will be returned with the message "Major parameter must be CS or SWE".