-- ============================================================
-- LEJOMER — Reconstrucción de Imágenes
-- Esquema inicial de base de datos
-- Versión: 1.0
-- ============================================================

-- ============================================================
-- 1. TABLA DE USUARIOS
-- ============================================================

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);


-- ============================================================
-- 2. TABLA DE TRABAJOS DE PROCESAMIENTO
-- ============================================================

CREATE TABLE processing_jobs (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    status VARCHAR(50) NOT NULL,
    total_images INTEGER NOT NULL DEFAULT 0,
    processed_images INTEGER NOT NULL DEFAULT 0,
    scale_factor INTEGER DEFAULT 1,
    started_at TIMESTAMP,
    completed_at TIMESTAMP,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_processing_jobs_user
        FOREIGN KEY (user_id)
        REFERENCES users(id)
        ON DELETE CASCADE
);


-- ============================================================
-- 3. TABLA DE IMÁGENES
-- ============================================================

CREATE TABLE images (
    id SERIAL PRIMARY KEY,
    job_id INTEGER NOT NULL,
    original_filename VARCHAR(255) NOT NULL,
    original_path VARCHAR(500) NOT NULL,
    mime_type VARCHAR(100) NOT NULL,
    width INTEGER NOT NULL,
    height INTEGER NOT NULL,
    file_size BIGINT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_images_job
        FOREIGN KEY (job_id)
        REFERENCES processing_jobs(id)
        ON DELETE CASCADE
);


-- ============================================================
-- 4. TABLA DE RESULTADOS
-- ============================================================

CREATE TABLE processing_results (
    id SERIAL PRIMARY KEY,
    image_id INTEGER NOT NULL,
    result_path VARCHAR(500) NOT NULL,
    width INTEGER NOT NULL,
    height INTEGER NOT NULL,
    scale_factor INTEGER NOT NULL DEFAULT 1,
    model_name VARCHAR(150),
    model_version VARCHAR(100),
    processing_time NUMERIC(12,4),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_processing_results_image
        FOREIGN KEY (image_id)
        REFERENCES images(id)
        ON DELETE CASCADE
);


-- ============================================================
-- 5. TABLA DE MÉTRICAS
-- ============================================================

CREATE TABLE metrics (
    id SERIAL PRIMARY KEY,
    result_id INTEGER NOT NULL,
    psnr NUMERIC(12,6),
    ssim NUMERIC(12,6),
    lpips NUMERIC(12,6),
    processing_time NUMERIC(12,4),
    gpu_used BOOLEAN NOT NULL DEFAULT FALSE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_metrics_result
        FOREIGN KEY (result_id)
        REFERENCES processing_results(id)
        ON DELETE CASCADE
);


-- ============================================================
-- 6. ÍNDICES
-- ============================================================

CREATE INDEX idx_processing_jobs_user_id
    ON processing_jobs(user_id);

CREATE INDEX idx_images_job_id
    ON images(job_id);

CREATE INDEX idx_processing_results_image_id
    ON processing_results(image_id);

CREATE INDEX idx_metrics_result_id
    ON metrics(result_id);
