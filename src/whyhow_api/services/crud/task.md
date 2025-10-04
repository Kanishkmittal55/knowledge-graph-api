# Task CRUD API

Tasks = Background jobs tracked in the database for async operations (document processing, graph building, etc.).

# Core Operation
1. create_task - Start background job with tracking

## Flow:
- Creates task document with status "pending"
- Inserts into database to get task ID
- Adds actual work function to FastAPI BackgroundTasks queue
- Returns task document immediately (non-blocking)
- Background worker executes function later, updates task status

## Purpose: 
- Allows long-running operations (like document processing with embeddings) to run asynchronously without blocking API responses.