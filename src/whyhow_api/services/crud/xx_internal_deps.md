# API Dependencies Documentation

| API Module | Depends On | Purpose |
|------------|-----------|---------|
| **Workspaces** | Graphs CRUD (`delete_graphs`), Schemas, Documents, Chunks collections | Delete cascades to all workspace entities using transactions |
| **Documents** | Chunks CRUD, S3 (boto3), Base CRUD (`update_one`) | Process files, store in S3, manage chunk references |
| **Chunks** | LLM Client (OpenAI), Nodes/Triples, Documents, Text splitters (LangChain), File parsers (pypdf, pandas) | Generate embeddings, maintain graph integrity, parse files |
| **Graphs** | Nodes, Triples, Chunks, Schemas, Queries, Workspaces, Rules collections | Orchestrate knowledge graph structure with transformation rules |
| **Triples** | Nodes, Chunks, Graphs, LLM Client (OpenAI), Text utilities (`clean_text`) | Store relationships, generate embeddings |
| **Schemas** | Graphs collection | Validate no graphs use schema before deletion |
| **Tasks** | FastAPI BackgroundTasks, Task collection | Track async job status for long-running operations |
| **Rules** | Triples (Triple model), Base CRUD (`create_one`, `get_all`, `get_all_count`) | Define transformations applied during graph construction |
| **Nodes** | Triples CRUD (`update_triple_embeddings`), Chunks, Graphs, Workspaces, LLM Client (OpenAI), Base CRUD (`update_one`) | Store entities, cascade updates to connected triples |

## Dependencies Table

| API Module | Depends On | Purpose |
|------------|-----------|---------|
| **Workspaces** | Documents, Schemas, Graphs, Chunks, Nodes, Triples | Delete cascades to all workspace entities using transactions |
| **Documents** | Chunks CRUD (`process_chunks`, `perform_node_chunk_unassignment`, `perform_triple_chunk_unassignment`) | Process uploaded files into chunks, clean up chunk references |
| **Documents** | S3 (boto3) | Store and retrieve uploaded files |
| **Documents** | Base CRUD (`update_one`) | Update document status during processing |
| **Chunks** | LLM Client (OpenAI) | Generate embeddings for semantic search |
| **Chunks** | Nodes/Triples collections | Unassign chunks when deleting to maintain graph integrity |
| **Chunks** | Documents collection | Reference parent document for each chunk |
| **Chunks** | Text splitters (LangChain) | Split large text into manageable pieces |
| **Chunks** | File parsers (pypdf, pandas) | Read PDF, CSV, JSON files |
| **Graphs** | Nodes collection | Populate node details in triples, fetch nodes for graph |
| **Graphs** | Triples collection | Store relationships between nodes |
| **Graphs** | Chunks collection | Get chunks referenced by nodes/triples |
| **Graphs** | Schemas collection | Define entity types and relationship rules |
| **Graphs** | Queries collection | Store saved graph queries |
| **Graphs** | Workspaces collection | Associate graph with workspace |
| **Triples** | Nodes collection | Fetch head/tail node details for embedding |
| **Triples** | Chunks collection | Get chunks referenced by triple |
| **Triples** | Graphs collection | Associate triple with graph/workspace |
| **Triples** | LLM Client (OpenAI) | Generate embeddings for semantic triple search |
| **Triples** | Text utilities (`clean_text`) | Sanitize text for natural language conversion |
| **Schemas** | Graphs collection | Validate no graphs use schema before deletion |
| **Tasks** | FastAPI BackgroundTasks, Task collection | Track async job status for long-running operations |
| **Rules** | Triples (Triple model), Base CRUD (`create_one`, `get_all`, `get_all_count`) | Define transformations applied during graph construction |
| **Nodes** | Triples collection (`update_triple_embeddings`), Chunks, Graphs, Workspaces, LLM Client (OpenAI), Base CRUD (`update_one`) | Store entities, cascade updates to connected triples |
| **Workspaces** | Graphs CRUD (`delete_graphs`), Schemas, Documents, Chunks collections | Delete cascades to all workspace entities using transactions |

Notes on schema crud - 
- Schema dependency is inverse: Graphs depend on schemas, so schemas check graphs before allowing deletion.
- For schema - Create/Update likely happens through different endpoints (not shown in this file), only delete is there.

Notes on tasks crud - 
Tasks are infrastructure - they don't directly depend on other business logic, but other modules (Documents, Graphs) likely use tasks for async operations.

## Data Flow Hierarchy

| Level | Entity | Contains | Operations Cascade To |
|-------|--------|----------|----------------------|
| 1 | Workspace | Documents, Schemas, Graphs | Delete → deletes all documents and related entities |
| 2 | Documents | Chunks | Delete → deletes all chunks + S3 file |
| 3 | Chunks | Embeddings | Delete → removes from nodes/triples |
| 4 | Nodes/Triples | Chunk references | Delete → updates references |

**Note:** All multi-collection operations use MongoDB transactions for atomicity.