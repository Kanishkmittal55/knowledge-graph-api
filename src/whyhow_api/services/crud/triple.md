# Triples CRUD API
Triples = Relationships between two nodes in the knowledge graph (head_node → relation → tail_node).

# Core Operations
1. delete_triple - Simple deletion
    - Removes triple
    - Allows connected nodes to become orphaned (nodes remain)

2. get_triple_chunks - Get chunks referenced by a triple
    - Joins: triple → graph → workspace → chunks → document
    - Returns workspace-scoped chunk details

3. convert_triple_to_text - Natural language representation
    - Converts structured triple to readable sentence
    - Includes node properties and relation properties
    - Optionally includes chunk content
    - Example: "John which is a Person with age of 30 works_at Microsoft, a Company with industry of Technology"

4. embed_triples - Generate embeddings for semantic search
    - Converts triples to text using convert_triple_to_text
    - Batches embeddings (max 2048 per batch)
    - Uses OpenAI embedding model

5. update_triple_embeddings - Refresh embeddings (uses optional transaction)
    - Fetches triples with head/tail node details
    - Generates new embeddings
    - Bulk updates triple documents