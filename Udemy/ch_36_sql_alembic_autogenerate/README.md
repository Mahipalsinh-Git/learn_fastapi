uv run alembic init alembic
uv run alembic upgrade head
uv run alembic revision --autogenerate -m "create user table"

# Alembic Commands
1. alembic init [directory]
    Initialize a new Alembic environment in the specified directory.
    This Sets up the configuration files and script directory needed for migrations.

2. alembic revision -m "message" [--autogenerate]
    Create a new migration script.
        Use -m to add a message describing the migration.
        Add -autogenerate to automatically generate migration code based on model and database differences.

3. alembic upgrade [revision]
    Apply migration up to the specified revision (eg. head for the latest). This updated the database schema to the desired state.

4. alembic upgrade +2
    This command upgrades your databaes schema forward by two migration steps from the current revision, applying the next two migrations
    in sequence

5. alembic downgrade [revision]
    Revert migration down to the specified revision, effectively rolling back schema changes.

6. alembic downgrade -1
    This command downgrades (rolls back) your database schema by one migration step from the current revision,
    reverting the most recent migration

7. alembic current
    Display the current revision(s) applied to the database

8. alembic history
    Show the list of all migragtion scripts in chronoligical order.

9. alembic list_templates
    List available migration environment templates for initializing new projects.
