# Coding Algo Notes

A simple Python Flask server that serves Markdown notes from the `notes/` folder.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the server:
   ```bash
   python app.py
   ```

3. Open your browser to `http://localhost:5000`

## Structure

- `notes/`: Folder containing all Markdown files (supports subfolders)
- `app.py`: Flask server
- `requirements.txt`: Python dependencies

## Adding Notes

Place your `.md` files in the `notes/` directory. Subfolders are supported. The server will automatically list all files on the index page.

Example:
```
notes/
├── dijkstra.md
├── graphs/
│   ├── bfs.md
│   └── dfs.md
└── sorting/
    └── quicksort.md
```

## Features

- Automatic listing of all Markdown files
- Recursive folder support
- Clean HTML rendering with syntax highlighting
- Navigation back to index

## Deployment

Deploy to any Python-supporting platform like Vercel, Heroku, or Railway.