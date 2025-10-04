# Documents CRUD API
Documents = Files uploaded to S3 (PDF, TXT, CSV, JSON) that get processed into chunks.

# Core Operations
1. get_documents / get_document - Retrieve with workspace details populated
2. update_document - Modify workspace-specific metadata/tags
3. delete_document - Full cleanup (uses transaction)
    - Deletes document from MongoDB
    - Deletes all associated chunks
    - Removes chunks from nodes/triples
    - Deletes file from S3

4. process_document - Main processing pipeline
    - Fetches file from S3
    - Updates status to "processing"
    - Calls process_chunks() to extract and embed
    - Updates status to "processed" or "failed"

5. assign/unassign_documents_to_workspace
    - Also updates all related chunks
    - Unassign uses transaction to remove from nodes/triples