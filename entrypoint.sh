#!/bin/bash
# exit immediately if a command exits with a non-zero status
set -e


# Run migrations
alembic upgrade head

# Start the application
exec "$@"
