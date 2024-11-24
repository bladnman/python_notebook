#!/bin/bash

initial_project_name="initial_project_name"

# Define the new project name as 
# the name of the current directory
new_project_name=$(basename "$PWD")

# Remove any existing git repository
rm -rf .git

# Check if pyproject.toml contains "initial_project_name"
if ! grep -q "$initial_project_name" pyproject.toml; then
    echo
    echo "It looks like this script has already been run,"
    echo "pyproject.toml does not contain '$initial_project_name'."
    echo "Exiting..."
    echo
    exit 1
fi

# Check if source directory exists
if [ ! -d "$initial_project_name" ]; then
    echo "Error: Source directory '$initial_project_name' does not exist."
    echo "Exiting..."
    exit 1
fi

# rename the main module folder
if ! mv "$initial_project_name" "$new_project_name"; then
    echo "Error: Failed to rename directory from '$initial_project_name' to '$new_project_name'"
    exit 1
fi

# Initialize a new git repository
git init

# Update all files with the new name
# Look through all files in the project and replace the old name with the new name
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS version
    find . -type f -not -path '*/\.*' -not -path './node_modules/*' \
        -exec sed -i '' "s/$initial_project_name/$new_project_name/g" {} +
else
    # Linux version
    find . -type f -not -path '*/\.*' -not -path './node_modules/*' \
        -exec sed -i "s/$initial_project_name/$new_project_name/g" {} +
fi

# Start fresh
# Initialize a new git repository
rm -rf .git
git init

# INSTALL
yarn install

# Make initial commit
git add .
git commit -m "Initial commit with custom template and updated packages"

# Provide feedback that the script is done
echo "Project $new_project_name has been set up and is ready to use!"
