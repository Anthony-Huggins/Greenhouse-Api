CREATE TABLE IF NOT EXISTS species (
    id                      INTEGER PRIMARY KEY AUTOINCREMENT,
    name                    TEXT NOT NULL,
    common_name             TEXT,
    sunlight_target         INTEGER NOT NULL,
    watering_interval_target INTEGER NOT NULL,
    created_at              DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at              DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TRIGGER update_species_updated_at
AFTER UPDATE ON species
FOR EACH ROW
BEGIN
    UPDATE species 
    SET updated_at = CURRENT_TIMESTAMP 
    WHERE id = OLD.id;
END;

CREATE TABLE IF NOT EXISTS plants (
    id                      INTEGER PRIMARY KEY AUTOINCREMENT,
    species_id              INTEGER REFERENCES greenhouses(id)
    nickname                TEXT NOT NULL,
    pot_size                INTEGER NOT NULL,
    acquisiton_date         DATETIME NOT NULL,
    health_status           TEXT NOT NULL CHECK (health_status IN ('thriving', 'stable', 'struggling', 'dormant', 'dead')),
    created_at              DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at              DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TRIGGER update_plants_updated_at
AFTER UPDATE ON plants
FOR EACH ROW
BEGIN
    UPDATE plants 
    SET updated_at = CURRENT_TIMESTAMP 
    WHERE id = OLD.id;
END;

CREATE TABLE IF NOT EXISTS greenhouses (
    id                      INTEGER PRIMARY KEY AUTOINCREMENT,
    name                    TEXT NOT NULL,
    num_rows                INTEGER NOT NULL,
    locations_per_row       INTEGER NOT NULL,
    created_at              DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at              DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TRIGGER update_greenhouses_updated_at
AFTER UPDATE ON greenhouses
FOR EACH ROW
BEGIN
    UPDATE greenhouses 
    SET updated_at = CURRENT_TIMESTAMP 
    WHERE id = OLD.id;
END;

CREATE TABLE IF NOT EXISTS locations (
    id              INTEGER PRIMARY KEY,
    greenhouse_id   INTEGER REFERENCES greenhouses(id),
    plant_id        INTEGER REFERENCES plants(id),
    row_number      INTEGER NOT NULL,
    spot_number     INTEGER NOT NULL,
    created_at              DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at              DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TRIGGER update_locations_updated_at
AFTER UPDATE ON locations
FOR EACH ROW
BEGIN
    UPDATE locations 
    SET updated_at = CURRENT_TIMESTAMP 
    WHERE id = OLD.id;
END;