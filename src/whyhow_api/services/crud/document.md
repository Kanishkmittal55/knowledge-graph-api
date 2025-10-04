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


# Added create documents for local integration with minio for local testing - 
## The Original Design (AWS Production)
    Frontend gets presigned URL (just generates credentials, no DB write)
    File uploaded directly to AWS S3 (bypasses backend entirely for performance)
    S3 automatically triggers Lambda/webhook when file lands
    Lambda creates MongoDB document record
    Lambda calls process endpoint
    Document appears in UI

## This design is common and sensible for production because:
Reduces backend load (uploads go straight to S3)
Scalable (Lambda handles spikes automatically)
Decoupled (backend doesn't block during uploads)
Event-driven architecture (standard AWS pattern)

## The Problem
Your team likely built this for AWS production but never implemented the local development equivalent. In production, S3 events would be configured. In local dev with MinIO, nobody set up bucket notifications, so the trigger never fires.
This is a common oversight - teams build for production infrastructure but forget to provide a dev-friendly alternative. The "proper" local setup would be:

## Configure MinIO bucket notifications
Create a webhook endpoint in your backend to receive them
Test the full event flow locally
But that's complex, so the pragmatic fix is what we did - just create the document record immediately since there's no event system in local dev.
Your instinct to question this is correct - it's poor developer experience to have this gap between production and local environments.