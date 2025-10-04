# Graph CRUD API
Graphs = Knowledge graph structures with nodes (entities) and triples (relationships between entities).

# Core Operations
1. delete_graphs - Delete graph and all components (uses transaction)
    - Deletes triples (relationships)
    - Deletes nodes (entities)
    - Deletes queries (graph queries)
    - Deletes graph document

2. get_graph / list_all_graphs - Retrieve with schema and workspace populated
3. list_nodes - Get all entities in graph with pagination
4. list_triples - Get all relationships with head/tail nodes populated
    - Excludes "Contains" type (internal relationship)
    - Joins with node collection to get full node details

5. list_relations - Get distinct relationship types in graph
6. get_graph_chunks - Get all chunks referenced by nodes/triples in graph
    - Collects chunk IDs from all nodes and triples
    - Deduplicates and fetches chunk details