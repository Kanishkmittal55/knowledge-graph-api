# Chunks CRUD API - Core Concepts
Chunks = Small pieces of text/data extracted from documents for semantic search and knowledge graphs.

# Main Operations
1. get_chunks - Retrieve chunks
    - Filters by workspace, document, data type
    - Optional vector similarity search using embeddings
    - Populates workspace/document details
    - Supports pagination

2. add_chunks - Insert new chunks
    - Generates embeddings for each chunk (text or stringified objects)
    - Bulk inserts into database
    - Returns created chunks without embeddings

3. process_chunks - Auto-process uploaded files
    - Structured (CSV/JSON): Each row becomes a chunk (object type)
    - Unstructured (PDF/TXT): Split text into manageable pieces (string type)
    - Generates embeddings
    - Updates document status on errors

4. assign_chunks_to_workspace - Link chunks to workspace
    - Adds workspace to chunk's workspaces array
    - Tracks: assigned, already_assigned, not_found

5. unassign_chunks_from_workspace - Remove from workspace
    - Uses transaction to ensure consistency
    - Removes chunk from nodes/triples that reference it
    - Removes workspace from chunk

6. update_chunk - Modify tags/metadata
    - Updates workspace-specific fields: tags.{workspace_id}, user_metadata.{workspace_id}

7. delete_chunk - Permanent removal
    - Uses transaction
    - Removes from all nodes/triples
    - Deletes chunk document

## Key Data Flow
Upload File → process_chunks() 
  → create_structured/unstructured_chunks() 
  → add_chunks() (generates embeddings)
  → Chunks stored in DB

## Important Notes
Embeddings: Vector representations for semantic search (not returned by default for performance)
Transactions: Used for operations affecting multiple collections (delete, unassign)
Workspace-scoped: Tags/metadata stored per workspace: {workspace_id: [values]}

This is the data layer that feeds knowledge graphs and semantic search.