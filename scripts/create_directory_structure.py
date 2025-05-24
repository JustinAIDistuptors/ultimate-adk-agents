#!/usr/bin/env python3
"""
Create the complete directory structure for Ultimate ADK Agents project.
Following Google ADK 1.0+ best practices and enterprise patterns.
"""

import os
from pathlib import Path

# Get the project root directory
PROJECT_ROOT = Path(__file__).parent.parent.absolute()

# Define the complete directory structure
DIRECTORY_STRUCTURE = [
    # ADK Configuration
    ".adk",
    ".adk/config",
    
    # Source Code
    "src",
    "src/agents",
    "src/agents/base",
    "src/agents/coding",
    "src/agents/orchestration",
    "src/agents/specialized",
    
    # Prompts and Templates
    "prompts",
    "prompts/system_prompts",
    "prompts/cursorrules_templates",
    "prompts/prompt_patterns",
    
    # Tools and Utilities
    "tools",
    "tools/diagnostic",
    "tools/observability",
    "tools/security",
    "tools/data_management",
    "tools/deployment",
    
    # Testing
    "tests",
    "tests/unit",
    "tests/unit/agent_tests",
    "tests/unit/tool_tests",
    "tests/unit/integration_tests",
    "tests/benchmarks",
    "tests/security",
    "tests/e2e",
    
    # Infrastructure
    "infrastructure",
    "infrastructure/docker",
    "infrastructure/kubernetes",
    "infrastructure/terraform",
    "infrastructure/helm",
    "infrastructure/helm/templates",
    
    # Monitoring
    "monitoring",
    "monitoring/dashboards",
    "monitoring/alerts",
    "monitoring/logs",
    
    # GitHub
    ".github",
    ".github/workflows",
    ".github/templates",
    
    # Documentation
    "docs",
    "docs/setup",
    "docs/architecture",
    "docs/api",
    "docs/best_practices",
    "docs/compliance",
    
    # Configuration
    "config",
    "config/production",
    "config/development",
    "config/local",
    
    # Scripts
    "scripts",
    "scripts/setup",
    "scripts/deployment",
    "scripts/maintenance",
    "scripts/monitoring",
    
    # Data
    "data",
    "data/vector_stores",
    "data/vector_stores/code_embeddings",
    "data/vector_stores/documentation_embeddings",
    "data/vector_stores/best_practices_embeddings",
    "data/training_data",
    "data/training_data/code_examples",
    "data/training_data/review_examples",
    "data/training_data/test_cases",
    "data/benchmarks",
    "data/benchmarks/gaia_dataset",
    "data/benchmarks/swe_bench_data",
    "data/benchmarks/performance_baselines",
    
    # Requirements
    "requirements",
]

def create_directory_structure():
    """Create all directories for the project."""
    created_dirs = []
    
    for dir_path in DIRECTORY_STRUCTURE:
        full_path = PROJECT_ROOT / dir_path
        if not full_path.exists():
            full_path.mkdir(parents=True, exist_ok=True)
            created_dirs.append(dir_path)
            print(f"[+] Created: {dir_path}")
        else:
            print(f"[=] Exists: {dir_path}")
    
    return created_dirs

def create_gitkeep_files():
    """Create .gitkeep files in empty directories to ensure they're tracked by git."""
    for dir_path in DIRECTORY_STRUCTURE:
        full_path = PROJECT_ROOT / dir_path
        gitkeep_path = full_path / ".gitkeep"
        
        # Only create .gitkeep if directory is empty
        if full_path.exists() and not any(full_path.iterdir()):
            gitkeep_path.touch()
            print(f"[.gitkeep] Created in: {dir_path}")

if __name__ == "__main__":
    print("[*] Creating Ultimate ADK Agents directory structure...")
    print(f"[*] Project root: {PROJECT_ROOT}")
    print("-" * 60)
    
    # Create directories
    created = create_directory_structure()
    
    print("-" * 60)
    print(f"[*] Created {len(created)} new directories")
    
    # Add .gitkeep files
    print("-" * 60)
    print("[*] Adding .gitkeep files to empty directories...")
    create_gitkeep_files()
    
    print("-" * 60)
    print("[*] Directory structure setup complete!")
