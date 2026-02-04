# IoT API SyamFarm

RESTful API untuk IoT sensor management pada project SyamFarm. Aplikasi dibangun menggunakan FastAPI dan di-deploy ke Google Cloud Run.

## Overview

Aplikasi ini menyediakan endpoints untuk mengelola dan mengumpulkan data dari IoT sensors. Aplikasi berjalan containerized dan di-deploy ke Google Cloud Run dengan VPC connector untuk akses private ke resources.

## Tech Stack

- **Framework**: FastAPI
- **Database**: [Database yang digunakan - sesuaikan]
- **Container**: Docker
- **Cloud Platform**: Google Cloud Run
- **VPC**: Configured dengan VPC connector (`cr-connector`) di region `asia-southeast2`

## Deployment

### Prerequisites

- Docker installed
- Google Cloud CLI (`gcloud`) configured
- Access ke Google Cloud project
- Service account dengan permissions untuk Cloud Run

### Build Docker Image

```bash
docker build -t iot-sensor-api:latest .
```

### Push ke Container Registry

```bash
# Set project ID
export PROJECT_ID=your-gcp-project-id

# Tag image untuk GCR
docker tag iot-sensor-api:latest gcr.io/${PROJECT_ID}/iot-sensor-api:latest

# Push ke Google Container Registry
docker push gcr.io/${PROJECT_ID}/iot-sensor-api:latest
```

### Deploy ke Google Cloud Run

```bash
gcloud run deploy iot-sensor-api \
  --image gcr.io/${PROJECT_ID}/iot-sensor-api:latest \
  --region asia-southeast2 \
  --vpc-connector cr-connector \
  --vpc-egress private-ranges-only \
  --platform managed
```

### Update Deployment

```bash
gcloud run services update iot-sensor-api \
  --region asia-southeast2 \
  --vpc-connector cr-connector \
  --vpc-egress private-ranges-only
```

## Environment Variables

Sesuaikan environment variables di Cloud Run service:

- `DATABASE_URL` - Connection string untuk database
- `[Tambahkan env var lainnya sesuai kebutuhan]`

## Project Structure

```
.
├── Dockerfile              # Container configuration
├── requirements.txt        # Python dependencies
├── .gitignore             # Git ignore rules
└── app/
    ├── __init__.py        # Package initialization
    ├── main.py            # Application entry point
    ├── db.py              # Database configuration
    ├── models.py          # Database models
    └── schemas.py         # Pydantic schemas
```

## Dependencies

Lihat `requirements.txt` untuk daftar lengkap dependencies.

Install dependencies untuk development:

```bash
pip install -r requirements.txt
```

## API Documentation

Setelah deployment, akses Swagger documentation di:

```
https://iot-sensor-api-[hash].a.run.app/docs
```

## Monitoring

Monitor Cloud Run service melalui Google Cloud Console:

- Service logs: Cloud Logging
- Performance metrics: Cloud Monitoring
- Error tracking: Error Reporting

## Notes

- Aplikasi menggunakan VPC connector untuk akses private ke internal resources
- VPC egress diatur ke `private-ranges-only` untuk security
- Deployment region: `asia-southeast2`
