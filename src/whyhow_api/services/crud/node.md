# Nodes CRUD API
Nodes = Entities in the knowledge graph (people, places, organizations, concepts) with properties and chunk references.

# Core Operations
1. update_node - Modify node with cascade (uses transaction)
    - Updates node properties (name, type, properties)
    - Cascades: Re-embeds all triples connected to this node
    - Why: Changing node details changes triple semantics, embeddings must reflect this

2. delete_node - Remove node and relationships (uses transaction)
    - Deletes node document
    - Deletes all triples where node is head OR tail
    - Prevents orphaned relationships

3. get_node_chunks - Fetch chunks referenced by node
    - Joins: node → graph → workspace → chunks → document
    - Returns workspace-scoped chunk details

4. get_nodes_by_ids - Batch fetch nodes by IDs