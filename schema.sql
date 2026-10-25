CREATE TABLE applications (
    application_id int GENERATED ALWAYS AS IDENTITY primary key,
    company text NOT NULL,
    role text NOT NULL,
    location text NOT NULL,
    url text unique NOT NULL,
    source text NOT NULL CHECK (source IN ('manual','import','agent')) DEFAULT 'manual' ,
    status text NOT NULL CHECK (status IN ('saved','applied','interviewing','offer','rejected','withdrawn')) DEFAULT 'saved',
    deadline date NULL,
    applied_at timestamptz NULL,
    notes text NULL,
    created_at timestamptz NOT NULL DEFAULT now(),
    updated_at timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE status_events (
    event_id int GENERATED ALWAYS AS IDENTITY primary key,
    application_id int NOT NULL references applications(application_id),
    from_status text NULL,
    to_status text NOT NULL CHECK (to_status IN ('saved','applied','interviewing','offer','rejected','withdrawn')),
    note text NULL,
    changed_at timestamptz NOT NULL DEFAULT now()
);

CREATE INDEX idx_applications_status ON applications (status);
CREATE INDEX idx_applications_deadline ON applications (deadline);
CREATE INDEX idx_applications_applied_at ON applications (applied_at);
CREATE INDEX idx_status_events_application_id ON status_events (application_id);
CREATE INDEX idx_status_events_changed_at ON status_events (changed_at);