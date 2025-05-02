#!/bin/bash

# Check if at least two arguments are given
if [ $# -lt 2 ]; then
  echo "Usage: $0 <project_name> -[p|j|g|s]"
  echo "  -py: Python file"
  echo "  -ja: Java file"
  echo "  -go: Go file"
  echo "  -js: JavaScript file"
  exit 1
fi

project_name=$1
flag=$2

# Create the project directory
mkdir -p "$project_name"
cd "$project_name"

# Function to open file in VS Code
open_file() {
  echo "Opening $1 in VS Code..."
  code "$1"
}

case $flag in
-py)
  # Create Python file
  cat >"main.py" <<EOF
#!/usr/bin/env python3

"""
source: 
problem: 
type: 
site: 
submission: 
"""

def main():
    sol = Solution()

    print()
    pass

if __name__ == "__main__":
    main()
EOF
  chmod +x "main.py"
  open_file "main.py"
  ;;
-ja)
  # Create Java file
  cat >"main.java" <<EOF
/**
 * source: 
 * problem: 
 * type: 
 * site: 
 * submission: 
 */

public class go {
    public static void main(String[] args) {
        
    }
}
EOF
  open_file "main.java"
  ;;
-go)
  # Create Go file
  cat >"main.go" <<EOF
package main

/**
 * source: 
 * problem: 
 * type: 
 * site: 
 * submission: 
 */

import (
    "fmt"
)

func main() {
    
}
EOF
  open_file "main.go"
  ;;
-js)
  # Create JavaScript file
  cat >"index.js" <<EOF
#!/usr/bin/env node
/**
 * source: 
 * problem: 
 * type: 
 * site: 
 * submission: 
 */

function main() {
    
}

main();
EOF
  chmod +x "index.js"
  open_file "index.js"
  ;;
*)
  echo "Invalid flag. Use -py for Python, -ja for Java, -go for Go, or -js for JavaScript."
  exit 1
  ;;
esac

echo "Project '$project_name' created successfully with file extension specified by flag '$flag'"
