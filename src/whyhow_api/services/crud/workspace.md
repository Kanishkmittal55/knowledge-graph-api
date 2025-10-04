# Workspace CRUD API
Workspaces = Top-level containers organizing all user data (documents, chunks, graphs, schemas).

# Core Operation
1. delete_workspace - Complete teardown (uses transaction)
    - Deletion order:
    - Graphs → calls delete_graphs() which cascades to nodes, triples, queries
    - Schemas → deletes all schemas in workspace
    - Documents → removes workspace reference + workspace-specific tags/metadata
    - Chunks → removes workspace reference + workspace-specific tags/metadata
    - Workspace → deletes the workspace document itself

## Why only delete?
Same reason as schemas - Create/Read/Update operations likely exist elsewhere:
- Create: Handled by dedicated workspace creation endpoint
- Read: Handled by workspace list/get endpoints (not in this file)
- Update: Handled by workspace update endpoints (not in this file) 

## This file focuses on the most complex operation - safe deletion with full cascade across all dependent collections using a transaction.