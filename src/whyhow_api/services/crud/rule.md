# Rules CRUD API
Rules = Transformation logic applied to triples during knowledge graph construction (e.g., merge duplicate entities, normalize names).
Core Operations

1. create_rule - Add new rule to workspace
2. get_workspace_rules - Fetch all rules for a workspace
3. get_graph_rules - Fetch rules embedded in a specific graph
    - Rules are stored inside graph documents, not just referenced
4. delete_rule - Remove rule from database
5. apply_rules_to_triples - Transform triples using rules
    - Iterates through rules and applies transformations
    - Currently supports: MergeNodesRule (consolidate duplicate entities)
6. merge_nodes_transform - Example rule implementation

    - Renames node if it matches from_node_names and node_type
    - Updates both head and tail nodes in triples

# Why Rules Matter
Rules allow users to define transformations applied during graph building:

- "Merge 'USA', 'United States', 'U.S.A.' into one node"
- "Normalize company names"
- Applied before triples are persisted