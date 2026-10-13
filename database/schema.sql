-- ============================================
-- SMART EXAM MONITOR — DATABASE SCHEMA
-- ============================================

-- Table 1: Candidates (FR1 — Registration)
CREATE TABLE IF NOT EXISTS candidates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    roll_number TEXT UNIQUE NOT NULL,
    name TEXT NOT NULL,
    seat_number TEXT NOT NULL,
    password_hash TEXT NOT NULL,
    photo_path TEXT NOT NULL,
    face_encoding BLOB,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Table 2: Sessions (FR3 — Session Lifecycle)
CREATE TABLE IF NOT EXISTS sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    candidate_id INTEGER NOT NULL,
    exam_id TEXT NOT NULL,
    start_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    end_time DATETIME,
    end_reason TEXT,
    status TEXT DEFAULT 'active',
    FOREIGN KEY (candidate_id) REFERENCES candidates(id)
);

-- Table 3: Events (FR4 — Event Logging)
CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id INTEGER NOT NULL,
    candidate_id INTEGER NOT NULL,
    event_type TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    confidence REAL,
    metadata TEXT,
    reviewed INTEGER DEFAULT 0,
    FOREIGN KEY (session_id) REFERENCES sessions(id),
    FOREIGN KEY (candidate_id) REFERENCES candidates(id)
);

-- Table 4: Integrity Reports (FR5 — Reports)
CREATE TABLE IF NOT EXISTS integrity_reports (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id INTEGER NOT NULL,
    candidate_id INTEGER NOT NULL,
    total_events INTEGER,
    integrity_score REAL,
    flag TEXT,
    generated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (session_id) REFERENCES sessions(id),
    FOREIGN KEY (candidate_id) REFERENCES candidates(id)
);

-- Indexes for performance
CREATE INDEX IF NOT EXISTS idx_events_session ON events(session_id);
CREATE INDEX IF NOT EXISTS idx_events_candidate ON events(candidate_id);
CREATE INDEX IF NOT EXISTS idx_events_type ON events(event_type);
CREATE INDEX IF NOT EXISTS idx_sessions_status ON sessions(status);
CREATE INDEX IF NOT EXISTS idx_sessions_candidate ON sessions(candidate_id);