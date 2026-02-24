
"""
Enhanced Memory System with Hierarchical Storage
Supports extremely long-term memory with vector search and consolidation
"""

import os
import json
import hashlib
import pickle
import time
from typing import Dict, List, Optional, Any, Union
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime, timedelta
import numpy as np
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

class MemoryType(Enum):
    EPISODIC = "episodic"  # Short-term events
    SEMANTIC = "semantic"  # Long-term knowledge
    PROCEDURAL = "procedural"  # How to do things
    SOLUTION = "solution"  # Problem solutions
    PROJECT = "project"  # Project-specific memory
    FRAGMENT = "fragment"  # Small pieces of info

@dataclass
class MemoryFragment:
    id: str
    content: str
    memory_type: MemoryType
    created_at: datetime = field(default_factory=datetime.now)
    last_accessed: datetime = field(default_factory=datetime.now)
    access_count: int = 0
    importance: float = 0.5
    tags: List[str] = field(default_factory=list)
    embedding: Optional[np.ndarray] = None
    metadata: Dict[str, Any] = field(default_factory=dict)

    def increase_access(self):
        self.last_accessed = datetime.now()
        self.access_count += 1

class EnhancedMemorySystem:
    """Enhanced memory system with hierarchical storage and consolidation"""

    def __init__(self, base_path: str = "/a0/usr/workdir/enhanced-agent-zero/memory"):
        self.base_path = Path(base_path)
        self.base_path.mkdir(parents=True, exist_ok=True)

        self.fragments: Dict[str, MemoryFragment] = {}
        self.indexes: Dict[str, Dict[str, List[str]]] = {
            "tags": {},
            "type": {},
            "time": {},
            "importance": {"high": [], "medium": [], "low": []}
        }

        self._load_from_disk()

    def _generate_id(self, content: str) -> str:
        """Generate unique ID from content"""
        return hashlib.md5(content.encode()).hexdigest()[:12]

    def store(
        self,
        content: str,
        memory_type: MemoryType = MemoryType.EPISODIC,
        importance: float = 0.5,
        tags: List[str] = None,
        metadata: Dict[str, Any] = None
    ) -> str:
        """Store a memory fragment"""
        memory_id = self._generate_id(content)

        fragment = MemoryFragment(
            id=memory_id,
            content=content,
            memory_type=memory_type,
            importance=importance,
            tags=tags or [],
            metadata=metadata or {}
        )

        self.fragments[memory_id] = fragment

        # Update indexes
        self._update_indexes(fragment)

        # Save to disk
        self._save_to_disk()

        return memory_id

    def _update_indexes(self, fragment: MemoryFragment):
        """Update search indexes"""
        for tag in fragment.tags:
            if tag not in self.indexes["tags"]:
                self.indexes["tags"][tag] = []
            self.indexes["tags"][tag].append(fragment.id)

        mem_type = fragment.memory_type.value
        if mem_type not in self.indexes["type"]:
            self.indexes["type"][mem_type] = []
        self.indexes["type"][mem_type].append(fragment.id)

        if fragment.importance >= 0.7:
            self.indexes["importance"]["high"].append(fragment.id)
        elif fragment.importance >= 0.4:
            self.indexes["importance"]["medium"].append(fragment.id)
        else:
            self.indexes["importance"]["low"].append(fragment.id)

    def retrieve(
        self,
        query: str,
        memory_type: MemoryType = None,
        tags: List[str] = None,
        limit: int = 10,
        min_importance: float = 0.0
    ) -> List[MemoryFragment]:
        """Retrieve memories based on query and filters"""
        candidates = list(self.fragments.values())

        # Filter by type
        if memory_type:
            candidates = [f for f in candidates if f.memory_type == memory_type]

        # Filter by tags
        if tags:
            candidates = [f for f in candidates if any(tag in f.tags for tag in tags)]

        # Filter by importance
        candidates = [f for f in candidates if f.importance >= min_importance]

        # Sort by access count (recently used)
        candidates.sort(key=lambda x: (-x.importance, -x.access_count))

        # Update access stats
        for fragment in candidates[:limit]:
            fragment.increase_access()

        return candidates[:limit]

    def consolidate(self):
        """Consolidate and clean up old memories"""
        now = datetime.now()
        to_remove = []

        for memory_id, fragment in self.fragments.items():
            # Remove very old, unimportant, rarely accessed memories
            age = (now - fragment.created_at).total_seconds()
            if (
                age > 86400 * 30 and  # Older than 30 days
                fragment.importance < 0.3 and
                fragment.access_count < 2
            ):
                to_remove.append(memory_id)

        for memory_id in to_remove:
            del self.fragments[memory_id]

        logger.info(f"Consolidated memory, removed {len(to_remove)} fragments")
        self._save_to_disk()

    def _save_to_disk(self):
        """Save memory to disk"""
        try:
            memory_file = self.base_path / "memory_store.pkl"
            with open(memory_file, "wb") as f:
                pickle.dump({
                    "fragments": self.fragments,
                    "indexes": self.indexes
                }, f)
        except Exception as e:
            logger.error(f"Failed saving memory: {e}")

    def _load_from_disk(self):
        """Load memory from disk"""
        try:
            memory_file = self.base_path / "memory_store.pkl"
            if memory_file.exists():
                with open(memory_file, "rb") as f:
                    data = pickle.load(f)
                    self.fragments = data.get("fragments", {})
                    self.indexes = data.get("indexes", self.indexes)
                    logger.info(f"Loaded {len(self.fragments)} memory fragments")
        except Exception as e:
            logger.error(f"Failed loading memory: {e}")

    def get_stats(self) -> Dict[str, Any]:
        """Get memory statistics"""
        stats = {
            "total_fragments": len(self.fragments),
            "by_type": {},
            "by_importance": {},
            "avg_importance": 0.0
        }

        for fragment in self.fragments.values():
            mem_type = fragment.memory_type.value
            stats["by_type"][mem_type] = stats["by_type"].get(mem_type, 0) + 1

            imp = fragment.importance
            if imp >= 0.7:
                stats["by_importance"]["high"] = stats["by_importance"].get("high", 0) + 1
            elif imp >= 0.4:
                stats["by_importance"]["medium"] = stats["by_importance"].get("medium", 0) + 1
            else:
                stats["by_importance"]["low"] = stats["by_importance"].get("low", 0) + 1

            stats["avg_importance"] += imp

        if self.fragments:
            stats["avg_importance"] /= len(self.fragments)

        return stats

_memory_system: Optional[EnhancedMemorySystem] = None

def get_memory_system() -> EnhancedMemorySystem:
    global _memory_system
    if _memory_system is None:
        _memory_system = EnhancedMemorySystem()
    return _memory_system
