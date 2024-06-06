#!/bin/bash

# Run migrations
alembic upgrade b38cdb8e0489

# Start the application
exec "$@"
