# Schema CRUD API
Schemas = Define the structure of knowledge graphs (entity types, relationship types, and their allowed properties).

# Core Operations
1. delete_schema - Conditional deletion with safety check
    - Checks if schema is used by any graphs
    - Returns False if graphs exist (prevents orphaning graphs)
    - Returns True and deletes if no graphs use it

## Why Only Delete?
Schema CRUD is minimal because:
Create/Update likely happens through different endpoints (not shown in this file)
Read operations are handled by graph endpoints (schemas are fetched when retrieving graphs via $lookup)
Delete is critical because it requires validation - can't delete if graphs depend on it
This is a safety-focused operation preventing data integrity issues.